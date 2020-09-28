#!/usr/bin/env python


import time
import rospy
from project.msg import gyro
from std_msgs.msg import float32

def get_gyro_data():
    acc = gyro()
    acc.acc_x = gyro.acc_x
    acc.acc_y = gyro.acc_y
    acc.acc_z = gyro.acc_z

    acc.gyro_x = gyro.gyro_x
    acc.gyro_y = gyro.gyro_y
    acc.gyro_z = gyro.gyro_z

    acc.angle_x = gyro.angle_x
    acc.angle_y = gyro.angle_y
    acc.angle_z = gyro.angle_z
    
    print("acc: ",acc.acc_x)
   
    

    

def listener():
    rospy.init_node("gyro_reader")
    rospy.Subscriber("ACCGYRO",gyro,get_gyro_data)
    rospy.spin()



while(1):
    listener()
         
 
# print("acc:" + acc.acc_x,"  ",acc.acc_y,"   ",acc.acc_z)
    time.sleep(0.2)
