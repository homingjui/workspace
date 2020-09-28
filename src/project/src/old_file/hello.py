#!/usr/bin/env python

import rospy

rospy.init_node('hello_python_node')

while not rospy.is_shutdown():
    rospy.loginfo('Hello World by python')
    rospy.sleep(2)
