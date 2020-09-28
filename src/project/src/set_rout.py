#!/usr/bin/env python

import os
import rospy
from project.msg import gps_msg


def setting(gps_data):
    if gps_data.fix_code != 4:
        rospy.loginfo("not fix")
    else:
        rospy.loginfo(os.getcwd()+'/rout5.txt')
        f = open(os.getcwd()+'/rout5.txt','a')
        f.write(str(gps_data.latitude)+" "+str(gps_data.longitude)+"\n")
        f.close()
        rospy.loginfo("set done\n"+str(gps_data.latitude)+" "+str(gps_data.longitude)+"\n")
        rospy.signal_shutdown("gps set done")

rospy.init_node('set_rout')
rospy.Subscriber('gps', gps_msg, setting)

rospy.spin()
