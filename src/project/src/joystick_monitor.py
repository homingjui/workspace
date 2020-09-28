#!/usr/bin/env python

import rospy
from project.msg import joystick_msg
import xbox

joy = xbox.Joystick()

def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    pub = rospy.Publisher('joystick_status', joystick_msg, queue_size=10)
    rospy.init_node('joystick_monitor')
    rate = rospy.Rate(rospy.get_param("/joystick_frq")) # 10hz
    count = 1
    while not rospy.is_shutdown():
        joystick = joystick_msg()
        joystick.connect = joy.connected()==1
        joystick.leftX = joy.leftX()
        joystick.leftY = joy.leftY()

        joystick.rightX = joy.rightX()
        joystick.rightY = joy.rightY()

        joystick.leftTrg = joy.leftTrigger()
        joystick.rightTrg = joy.rightTrigger()
        
        joystick.A = joy.A() == 1
        joystick.B = joy.B() == 1
        joystick.X = joy.X() == 1
        joystick.Y = joy.Y() == 1

        joystick.padUp = joy.dpadUp() == 1
        joystick.padDown = joy.dpadDown() == 1
        joystick.padLeft = joy.dpadLeft() == 1
        joystick.padRight = joy.dpadRight() == 1

        joystick.bumperLeft = joy.leftBumper() == 1
        joystick.bumperRight = joy.rightBumper() == 1

        joystick.guide = joy.Guide() == 1

        pub.publish(joystick)
        #rospy.loginfo(joystick)
        count = count + 1

        #hello_str = "hello world talker %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        rate.sleep()
    joy.close() 

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
