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


vhex=np.vectorize(hex)

def hex_to_float(a):
    a= ("{:0>2x}" * len(a)).format(*tuple(a[::-1]))
#    print a
    return struct.unpack('!f', a.decode('hex'))[0]

pcl2=None
def new_pcl2(data):
    global pcl2
    pcl2=data

def pub_pcl2():
    print ""
    pcl2_temp=PointCloud2()
    pcl2_temp.header=pcl2.header
    pcl2_temp.height=pcl2.height
    pcl2_temp.width=pcl2.width
    pcl2_temp.fields=pcl2.fields
    pcl2_temp.is_bigendian=pcl2.is_bigendian
    pcl2_temp.point_step=pcl2.point_step
    pcl2_temp.row_step=pcl2.row_step
    pcl2_temp.is_dense=pcl2.is_dense
    print pcl2_temp.width

    start = time.time()
    point_arr = np.ndarray(buffer=pcl2.data,dtype=np.uint8,
            shape=(pcl2.width,pcl2.point_step/4,4))
    rgb = np.array(point_arr[:,-2:])
    xyz_hex = np.zeros((np.shape(point_arr)[0],3),dtype=np.uint32)


    xyz_hex[:,:]=point_arr[:,:3,-1]*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-2])*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-3])*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-4])

    sign = (-1)**(xyz_hex >>31).astype('int8')
    exp = 2**(((xyz_hex >> 23)&0xFF).astype('float64')-127)
    num = 1+(xyz_hex & 0x7FFFFF).astype('float64')/2**23
    xyz = sign*exp*num
    xyz = xyz.astype('float32')

    ################################################## do your work below
    #### pcl2_temp.width: points num
    #### xyz: array for points xyz -> [x,y,z]* points num
    #### rgb: array for points rgb -> [r,g,b,0]* points num

    ################################################## finish your work here
    new_pcl2 = np.array(xyz.data).reshape((-1,3,4))
    new_pcl2 = np.hstack((new_pcl2, rgb))
    new_pcl2 = new_pcl2.reshape(-1)

    mydata = new_pcl2.tolist()
    pcl2_temp.data = mydata
    print time.time()-start
    pcl2_pub.publish(pcl2_temp)
    print time.time()-start
rospy.init_node('pcl2_pub_example')
rospy.Subscriber('/camera/depth/color/points',PointCloud2,new_pcl2,queue_size=1)
pcl2_pub = rospy.Publisher('my_pcl2',PointCloud2,queue_size=1)
try:
    while pcl2==None:
        print "wait"
    while not rospy.is_shutdown():
        pub_pcl2()
except rospy.ROSInterruptException:
    pass
