#!/usr/bin/env python
import rospy
import math
import sys
import struct
import numpy as np
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2
import time
import matplotlib.pyplot as plt 
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
#    print a
    return struct.unpack('!f', a.decode('hex'))[0]


#sigma = np.zeros((60,3))
sigma = []
del_t = 0
t_rec = []
filtera=[]
filterb=[]
ori = []
filtn = 'a'

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

myrgb = np.zeros((300,400,3))

def new_pcl2(pcl2):
    global del_t,t_rec,filtera,filterb,ori
    print ""
    pcl2_temp=PointCloud2()
    pcl2_temp.header=pcl2.header
    pcl2_temp.height=pcl2.height
    pcl2_temp.fields=pcl2.fields
    pcl2_temp.is_bigendian=pcl2.is_bigendian
    pcl2_temp.point_step=pcl2.point_step
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
    xyzo = np.array(xyz)
    #print point_arr[-1]
    #print vhex(point_arr[-1])

    #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    
    xyz[:,0] /= xyz[:,2]
    xyz[:,1] /= xyz[:,2]
    xyz[:,2] /= xyz[:,2]

    x_max = xyz[:,0].max()
    x_min = xyz[:,0].min()
    x_l = x_max-x_min
    y_max = xyz[:,1].max()
    y_min = xyz[:,1].min()
    y_l = y_max-y_min
   
   
    
    del_x = int(10000*(x_max-x_min)/3.999)
    del_y = int(10000*(y_max-y_min)/2.999)
    xyz[:,0] *= 1000000
    xyz[:,1] *= 1000000
    xyz[:,0] -= x_min
    xyz[:,0] /= del_x
    xyz[:,1] -= y_min
    xyz[:,1] /= del_y
    xyz = xyz[:,:2].astype('int32')
    xyz[:,0] += -xyz[:,0].min()
    xyz[:,1] += -xyz[:,1].min()
    print (x_min,x_max,(x_max-x_min)/4)
    print xyz[:,0].max()
    print xyz[:,1].max()

    myrgb = np.zeros((300,400,3))
    myrgb -= 1
    myrgb[xyz[:,1],xyz[:,0]]=rgb[:,1,:3]
    print len(myrgb[myrgb[:,:,0] != -1])
    #publish_image(myrgb.astype('uint8'))
    myrgb =myrgb.reshape((120000,3))
    myz = np.zeros((300,400))
    myz[xyz[:,1],xyz[:,0]]=xyzo[:,2]

    myxyz = np.zeros((300,400,3))
    myxyz[xyz[:,1],xyz[:,0]]=xyzo[:]
    myxyz =myxyz.reshape((120000,3))
    
    #line_w = 0.0025
    #mask = ((xyz[:,0]>x_min+(x_l*(0.5-line_w))) &
    #       (xyz[:,0]<x_min+(x_l*(0.5+line_w)))) 
    #rgb[mask,-1]=[255,0,0,0]
    #mask = ((xyz[:,1]>y_min+(y_l*(0.5-line_w))) & 
    #       (xyz[:,1]<y_min+(y_l*(0.5+line_w)))) 
    #rgb[mask,-1]=[0,255,0,0]
    #print xyz[:,2].max()
    #print xyz[-1]

    ################################################## do your work below
    #### pcl2_temp.width: points num
    #### xyz: array for points xyz -> [x,y,z]* points num
    #### rgb: array for points rgb -> [r,g,b,0]* points num
    
    sigma.append(myz.flatten())
    t_rec.append(time.time()-del_t)
    del_t = time.time()
    if len(sigma)>=6:
        sigmanp=np.array(sigma)

        cutoff_hz = 0.025
        
        mask = sigmanp[1:,:]==0
        
        sigmamask2=sigmanp[:-1]
        sigmamask=sigmanp[1:]
        sigmamask[mask]=sigmamask2[mask]

        sigmanp = np.average(sigmamask,axis=0)
        #print np.shape(sigmanp)

        xyzave = myz.flatten()
        #print len(xyzave[xyzave!=0])
        xyzave = sigmanp/xyzave
        print np.shape(xyzave)
        print np.shape(myxyz)
        myxyz[:,0] *= xyzave
        myxyz[:,1] *= xyzave
        myxyz[:,2] *= xyzave
        
        myxyz = myxyz[(~np.isnan(xyzave)) & (xyzave!=0)]
        myxyz = myxyz.astype('float32')
        myrgb = myrgb[(~np.isnan(xyzave)) & (xyzave!=0)]
        #xyzave = xyzave[(~np.isnan(xyzave)) & (xyzave!=0)]
        
        print np.shape(myxyz)
        print myxyz[0]
        print myrgb[0]
        newrgb = np.zeros((len(myrgb),2,4))
        newrgb[:,1,:3]=myrgb[:]
        newrgb = newrgb.astype('uint8')
        #print newrgb[0]


        sigma.pop(0)
    ################################################## finish your work here
     
        pcl2_temp.width=len(myxyz)
        pcl2_temp.row_step=len(myxyz)*20
        
        new_pcl2 = np.array(myxyz.data).reshape((-1,3,4))
        new_pcl2 = np.hstack((new_pcl2, newrgb))
        new_pcl2 = new_pcl2.reshape(-1)
        #mydata = new_pcl2.tolist()
        #pcl2_temp.data = mydata
    
        pcl2_temp.data = new_pcl2.tobytes()
        pcl2_pub.publish(pcl2_temp)
    
rospy.init_node('pcl2_pub_example')
rospy.Subscriber('/camera/depth/color/points',PointCloud2,new_pcl2,queue_size=1)
pcl2_pub = rospy.Publisher('my_pcl2',PointCloud2,queue_size=1)
img_pub = rospy.Publisher('pcl2_image',Image,queue_size=1)
try:
    rospy.spin()
except rospy.ROSInterruptException:
    pass
