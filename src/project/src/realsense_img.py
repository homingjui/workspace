#!/usr/bin/env python3

import pyrealsense2 as rs
import rospy
from project.msg import position_msg
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
import numpy as np

import jetson.inference
import jetson.utils

import argparse
import sys

colorlib = np.zeros((256*4,3), dtype=np.uint8)
colorlib[1:256,0] = 255
colorlib[256:256*2,0] = np.arange(255,-1,-1)
colorlib[0:256,1] = np.arange(0,256)
colorlib[256:256*3,1]= 255
colorlib[256*3:256*4,1]= np.arange(255,-1,-1)
colorlib[256*2:256*3,2] = np.arange(0,256)
colorlib[256*3:256*4,2]= 255
colorlib = (colorlib/50)*50
RGB = []
max_len = 0

def publish_image(imgdata):
    image_temp=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height=np.shape(imgdata)[0]
    image_temp.width=np.shape(imgdata)[1]
    image_temp.encoding='rgb8'
    image_temp.data=np.array(imgdata).tostring()
    #print(imgdata)
    #image_temp.is_bigendian=True
    image_temp.header=header
    image_temp.step=np.shape(imgdata)[1]*3
    img_pub.publish(image_temp)

def getRGB(data):
    global RGB,detections
    RGB = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1) 

    #img = cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA).astype(np.float32) 
    #img = jetson.utils.cudaFromNumpy(img)
    #detections = net.Detect(img, overlay=opt.overlay)
    #img2 = jetson.utils.cudaToNumpy(img, 1280, 720, 4)
    #img2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGBA2RGB).astype(np.uint8)
    #img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
    #for detection in detections:
    #    rospy.loginfo(detection)
    #    cv2.circle(RGB, (int(detection.Center[0]),int(detection.Center[1]) ), 5,(255, 0, 255), -1)
    #rospy.loginfo(len(detections))
    

def draw(data):
    global max_len 
    depth_img = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
    rospy.loginfo(np.shape(depth_img))
    
    depth = np.zeros((data.height, data.width), dtype=np.uint16)
    depth[:,:] = depth_img[:,:,1]
    depth *= 255
    depth += depth_img[:,:,0]

    rospy.loginfo(depth.max())

    color = np.array(depth, dtype=np.float64)
    if color.max() > max_len:
        max_len=color.max()
    color = (color/color.max())*1023
    color = color.astype(np.uint16)

    img = np.zeros((data.height, data.width, 3), dtype=np.uint8)

    img[:,:,:]=[colorlib[i] for i in color]

    y = int(data.width/2)
    x = int(data.height/2)+20
    rospy.loginfo(str(x)+" "+str(y))
    rospy.loginfo(depth[x,y])
    #rospy.loginfo(depth_img[x,y])
    cv2.circle(img, (y, x), 5,(255, 255, 255), 1)
    img_pub = cv2.addWeighted(RGB,0.5,img,0.5,0)
    publish_image(img_pub)
try:
    rospy.init_node('image_pub')
    rospy.Subscriber('/camera/color/image_raw',Image,getRGB)
    rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,draw)
    img_pub = rospy.Publisher('my_image_raw',Image,queue_size=1)
    rospy.spin()
except rospy.ROSInterruptException:
        pass
