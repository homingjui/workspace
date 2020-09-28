#!/usr/bin/env python

import rospy
from motor import motor
from std_msgs.msg import String
from project.msg import joystick_msg

stop = True

def set_motor(joystick_data):
    global mymotor
    global stop
    speed = 100
    if joystick_data.leftTrg == 1:
        speed = 150
    elif joystick_data.rightTrg == 1:
        speed = 50
    persent = 0
    if joystick_data.B ==1:
        persent = 0.5
    elif joystick_data.X ==1:
        persent = -0.5
    
    if joystick_data.leftY == 1:
        mymotor.front(speed,persent)
        stop = False
    elif joystick_data.leftY == -1:
        mymotor.back(speed,persent)
        stop = False
    elif joystick_data.leftX == -1:
        mymotor.left()
        stop = False
    elif joystick_data.leftX == 1:
        mymotor.right()
        stop = False
    else:
        if not(stop):
            mymotor.stop()
            stop = True


mymotor = motor()
rospy.init_node('now_motion')
rospy.Subscriber('joystick_status', joystick_msg, set_motor)
    
rospy.spin()
mymotor.stop()
