#!/usr/bin/env python

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
    drawpath = np.array(np.array(data.path).reshape(-1,2))

    resize_a = 10000000
    resize_b = 10000

    side = 100

    drawpath *= resize_a
    drawpath %= resize_b

    w = int(np.max(drawpath[:,1]) - np.min(drawpath[:,1]))
    h = int(np.max(drawpath[:,0]) - np.min(drawpath[:,0]))

    img = np.zeros((w+side,h+side,3), np.uint8)

    del_x = np.min(drawpath[:,0])-side/2
    del_y = np.min(drawpath[:,1])-side/2

    #rospy.loginfo(drawpath)

    drawpath[:,0] -= del_x
    drawpath[:,1] -= del_y

    my_x = (data.now_x*resize_a)%resize_b-del_x
    my_y = (data.now_y*resize_a)%resize_b-del_y

    #rospy.loginfo(str(my_x)+' '+str(my_y))

    my_passing = np.array(np.array(data.passing)).reshape((-1, 2))
    my_passing *= resize_a
    my_passing %= resize_b
    my_passing[:,0] -= del_x
    my_passing[:,1] -= del_y

    img[:,:]=[98, 222, 95]

    my_next_p = np.array(data.next_p)
    my_next_p *= resize_a
    my_next_p %= resize_b
    my_next_p[0] -= del_x
    my_next_p[1] -= del_y


    cv2.circle(img,(int(my_x),int(my_y)), 4, (255, 0, 0), -1)
    cv2.circle(img,(int(drawpath[data.next_dot,0]),int(drawpath[data.next_dot,1])), 4, (0, 255, 255), -1)
    cv2.circle(img,(int(my_next_p[0]),int(my_next_p[1])), 4, (0, 255, 255), -1)
    cv2.polylines(img, np.int32([drawpath]), False, (255, 255, 0), 2)
    cv2.polylines(img, np.int32([my_passing]), False, (255, 0, 255), 2) 
    publish_image(img)
try:
    rospy.init_node('image_pub')
    rospy.Subscriber('position', position_msg, draw)
    img_pub = rospy.Publisher('image_raw',Image,queue_size=1)
    rospy.spin()
except rospy.ROSInterruptException:
        pass
