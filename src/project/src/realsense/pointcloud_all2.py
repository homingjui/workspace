#!/usr/bin/env python
import rospy
import math
import cv2
import sys
import struct
import numpy as np
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField
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
    #print(np.shape(imgdata))
    #image_temp.is_bigendian=True
    image_temp.header=header
    image_temp.step=np.shape(imgdata)[1]*3
    img_pub.publish(image_temp)


def hex_to_float(a):
    a= ("{:0>2x}" * len(a)).format(*tuple(a[::-1]))
    return struct.unpack('!f', a.decode('hex'))[0]

def pcl_lable(x,y,d=200,r=255,g=255,b=255):

    x_y = np.array(y)-x
    xyz=np.repeat(np.arange(d,dtype=np.float32)/d,3).reshape((d,3))*x_y+x
    rgb=np.repeat([[0,0,0,0,r,g,b,0]],d,axis=0).reshape((d,8))
    return xyz,rgb

def pcl_box(xyz_min,xyz_max):
    lable_xyz,lable_rgb=pcl_lable([xyz_min[0],xyz_max[1],xyz_max[2]],[xyz_max[0],xyz_max[1],xyz_max[2]])
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_min[1],xyz_max[2]],[xyz_max[0],xyz_max[1],xyz_max[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_max[1],xyz_min[2]],[xyz_max[0],xyz_max[1],xyz_max[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_min[0],xyz_min[1],xyz_max[2]],[xyz_min[0],xyz_min[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_min[0],xyz_max[1],xyz_min[2]],[xyz_min[0],xyz_min[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_min[1],xyz_min[2]],[xyz_min[0],xyz_min[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_min[0],xyz_max[1],xyz_max[2]],[xyz_min[0],xyz_max[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_max[1],xyz_min[2]],[xyz_min[0],xyz_max[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_max[1],xyz_min[2]],[xyz_max[0],xyz_min[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_min[1],xyz_max[2]],[xyz_max[0],xyz_min[1],xyz_min[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_min[0],xyz_max[1],xyz_max[2]],[xyz_min[0],xyz_min[1],xyz_max[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    xyz_t,rgb_t=pcl_lable([xyz_max[0],xyz_min[1],xyz_max[2]],[xyz_min[0],xyz_min[1],xyz_max[2]])
    lable_xyz=np.vstack((lable_xyz,xyz_t))
    lable_rgb=np.vstack((lable_rgb,rgb_t))
    return lable_xyz,lable_rgb

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

lable=PointCloud2()
lable.header.frame_id="camera_color_optical_frame"
lable.height=1
lable.fields=[
        PointField('x', 0, PointField.FLOAT32, 1),
        PointField('y', 4, 7, 1),
        PointField('z', 8, 7, 1),
        PointField('rgb', 16, 7, 1)
        ]
lable.is_bigendian=False
lable.point_step=20
is_dense=False


#lable.width=?
#lable.row_step=?
#lable.data=?


mytime=time()
plt.show()

def new_pcl2(pcl2):
    global mytime
    #print ""
    fps=round(1/(time()-mytime),3)
    #print(fps)
    mytime=time()
    
    pcl2_temp=PointCloud2()
    pcl2_temp.header=pcl2.header
    #pcl2_temp.header.frame_id="mypcl2"
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
    #print(point_arr[0])

    rgb = np.array(point_arr[:,-2:])
    myrgb=np.reshape(rgb[:,1,:3],(height,width,3))
    #myrgb.dtype=uint8
    hsv=cv2.cvtColor(myrgb, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,np.array([30,50,50]),np.array([80,255,255]))
    n,lables,stats,centroids=cv2.connectedComponentsWithStats(mask)
    my_lable=np.where(stats==stats[1:,-1].max())[0][0]
    #print(my_lable)
    #print(stats[my_lable])
    mask[lables!=my_lable]=0
    #print(np.shape(mask))
    myrgb=cv2.bitwise_and(myrgb,myrgb,mask=mask)
    myrgb=cv2.putText(myrgb, "fps:"+str(fps), (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 2)
    #myrgb=myrgb.get()
    publish_image(myrgb)
    
   
    a=time()
    xyz_hex = np.zeros((width*height,3),dtype=np.uint32)
    #print(time()-a)
    a=time()
    xyz_hex[:,:]=point_arr[:,:3,-1]*256
    #print(time()-a)
    a=time()
    xyz_hex=(xyz_hex+point_arr[:,:3,-2])*256
    #print(time()-a)
    a=time()
    xyz_hex=(xyz_hex+point_arr[:,:3,-3])*256
    #print(time()-a)
    a=time()
    xyz_hex=(xyz_hex+point_arr[:,:3,-4])
    #print(time()-a)
    a=time()
    sign = (-1)**(xyz_hex >>31).astype('int8')
    #print(time()-a)
    a=time()
    exp = np.power(2,((xyz_hex >> 23)&0xFF).astype('float64')-127)
    #print(time()-a)
    a=time()
    num = 1+(xyz_hex & 0x7FFFFF).astype('float64')/2**23
    #print(time()-a)
    a=time()
    xyz = (sign*exp*num).astype('float32') 
    #print(time()-a)
    a=time()
    xyz[np.any(np.isinf(xyz),axis=1)]=np.nan
    #print(time()-a)
    a=time()
    '''
    xyzo = np.array(xyz)
    xyz[:,0] /= xyz[:,2]
    xyz[:,1] /= xyz[:,2]
    xyz[:,2] /= xyz[:,2]
    new_pcl2 = np.array(xyz.data).reshape((-1,3,4))
    new_pcl2 = np.hstack((new_pcl2, rgb))
    new_pcl2 = new_pcl2.reshape(-1)
    #print pcl2_temp 
    pcl2_temp.data = new_pcl2.tobytes()
    pcl2_pub.publish(pcl2_temp)
    '''
    
    box_xyz=np.array(xyz).reshape((-1,3))
    mask=mask.reshape((-1))
    box_xyz=box_xyz[mask==255]
    box_xyz=box_xyz[~np.isnan(box_xyz[:,0])]
    #print(len(box_xyz))

    for i in range(3):
        q1=np.quantile(box_xyz[:,i],0.25)
        q3=np.quantile(box_xyz[:,i],0.75)
        irq=q3-q1
        box_xyz=box_xyz[box_xyz[:,i]>(q1-1.5*irq)]
        box_xyz=box_xyz[box_xyz[:,i]<(q3+1.5*irq)]

    #print(len(box_xyz))

    '''
    plt.subplot(231)
    plt.hist(box_xyz[:,0]*100)
    plt.subplot(232)
    plt.hist(box_xyz[:,1]*100)
    plt.subplot(233)
    plt.hist(box_xyz[:,2]*100)
    plt.subplot(234)
    plt.boxplot(box_xyz[:,0]*100)
    plt.subplot(235)
    plt.boxplot(box_xyz[:,1]*100)
    plt.subplot(236)
    plt.boxplot(box_xyz[:,2]*100)
    plt.draw()
    plt.pause(0.001)
    plt.clf()
    '''

    xyz_max=np.nanmax(box_xyz,axis=0)
    xyz_min=np.nanmin(box_xyz,axis=0)
    lable_xyz,lable_rgb=pcl_box(xyz_min,xyz_max)

    #print(len(lable_xyz))
    lable.width=len(lable_xyz)
    lable.row_step=len(lable_xyz)*20
    
    lable_xyz = np.array(np.array(lable_xyz,dtype=np.float32).data).reshape((-1,3,4))
    #print np.shape(lable_xyz)

    lable_rgb=np.array(lable_rgb,dtype=np.uint8).reshape((-1,2,4))
    #print(np.shape(lable_rgb))
    
    lable_data = np.hstack((lable_xyz, lable_rgb))
    #print lable_data[0]
    lable_data = lable_data.reshape(-1)
    lable.data = lable_data.tobytes()
    pcl2_pub.publish(lable)
    

rospy.init_node('pcl2_pub_example')
rospy.Subscriber('/camera/depth_registered/points',PointCloud2,new_pcl2,queue_size=1)
pcl2_pub = rospy.Publisher('my_pcl2',PointCloud2,queue_size=1)
img_pub = rospy.Publisher('pcl2_image',Image,queue_size=1)
try:
    rospy.spin()
except rospy.ROSInterruptException:
    pass
