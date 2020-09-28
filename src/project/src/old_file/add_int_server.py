#!/usr/bin/env python

from rospy_tutorials.srv import *
import rospy

def adder(req):
    print "adder: %s + %s = %s"%(req.a, req.b, req.a+req.b)
    return AddTwoIntsResponse(req.a+req.b)

def add_server():
    rospy.init_node('add_server')
    s = rospy.Service('add_two_ints', AddTwoInts, adder)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_server()
