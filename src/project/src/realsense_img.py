#!/usr/bin/env python3

import pyrealsense2 as rs
import rospy
from project.msg import position_msg
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
import numpy as np


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


def draw(data):
    
    depth_img = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
    rospy.loginfo(np.shape(depth_img))
    
    #rospy.loginfo(get_distance(depth_img[0,0]))
    

    img = np.zeros((data.height, data.width, 3), dtype=np.uint8)
    img[:,:,:2]=depth_img
    y = int(data.width/2)
    x = int(data.height/2)+20
    rospy.loginfo(str(x)+" "+str(y))
    rospy.loginfo(depth_img[x-2:x+2,y-2:y+2])
    rospy.loginfo(img[x,y,0]+(255*img[x,y,1]))
    cv2.circle(img, (y, x), 5,(255, 255, 255), 1)
    publish_image(img)
try:
    rospy.init_node('image_pub')
    rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,draw)
    img_pub = rospy.Publisher('my_image_raw',Image,queue_size=1)
    rospy.spin()
except rospy.ROSInterruptException:
        pass
