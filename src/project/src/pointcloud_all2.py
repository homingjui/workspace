#!/usr/bin/env python
import rospy
import math
import cv2
import sys
import struct
import numpy as np
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2
from time import time
import matplotlib.pyplot as plt
import cv_bridge
#from scipy.fftpack import fft,fftfreq
#from scipy.signal import kaiserord, lfilter, firwin, freqz
#from scipy import signal

vhex=np.vectorize(hex)

def publish_image(imgdata):
    image_temp=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height=np.shape(imgdata)[0]
    image_temp.width=np.shape(imgdata)[1]
    image_temp.encoding='bgr8'
    image_temp.data=np.array(imgdata).tostring()
    print(np.shape(imgdata))
    #image_temp.is_bigendian=True
    image_temp.header=header
    image_temp.step=np.shape(imgdata)[1]*3
    img_pub.publish(image_temp)


def hex_to_float(a):
    a= ("{:0>2x}" * len(a)).format(*tuple(a[::-1]))
    return struct.unpack('!f', a.decode('hex'))[0]


def myfilter(arr):
        
    if filtn == 'a':
        b, a = signal.butter(3, cutoff_hz)
        y = signal.filtfilt(b, a, arr[:,2])
        return y[-2]

    elif filtn == 'b':
        T = np.average(t_rec[1:])
        sample_rate = 1/T
        nyq_rate = sample_rate / 2.0
        width = 5.0/nyq_rate
        ripple_db = 60.0
        N, beta = kaiserord(ripple_db, width)
        taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta),fs=sample_rate)
        y = lfilter(taps, 1.0, arr[:,2])
        return y[-2]


mytime=time()

def new_pcl2(pcl2):
    global mytime
    print ""
    fps=round(1/(time()-mytime),3)
    mytime=time()
    
    pcl2_temp=PointCloud2()
    pcl2_temp.header=pcl2.header
    pcl2_temp.width=pcl2.width
    pcl2_temp.height=pcl2.height
    pcl2_temp.fields=pcl2.fields
    pcl2_temp.is_bigendian=pcl2.is_bigendian
    pcl2_temp.point_step=20
    #pcl2_temp.point_step=pcl2.point_step
    pcl2_temp.is_dense=pcl2.is_dense
    width = pcl2.width
    height = pcl2.height
    pcl2_temp.row_step=width*height*20

    point_arr = np.ndarray(buffer=pcl2.data,dtype=np.uint8,
            shape=(width*height,pcl2.point_step/4,4))
    point_arr=point_arr[:,:5]

    rgb = np.array(point_arr[:,-2:])
    myrgb=np.reshape(rgb[:,1,:3],(height,width,3))
    #myrgb.dtype=uint8
    myrgb=cv2.putText(myrgb, "fps:"+str(fps), (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 2)
    myrgb=myrgb.get()
    publish_image(myrgb)
    
    
    xyz_hex = np.zeros((width*height,3),dtype=np.uint32)
    xyz_hex[:,:]=point_arr[:,:3,-1]*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-2])*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-3])*256
    xyz_hex=(xyz_hex+point_arr[:,:3,-4])

    sign = (-1)**(xyz_hex >>31).astype('int8')
    exp = 2**(((xyz_hex >> 23)&0xFF).astype('float64')-127)
    num = 1+(xyz_hex & 0x7FFFFF).astype('float64')/2**23
    xyz = sign*exp*num
    xyz = xyz.astype('float32') 
    
    xyz[np.any(xyz==-np.inf,axis=1)]=np.nan
    xyz[np.any(xyz==np.inf,axis=1)]=np.nan

    xyzo = np.array(xyz)

    xyz[:,0] /= xyz[:,2]
    xyz[:,1] /= xyz[:,2]
    xyz[:,2] /= xyz[:,2]

   

        
    new_pcl2 = np.array(xyz.data).reshape((-1,3,4))
    new_pcl2 = np.hstack((new_pcl2, rgb))
    new_pcl2 = new_pcl2.reshape(-1)
    
    pcl2_temp.data = new_pcl2.tobytes()
    pcl2_pub.publish(pcl2_temp)


rospy.init_node('pcl2_pub_example')
rospy.Subscriber('/camera/depth_registered/points',PointCloud2,new_pcl2,queue_size=1)
pcl2_pub = rospy.Publisher('my_pcl2',PointCloud2,queue_size=1)
img_pub = rospy.Publisher('pcl2_image',Image,queue_size=1)
try:
    rospy.spin()
except rospy.ROSInterruptException:
    pass
