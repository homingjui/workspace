#!/usr/bin/env python3

import rospy
from project.msg import deg_msg,motor_msg
from nav_msgs.msg import OccupancyGrid
from sensor_msgs.msg import Image,LaserScan
from std_msgs.msg import Header
from tf2_msgs.msg import TFMessage
import cv2
import numpy as np
import math
from scipy.spatial.transform import Rotation
import time


rout = np.array([[0,0],[1.1,1.1],[2.1,0],[1.1,-1.1]])
for i in range(1,len(rout)):
    rout[i]=[rout[i,0]*np.cos(np.pi/2)-rout[i,1]*np.sin(np.pi/2),
             rout[i,0]*np.sin(np.pi/2)+rout[i,1]*np.cos(np.pi/2)]

setup=np.array([False,False,False])

def get_deg(vac1,vac2):
    #Lx=np.sqrt(vac1.dot(vac1))
    #Ly=np.sqrt(vac2.dot(vac2))
        
    norm = np.linalg.norm(vac1)*np.linalg.norm(vac2)
    rho = np.arcsin(np.cross(vac1,vac2)/norm)
    cos_ang= vac1.dot(vac2) / norm
    
    #rospy.loginfo(math.atan2(vac2[0]-vac1[0], vac2[1]-vac1[1]))
    ang=np.arccos(cos_ang)
    if rho>0:
        return -ang
    #rospy.loginfo(ang)
    return ang

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

def update_pos(data):
    global now_x,now_y,xyz
    setup[0]=True
    tf = data.transforms[0]
    now_x = tf.transform.translation.x
    now_y = tf.transform.translation.y
    tfx = tf.transform.rotation.x
    tfy = tf.transform.rotation.y
    tfz = tf.transform.rotation.z
    tfw = tf.transform.rotation.w
    #rospy.loginfo(tf)
    rot = Rotation.from_quat([tfx, tfy, tfz, tfw])
    xyz = rot.as_euler('xyz')
    #rospy.loginfo(xyz)
    #draw()

def update_map(data):
    global slam_map,w,h,res,map_pos
    setup[1]=True
    slam_map = np.array(data.data).reshape(data.info.height, data.info.width, -1)
    w = data.info.width
    h = data.info.height
    res = data.info.resolution
    map_pos = data.info.origin.position

def update_scan(data):
    global len_per_ndeg,angle_min,angle_n
    setup[2]=True
    header = data.header
    ranges = data.ranges
    #rospy.loginfo(header)
    #rospy.loginfo(len(ranges))
    len_per_deg = ranges[::4]
    #rospy.loginfo(len(len_per_deg))
    angle_n = 15
    len_per_ndeg = len_per_deg[::angle_n]
    #rospy.loginfo(len(len_per_45deg))
    angle_min = data.angle_min
    #rospy.loginfo(angle_min)
    #draw()


#angle_min: -3.1241390705108643
#angle_max: 3.1415927410125732
#angle_increment: 0.004354226402938366
#time_increment: 5.4129151976667345e-05
#scan_time: 0.07789184898138046
#range_min: 0.15000000596046448
#range_max: 25.0
#ranges:

def draw():
    #rospy.loginfo(np.shape(slam_map))
    
    map_x = -map_pos.x / res
    map_y = -map_pos.y / res

    x = (-map_pos.x+now_x) / res
    y = (-map_pos.y+now_y) / res

    dot_size = h/100
    img = np.zeros((h, w, 3), dtype=np.uint8)
    try:
        img[:,:,:]=slam_map[:,:,:]
    except ValueError:
        rospy.loginfo("ValueError")
    img[ (img[:,:,0]!=255) & (img[:,:,0]>=60)  ] = [255,0,0]
    
    rad_angle_n = angle_n*np.pi/180

    for i in range(len(rout)-1):
        cv2.line(img, (int(map_x+rout[i,0]/res),int(map_y+rout[i,1]/res)),
                      (int(map_x+rout[i+1,0]/res),int(map_y+rout[i+1,1]/res)),
                    (144, 144, 0), int(1+(dot_size)/5))


    #for i in range(len(len_per_ndeg)):
        #if len_per_ndeg[i]==float("inf"):
        #    continue
        #rospy.loginfo(len_per_ndeg[i])
        #scan_col = 0
        #if len_per_ndeg[i] < 1:
        #    scan_col = 255
        #cv2.line(img, (int(x),int(y)), 
        #         (int(x+(len_per_ndeg[i]*np.cos(xyz[2]+angle_min+(rad_angle_n*i)))/res),
        #          int(y+(len_per_ndeg[i]*np.sin(xyz[2]+angle_min+(rad_angle_n*i)))/res)),
        #          (scan_col, 255, 0), int(1+(dot_size)/5))

    cv2.circle(img, (int(map_x),int(map_y)), int(1+dot_size),(0, 255, 255), -1)
    cv2.circle(img, (int(x),int(y)),int(1+dot_size),(0, 0, 255), -1)
    cv2.line(img, (int(x),int(y)), (int(x-5*dot_size*np.cos(xyz[2])),
                int(y-5*dot_size*np.sin(xyz[2]))),
                (0, 0, 255), int(1+(dot_size*2)/3))
    #img = cv2.flip(img, 1)
    publish_image(img)


try:
    rospy.init_node('slam_control')
    rospy.Subscriber('/scan',LaserScan,update_scan)
    rospy.Subscriber('/tf',TFMessage,update_pos)
    rospy.Subscriber('/map',OccupancyGrid,update_map)
    img_pub = rospy.Publisher('my_image_raw',Image,queue_size=1)
    pub_deg = rospy.Publisher('revise_deg', deg_msg, queue_size=10)
    pub_mot = rospy.Publisher('auto_motion', motor_msg, queue_size=10)

    deg = deg_msg()
    #rate = rospy.wallRate(1) # 10hz
    rospy.loginfo("wait to start")
    while setup.all() != True:
        if rospy.is_shutdown():
            break
        continue
    rospy.loginfo(setup)
    rospy.loginfo("done")
    
    rospy.set_param("/turning",True)
    deg = get_deg(np.array([-1,0]),rout[1]-rout[0])

    pub_deg.publish(deg)
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(rout[1])
        rospy.loginfo((now_x,now_y))
        rospy.loginfo(np.linalg.norm([rout[1,0]-now_x,rout[1,1]-now_y]))
        deg = get_deg(np.array([-np.cos(xyz[2]),-np.sin(xyz[2])]),rout[1]-rout[0])
        rospy.loginfo(deg)
        pub_deg.publish(deg)
        if np.linalg.norm([rout[1,0]-now_x,rout[1,1]-now_y]) < 0.2 :
            mymotor = motor_msg()
            mymotor.way = 'stop'
            pub_mot.publish(mymotor)
            while not rospy.is_shutdown():
                rospy.loginfo("finish!!")
                rospy.sleep(2)
        draw()
        rate.sleep()
    rospy.spin()
except rospy.ROSInterruptException:
        pass
