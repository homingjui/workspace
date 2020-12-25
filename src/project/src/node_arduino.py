#!/usr/bin/python3

import rospy
from project.msg import arduino_msg
from project.msg import motor_msg
import numpy as np
import smbus2

bus = smbus2.SMBus(1)

address = 0x04
readn = 0

motion = {'back':False,'front':False,'left':False,'right':False,'stop':False}

offset = rospy.get_param("/offset")

persent = 0
speed = 0


def motor(motor):
    global motion,persent,speed
    motion[motor.way]=True
    persent = motor.persent
    speed = motor.speed
    #rospy.loginfo(motor)

def writeNumber(value):
    r.sleep()
    
    bus.write_byte(address, int(value))
    
    return -1

def readNumber():    
    return bus.read_byte(address)

pub = rospy.Publisher('arduino', arduino_msg, queue_size=10)
rospy.init_node('node_arduino')
r = rospy.Rate(120)
arduino = arduino_msg()
check = [0,0]

rospy.Subscriber('auto_motion', motor_msg, motor)

try:
    while not rospy.is_shutdown():
        
        if readn == 0:
            check[0] = readNumber()
        elif readn == 1:
            check[1] = readNumber()
        elif readn == 2:
            arduino.voltage = readNumber()
        elif readn == 3:
            arduino.gyroX = (float(readNumber())/255)*360
        elif readn == 4:
            arduino.gyroY = (float(readNumber())/255)*360
        elif readn == 5:
            arduino.gyroZ =(float(readNumber())/255)*360
        elif readn == 6:
            arduino.accX = (float(readNumber())/255)*360
        elif readn == 7:
            arduino.accY = (float(readNumber())/255)*360
        elif readn == 8:
            arduino.accZ = (float(readNumber())/255)*360
        elif readn == 9:
            arduino.roll = (float(readNumber())/255)*360
        elif readn == 10:
            arduino.pitch = (float(readNumber())/255)*360
        elif readn == 11:
            arduino.yaw = (float(readNumber())/255)*360

        readn += 1
        #rospy.loginfo(readn)
        if readn >= 12:
            readn = 0
            if not check==[0,255]:
                r.sleep()
                readNumber()
                rospy.loginfo("arduino setting")
                continue
            #rospy.loginfo("arduino set ok")
            pub.publish(arduino)
        else:
            r.sleep()
            continue
        #rospy.loginfo(motion)
        if motion['back']:
            persentvalu = int((255-speed)*persent)
            writeNumber("01")
            duty = max(0,min(speed+offset+persentvalu,255))
            #rospy.loginfo(persentvalu)
            writeNumber(duty)
            writeNumber("10")
            duty = max(0,min(speed-offset-persentvalu,255))
            writeNumber(duty)
            motion['back']=False
        elif motion['front']:
            #rospy.loginfo('front')
            persentvalu = int((255-speed)*persent)
            writeNumber("10")
            duty = max(0,min(speed+offset+persentvalu,255))
            writeNumber(duty)
            writeNumber("01")
            duty = max(0,min(speed-offset-persentvalu,255))
            writeNumber(duty)
            motion['front']=False
        elif motion['left']:
            writeNumber("10")
            writeNumber(speed)
            writeNumber("10")
            writeNumber(speed)
            motion['left']=False
        elif motion['right']:
            writeNumber("01")
            writeNumber(speed)
            writeNumber("01")
            writeNumber(speed)
            motion['right']=False
        elif motion['stop']:
            #rospy.loginfo("stop motor");
            writeNumber("00")
            writeNumber("0")
            writeNumber("00")
            writeNumber("0")
            motion['stop']=False

        r.sleep()

except rospy.ROSInterruptException:
    writeNumber("00")
    writeNumber("0")
    writeNumber("00")
    writeNumber("0")
    ser.close()
