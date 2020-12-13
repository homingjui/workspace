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


myclassID = {0:"__background__", 1:"person", 2:"bicycle", 3:"car", 4:"motorcycle", 5:"airplane", 6:"bus", 7:"train", 8:"truck", 9:"boat", 10:"traffic light", 11:"fire hydrant", 12:"stop sign", 13:"parking meter", 14:"bench", 15:"bird", 16:"cat", 17:"dog", 18:"horse", 19:"sheep", 20:"cow", 21:"elephant", 22:"bear", 23:"zebra", 24:"giraffe", 25:"backpack", 26:"umbrella", 27:"handbag", 28:"tie", 29:"suitcase", 30:"frisbee", 31:"skis", 32:"snowboard", 33:"sports ball", 34:"kite", 35:"baseball bat", 36:"baseball glove", 37:"skateboard", 38:"surfboard", 39:"tennis racket", 40:"bottle", 41:"wine glass", 42:"cup", 43:"fork", 44:"knife", 45:"spoon", 46:"bowl", 47:"banana", 48:"apple", 49:"sandwich", 50:"orange", 51:"broccoli", 52:"carrot", 53:"hot dog", 54:"pizza", 55:"donut", 56:"cake", 57:"chair", 58:"couch", 59:"potted plant", 60:"bed", 61:"dining table", 62:"chair", 63:"tv", 64:"laptop", 65:"mouse", 66:"remote", 67:"keyboard", 68:"cell phone", 69:"microwave", 70:"oven", 71:"toaster", 72:"sink", 73:"refrigerator", 74:"book", 75:"clock", 76:"vase", 77:"scissors", 78:"teddy bear", 79:"hair drier", 80:"toothbrush",81:"",82:"",83:"",84:"",85:"",86:"",87:"",88:"",89:"",90:"",91:"",92:""}

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
sys.argv += ['--threshold=0.3']

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
        rospy.loginfo(detection)
        #rospy.loginfo(myclassID[detection.ClassID])
        detx = int(detection.Center[0])
        dety = int(detection.Center[1])
        cv2.circle(RGB, (detx,dety), 5,(255, 255, 255), -1)
        cv2.putText(RGB, str(depth[dety,detx])+" "+myclassID[detection.ClassID], 
                    (detx,dety), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)

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
