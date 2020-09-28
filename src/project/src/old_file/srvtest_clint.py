#!/usr/bin/env python

import sys
import rospy
from project.srv import my_srv

def tell_thing_clint(x):
    rospy.wait_for_service('tell_thing')
    teller = rospy.ServiceProxy('tell_thing', my_srv)
    resp1 = teller(x)
    print resp1

if __name__ == "__main__":
    tell_thing_clint(5)

