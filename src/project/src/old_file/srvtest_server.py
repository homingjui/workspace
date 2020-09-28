#!/usr/bin/env python

import rospy
from project.srv import my_srv

def tell(x):
    x.id=50
    print(x)
    return "got","qaz",8787

def talker():
    rospy.init_node('taller')
    s = rospy.Service('tell_thing', my_srv, tell)
    rospy.spin()

if __name__ == "__main__":
    talker()

