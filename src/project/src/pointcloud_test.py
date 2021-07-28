#!/usr/bin/env python
import rospy
import math
import sys
import struct
import numpy as np
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2
import time


np.set_printoptions(precision=5,suppress=True)
vhex = np.vectorize(hex)
pcl2_temp=PointCloud2()
pub_row = 1 

def hex_to_float(a):
    a= ("{:0>2x}" * len(a)).format(*tuple(a[::-1]))
#    print a
    return struct.unpack('!f', a.decode('hex'))[0]

def get_pcl2(data):
    global pub_row
    print ""
    print data.width
    #print data.row_step
    #print data.point_step
    #print data.fields
    pcl2_temp.header = data.header
    pcl2_temp.height = data.height
    pcl2_temp.is_bigendian = data.is_bigendian
    pcl2_temp.point_step = data.point_step
    pcl2_temp.fields = data.fields
    pcl2_temp.is_dense = False
    

    start = time.time()
    point_arr = np.ndarray(buffer=data.data,dtype=np.uint8,
            shape=(data.width,data.point_step/4,4))
    xyz_hex = np.zeros((np.shape(point_arr)[0],3),dtype=np.uint32)
    xyzrgb = np.zeros((np.shape(point_arr)[0],3),dtype=np.float32)


    xyz_hex[:,:]=point_arr[:,:3,-1]*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-2])*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-3])*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-4])
    
    sign = (-1)**(xyz_hex >>31).astype('int8')
    exp = 2**(((xyz_hex >> 23)&0xFF).astype('float64')-127)
    num = 1+(xyz_hex & 0x7FFFFF).astype('float64')/2**23
    xyzrgb = sign*exp*num
    xyzrgb = np.hstack((xyzrgb, point_arr[:,4,:3]))

    print time.time()-start
    #print time.time()-start
    print point_arr[-1]
    print vhex(point_arr[-1])
    #print hex_to_float(point_arr[-1][0])
    #print hex_to_float(point_arr[-1][1])
    #print hex_to_float(point_arr[-1][2])
    #print vhex(xyz_hex[-1])
    #print sign[-1]
    #print exp[-1]
    #print num[-1]
    print xyzrgb[-1]
   
    mydata=data.data
    pcl2_temp.row_step = data.row_step
    pcl2_temp.width = data.width
    pcl2_temp.data = mydata
    pcl2_pub.publish(pcl2_temp)

rospy.init_node('pcl2_pub_example')
rospy.Subscriber('/camera/depth/color/points',PointCloud2,get_pcl2)
pcl2_pub = rospy.Publisher('my_pcl2',PointCloud2,queue_size=1)
rospy.spin()
#except rospy.ROSInterruptException:
#    pass

