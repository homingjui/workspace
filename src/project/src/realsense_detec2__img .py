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
import math

import os

parser = argparse.ArgumentParser()

parser.add_argument("input_URI", type=str, default="", nargs='?')
parser.add_argument("output_URI", type=str, default="", nargs='?')
parser.add_argument("--overlay", type=str, default="box,labels,conf")
parser.add_argument("--threshold", type=float, default=0.5)
parser.add_argument("--network", type=str, default="facenet-120")
parser.add_argument("--camera", type=str, default="/dev/video2")


is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
        opt = parser.parse_known_args()[0]
except:
        print("")
        parser.print_help()
        sys.exit(0)
print(opt)
print(sys.argv)
sys.argv += ['--camera=/dev/video2']
#sys.argv += ['--network=facenet-120']
sys.argv += ['--threshold=0.1']

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources & outputs
#input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
#output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)


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

    img = cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA).astype(np.float32) 
    img = jetson.utils.cudaFromNumpy(img)
    detections = net.Detect(img, overlay=opt.overlay)
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
      
    for detection in detections:
        #rospy.loginfo(detection)
        detx = int(detection.Center[0])
        dety = int(detection.Center[1])
        topedge=int(detection.Top)
        bottomedge=int(detection.Bottom)
        center=int(detection.Center[0])
        cv2.circle(RGB, (detx,dety), 5,(255, 255, 255), -1)
        cv2.putText(RGB, str(depth[dety,detx]), 
                    (detx,dety), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
	
        cv2.circle(RGB, (center,topedge+10), 5,(255, 255, 255), -1)
        cv2.putText(RGB, str(depth[topedge+10,center]), 
                    (center,topedge+10), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)

        cv2.circle(RGB, (center,bottomedge-5), 5,(255, 255, 255), -1)
        cv2.putText(RGB, str(depth[bottomedge-5,center]),
                    (center,bottomedge-5), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
        
        
        if int(detection.ClassID) == 82 :
            D=math.sqrt((depth[bottomedge-5,center])**2-(329)**2)
            
            
            #objectdegree=42.5*((bottomedge-topedge)/480)
            
            left_degree=(math.atan(D/29))*(180/math.pi)
            rospy.loginfo(depth[bottomedge-5,center])
            rospy.loginfo(depth[topedge+55,center])
            rospy.loginfo(depth[dety,detx])
            #right_degree=90-left_degree
            #if objectdegree == right_degree:
            #    objectHeigh=math.sqrt((329)**2+(depth[topedge+10,center]-D)**2)
            if D == depth[topedge+10,center]:
                objectHeigh=329
            #elif objectdegree < right_degree:
                
            #    top_degree=90-objectdegree-left_degree
            #    h=(depth[topedge+10,center])*math.sin((math.pi/180)*top_degree)
            #    d=(depth[topedge+10,center])*math.cos((math.pi/180)*top_degree)
            #    x=d-D
            #    objectHeigh=math.sqrt((329-h)**2+x**2)

            #elif objectdegree > right_degree:
                
            #    top_degree=180-objectdegree-left_degree
            #    h=(depth[topedge+10,center])*math.cos((math.pi/180)*top_degree)
            #    d=(depth[topedge+10,center])*math.sin((math.pi/180)*top_degree)
            #    x=d-D
            #    objectHeigh=math.sqrt((329+h)**2+(x)**2)
            if depth[topedge+5,center] > depth[dety,detx] :
                h = math.sqrt((depth[topedge+10,center])**2-(D)**2)
                objectHeigh=329+h
                a=1
            elif depth[topedge+5,center] < depth[dety,detx] and depth[topedge+5,center] > D:
                h = math.sqrt((depth[topedge+5,center])**2-(D)**2)
                objectHeigh=329+h
                a=2
            elif depth[topedge+5,center] < depth[dety,detx] :
                h = math.sqrt((depth[topedge+10,center])**2-(D)**2)
                objectHeigh=329-h
                a=3
           
            rospy.loginfo(detection)
            rospy.loginfo(D)
            rospy.loginfo(a)
            #rospy.loginfo(objectdegree)
            #rospy.loginfo(left_degree)
            #rospy.loginfo(right_degree)
            #rospy.loginfo(top_degree)
            rospy.loginfo(h)
            #rospy.loginfo(d)
            #rospy.loginfo(x)
            rospy.loginfo(objectHeigh)
            
            f2=open('/home/isp/Desktop/tmp.txt','r+')
            f2.read()
            
            f2.write(str(depth[topedge+5,center])+' '+str(depth[bottomedge-5,center])+' '+str(depth[dety,detx])+' '+str(D)+' '+str(objectHeigh)+'\n')
            #f2.write(str(objectHeigh))
            f2.close()

            cv2.putText(RGB,'Heigh='+str(objectHeigh),(detx+20,dety+20),cv2.FONT_HERSHEY_SIMPLEX,1, (0,255,255), 1, cv2.LINE_AA)    
    


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
