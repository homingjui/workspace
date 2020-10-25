#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid
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
    rospy.loginfo(data.info) 
    #depth_img = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
    slam_map = np.array(data.data).reshape(data.info.height, data.info.width, -1)

    rospy.loginfo(np.shape(slam_map))
    
    #rospy.loginfo(get_distance(depth_img[0,0]))
    

    img = np.zeros((data.info.height, data.info.width, 3), dtype=np.uint8)
    img[:,:,:]=slam_map
    publish_image(img)
try:
    rospy.init_node('image_pub')
    rospy.Subscriber('/map',OccupancyGrid,draw)
    img_pub = rospy.Publisher('my_image_raw',Image,queue_size=1)
    rospy.spin()
except rospy.ROSInterruptException:
        pass
