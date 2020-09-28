#!/usr/bin/env python

import RPi.GPIO as GPIO
import smbus
import time
import rospy

bus = smbus.SMBus(1)

address = 0x04
offset = rospy.get_param("/offset")

def writeNumber(value):
    #bus.write_byte(address, value)
    #rospy.sleep(0.5)
    return -1

def readNumber():
    #number = bus.read_byte(address)
    return number

class motor:
    
    def __init__(self):
        rospy.loginfo("init motor");

    def back(self,speed,persent):
        persentvalu = int((255-speed)*persent)
        writeNumber(01)
        duty = max(0,min(speed+offset+persentvalu,255))
        #rospy.loginfo(persentvalu)
        writeNumber(duty)
        writeNumber(10)
        duty = max(0,min(speed-offset-persentvalu,255))
        writeNumber(duty)

    def front(self,speed,persent):
        persentvalu = int((255-speed)*persent)
        writeNumber(10)
        duty = max(0,min(speed+offset+persentvalu,255))
        writeNumber(duty)
        writeNumber(01)
        duty = max(0,min(speed-offset-persentvalu,255))
        writeNumber(duty)

    def left(self,speed):
        writeNumber(10)
        writeNumber(speed)
        writeNumber(10)
        writeNumber(speed)
    def right(self,speed):
        writeNumber(01)
        writeNumber(speed)
        writeNumber(01)
        writeNumber(speed)
    def stop(self):
        #rospy.loginfo("stop motor");
        writeNumber(00)
        writeNumber(0)
        writeNumber(00)
        writeNumber(0)
