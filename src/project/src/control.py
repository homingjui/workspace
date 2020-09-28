#!/usr/bin/env python

import rospy
from project.msg import deg_msg,gps_msg,position_msg,motor_msg
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
import math
import socket
import time
import os

bridge = CvBridge()
last_x = 23.89865817
last_y = 121.5434105
now_x = 23.89865817001
now_y = 121.5434105001

direction = 0
moving = 0
passing = np.array([[last_x,last_y],[now_x,now_y]],float)
run_len = 0 
run_vec = [now_x-last_x,now_y-last_y]
next_dot = 0
next_p = np.array([0,0],float)
dots = 0

onemeter = 0.00000900900901/((111.320*math.cos((23*math.pi)/180))/110.574)

def get_movement():
    global moving,run_len,run_vec
    run_vec = [now_x-last_x, now_y-last_y]
    run_len = np.linalg.norm(run_vec)
    moving = math.atan2(now_x-last_x, now_y-last_y)

def get_dir():
    global direction,get_first_dot,next_dot,next_p,dots,last_x,last_y,run_len
    vec = np.array([path[next_dot,0]-now_x, path[next_dot,1]-now_y])
    direction = math.atan2(path[next_dot,0]-now_x, path[next_dot,1]-now_y)

    if next_dot > 0:
        rospy.loginfo(path[next_dot-1])
        rospy.loginfo(path[next_dot])
        rospy.loginfo("x "+str(now_x)+" y "+str(now_y))
        rode = path[next_dot]-path[next_dot-1]
        vec_l = ((dots+1)*(onemeter*1.5))/np.linalg.norm(rode)
        next_p =path[next_dot-1] + rode * vec_l
        if (np.linalg.norm(rode)<((dots+1)*(onemeter*1.5))):
            next_p=path[next_dot]
        direction = math.atan2(next_p[0]-now_x, next_p[1]-now_y)
        vec_nextp = np.array([next_p[0]-now_x, next_p[1]-now_y])
        if np.linalg.norm(vec_nextp) < onemeter*0.7 :
            dots += 1
    direction = moving-direction
    if  np.linalg.norm(vec) < run_len*1.25 :
        next_dot += 1
        if next_dot >= np.shape(path)[0]:
            mymotor = motor_msg()
            mymotor.way = 'stop'
            pub_mot.publish(mymotor)
            while True:
                rospy.loginfo("finish!!")
                rospy.sleep(2)
        rode = path[next_dot]-path[next_dot-1]
        rout_ang = math.atan2(rode[0],rode[1])
        direction = moving-rout_ang
        rospy.set_param("/turning",True)
        dots = 2
        last_x = 0
        last_y = 0


def get_deg(gps_data):
    global pub,now_x,now_y,direction,run_vec,last_x,last_y,passing,path,next_dot,next_p
    deg = deg_msg()
    pos = position_msg()
    if gps_data.fix_code != 4:
        rospy.loginfo("not fix")
        #last_x = 0
        #last_y = 0
        #return 0

    if rospy.get_param("/turning") == True:
        last_x = 0
        last_y = 0
        rospy.loginfo("turn")
        return 0
    #now_x = gps_data.latitude 
    #now_y = gps_data.longitude
    
    now_x += run_vec[0]*math.cos(direction)-run_vec[1]*math.sin(direction)
    now_y += run_vec[0]*math.sin(direction)+run_vec[1]*math.cos(direction)
    
    passing = np.append(passing,[[now_x,now_y]],axis=0)

    #if last_x==0 or last_y==0:
        #rospy.loginfo('first')
        #pub_deg.publish(0)
        #last_x,last_y = now_x,now_y
        #return 0
    
    #if abs(now_x-last_x)+abs(now_y-last_y) < onemeter*0.2:
        #pub_deg.publish(0)
        #rospy.loginfo('not move')
        #rospy.loginfo(str(abs(now_x-last_x)+abs(now_y-last_y)))
        #return 0

    rospy.loginfo("control")
    get_movement()
    get_dir()
    
    rospy.loginfo(str(now_x)+" "+str(now_y)+" "+str(run_len)+" "+str(moving)+" "+str(direction))
   
    #rospy.loginfo(path.reshape(-1).tolist())
    #rospy.loginfo(next_p.tolist())

    pos.path = path.reshape(-1).tolist()
    pos.now_x = now_x
    pos.now_y = now_y
    pos.next_dot = next_dot
    pos.next_p = next_p.tolist()
    pos.passing = passing.reshape(-1).tolist()
    pub_pos.publish(pos)

    last_x,last_y = now_x,now_y
    deg.deg = direction
    pub_deg.publish(deg)

get_path = 0
rospy.init_node('control')
if get_path==1:
    host = "134.208.1.101"
    port = 3400
    rospy.loginfo("connect to server")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'get_rout')
    request = s.recv(1024)
    rospy.loginfo(request)
    s.close()

    path = np.array([])
    request = np.array(request.split(';'))
    for i in request:
        path = np.append(path,float(np.array(i.split(','))[0]))
        path = np.append(path,float(np.array(i.split(','))[1]))
    path = path.reshape((-1,2))
    rospy.loginfo(path)

else:
    f = open('/home/isp/Desktop/workspace/src/project/src/rout5.txt', 'r')
    x = np.array(f.read().split('\n'))[:-1]
    f.close()

    path = np.array([ i.split(' ') for i in x],float)
    path = path.reshape((-1,2))
    rospy.loginfo(path)

try:
    pub_deg = rospy.Publisher('revise_deg', deg_msg, queue_size=10)
    pub_pos = rospy.Publisher('position', position_msg, queue_size=10)
    pub_mot = rospy.Publisher('auto_motion', motor_msg, queue_size=10)
    rospy.Subscriber('gps', gps_msg, get_deg)
    rospy.spin()
    
    
except KeyboardInterrupt:
    cv2.destroyAllWindows()

