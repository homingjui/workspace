#!/usr/bin/env python3

#import pyrealsense2 as rs
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

hfov = 42*(np.pi/180)
vfov = 69*(np.pi/180)

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
    #rospy.loginfo(np.shape(depth_img))
    
    depth = np.zeros((data.height, data.width), dtype=np.uint16)
    print ("d",depth_img[0,0])
    depth[:,:] = depth_img[:,:,1]
    depth *= 255
    depth += depth_img[:,:,0]

    #rospy.loginfo(depth.max())

    color = np.array(depth, dtype=np.float64)
    if color.max() > max_len:
        max_len=color.max()
    color = (color/color.max())*1023
    color = color.astype(np.uint16)

    dimg = np.zeros((data.height, data.width, 3), dtype=np.uint8)

    dimg[:,:,:]=[colorlib[i] for i in color]

    x = int(data.width/2)
    y = int(data.height/2)
    #rospy.loginfo(str(x)+" "+str(y))
    #rospy.loginfo(depth_img[x,y])
    img = np.array(RGB)
    img[y,:,:]=[255,255,255]
    img[:,x,:]=[255,255,255]
    cv2.circle(img, (x, y), 5,(255, 255, 255), 0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.medianBlur(gray, 25) #cv2.bilateralFilter(gray,10,50,50)

    minDist = 100
    param1 = 30 #500
    param2 = 50 #200 #smaller value-> more false circles
    minRadius = 2
    maxRadius = 100 #10

# docstring of HoughCircles: HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, 
                                param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img, (i[0], i[1]), 5, (0, 255, 0), -1)
            x_deg = (vfov/2)*(abs(x-i[0])/x)
            y_deg = (hfov/2)*(abs(y-i[1])/y)
            point_tf = [0,0,0]
            point_tf[0] = depth[i[1],i[0]]*np.cos(x_deg)*np.cos(y_deg)
            point_tf[1] = depth[i[1],i[0]]*np.sin(x_deg) 
            point_tf[2] = depth[i[1],i[0]]*np.sin(y_deg) 
            #alpha = depth*np.cos()
            rospy.loginfo((x_deg,y_deg,depth[i[1],i[0]],np.cos(x_deg),np.cos(y_deg),point_tf))
            rospy.loginfo(depth[x,y])
            rospy.loginfo("")
    #img_pub = cv2.addWeighted(img,0.9,dimg,0.1,0)
    #publish_image(img_pub)
    publish_image(img)
try:
    rospy.init_node('image_pub')
    rospy.Subscriber('/camera/color/image_raw',Image,getRGB)
    rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,draw)
    img_pub = rospy.Publisher('rs_image_raw',Image,queue_size=1)
    rospy.spin()
except rospy.ROSInterruptException:
        pass
