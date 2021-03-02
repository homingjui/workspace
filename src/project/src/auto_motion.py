#!/usr/bin/env python3

import rospy
from project.msg import deg_msg
from project.msg import arduino_msg
from project.msg import motor_msg
from tf2_msgs.msg import TFMessage
from scipy.spatial.transform import Rotation
import math

the_acc = 0
turn_speed = 125

def update_pos(data):
    tf = data.transforms[0]
    tfx = tf.transform.rotation.x
    tfy = tf.transform.rotation.y
    tfz = tf.transform.rotation.z
    tfw = tf.transform.rotation.w
    rot = Rotation.from_quat([tfx, tfy, tfz, tfw])
    xyz = rot.as_euler('xyz')
    global the_acc
    the_acc = (xyz[2]/math.pi)*180
    

def update_acc(acc):
    global the_acc
    the_acc = acc.yaw

def set_motor(deg):
    global mymotor,the_acc
    if not rospy.get_param("/turning"):
        per = (deg.deg*(-3)) / math.pi
        rospy.loginfo("run"+str(per))
        mymotor.way = 'front'
        mymotor.speed = 100
        mymotor.persent = per
        pub.publish(mymotor)
    else:
        rospy.loginfo(deg.deg)
        my_turn = (deg.deg/math.pi)*180
        if my_turn >180:
            my_turn = -360 + my_turn
        if my_turn < -180:
            my_turn =  360 + my_turn

        rospy.loginfo("turn"+str(my_turn))

        if my_turn < 0:
            mymotor.way = 'left'
            mymotor.speed = turn_speed
            mymotor.persent = 0
        else:
            mymotor.way = 'right'
            mymotor.speed = turn_speed
            mymotor.persent = 0
        pub.publish(mymotor)

        now_acc = the_acc
        rospy.loginfo("???"+str(now_acc)+" "+str(the_acc)+" "+str(my_turn))
        if my_turn > 0 and now_acc < abs(my_turn):
            while  the_acc <= abs(my_turn) :
                rospy.loginfo("a"+str(the_acc)+" "+str(my_turn))
                continue
            my_turn = abs(my_turn)-now_acc
            now_acc = 360
            rospy.loginfo(">0!!!!")
        
        elif my_turn < 0 and 360-now_acc < abs(my_turn):
            while  360-the_acc < abs(my_turn) :
                rospy.loginfo("b"+str(360-the_acc)+" "+str(my_turn))
                continue
            my_turn = abs(my_turn) - (360-now_acc)
            now_acc = 0
            rospy.loginfo("<0!!!")

        rospy.loginfo("???"+str(now_acc)+" "+str(the_acc)+" "+str(my_turn))
        while(abs(now_acc-the_acc) < abs(my_turn*0.7) ):
            rospy.loginfo("!!!!"+str(now_acc)+" "+str(the_acc)+" "+str(abs(my_turn)))
            if rospy.is_shutdown():
                break
            continue
            pass

        rospy.loginfo(the_acc)
        mymotor.way = 'stop'
        mymotor.speed = 0
        mymotor.persent = 0
        pub.publish(mymotor)
        rospy.sleep(1)
 
        rospy.set_param("/turning",False)

mymotor = motor_msg()
rospy.init_node('auto_motion')
rospy.Subscriber('revise_deg', deg_msg, set_motor)
#rospy.Subscriber('arduino', arduino_msg, update_acc)
rospy.Subscriber('/tf',TFMessage,update_pos)
pub = rospy.Publisher('auto_motion', motor_msg, queue_size=10)    
rospy.spin()
#mymotor.stop()
