#!/usr/bin/env python
import rospy
import math
import sys

import numpy as np
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2

pcl2_temp=PointCloud2()
pub_row = 1 
def get_pcl2(data):
    global pub_row
    print ""
    print data.width
    print data.row_step
    print data.point_step
    print data.fields
    pcl2_temp.header = data.header
    pcl2_temp.height = data.height
    pcl2_temp.is_bigendian = data.is_bigendian
    pcl2_temp.point_step = data.point_step
    pcl2_temp.fields = data.fields
    pcl2_temp.is_dense = False
    point_arr = np.ndarray(buffer=data.data,dtype=np.uint8,
            shape=(data.width,data.point_step/4,4))
    #print point_arr[-1]
    #point = pcl2.read_points(data)
    #print next(point)[3].hex()
    #    point_arr.append(point)
    #print point_arr[0][3].hex()[2:9]
    #print type(point_arr[0])
    pcl2_temp.row_step = data.point_step*pub_row
    pcl2_temp.width = pub_row
    pcl2_temp.data = data.data[:data.point_step*pub_row]
    pcl2_pub.publish(pcl2_temp)
    pub_row += 2000
    if pcl2_temp.row_step > data.row_step:
        pub_row=0

rospy.init_node('pcl2_pub_example')
rospy.Subscriber('/camera/depth/color/points',PointCloud2,get_pcl2)
pcl2_pub = rospy.Publisher('my_pcl2',PointCloud2,queue_size=1)
rospy.spin()
#except rospy.ROSInterruptException:
#    pass

