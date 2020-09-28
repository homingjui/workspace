#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from project.msg import my_msg


def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    pub = rospy.Publisher('chatter', my_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(rospy.get_param("/print_frq")) # 10hz
    count = 1
    while not rospy.is_shutdown():
        print "talk" 
        msg = my_msg()
        msg.id = count
        msg.title = "hello"
        msg.content = "hello from python"
        pub.publish(msg)
        rospy.loginfo(msg)
        count = count + 1

        #hello_str = "hello world talker %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
