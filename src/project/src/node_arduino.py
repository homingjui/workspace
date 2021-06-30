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


#offset = rospy.get_param("/offset")
offset = 100


persent = 0
speed = 0


def motor(motor):
    global motion,persent,speed
    motion[motor.way]=True
    persent = motor.persent
    speed = motor.speed
    #rospy.loginfo(motor)

def writeNumber(value):
#    r.sleep()
#    rospy.loginfo(value)
#    bus.write_byte(address, int(0))
    return -1
#def writeNumbers(value):
#    data = [1, 2, 3, 4, 5, 6, 7, 8]
#    bus.write_i2c_block_data(address, 0, data)
#    return -1

def readNumber():
    azx = bus.read_byte(address)
    print(azx)
    return azx

def readNumbers():    
    return bus.read_i2c_block_data(address,0,20)

pub = rospy.Publisher('arduino', arduino_msg, queue_size=10)
rospy.init_node('node_arduino')
r = rospy.Rate(10)
arduino = arduino_msg()
check = [0,0]

rospy.Subscriber('auto_motion', motor_msg, motor)

try:
    while not rospy.is_shutdown():
        read = readNumbers()
        #rospy.loginfo(read)
        arduino.gyroX = (float(read[2])*256+read[3])
        arduino.gyroY = (float(read[4])*256+read[5])
        arduino.gyroZ = (float(read[6])*256+read[7])
        arduino.accX = (float(read[8])*256+read[9])
        arduino.accY = (float(read[10])*256+read[11])
        arduino.accZ = (float(read[12])*256+read[13])
        arduino.roll = (float(read[14])*256+read[15]-32768)/(32768/180)
        arduino.pitch = (float(read[16])*256+read[17]-32768)/(32768/180)
        arduino.yaw = (float(read[18])*256+read[19]-32768)/(32768/180)
        pub.publish(arduino)
        
        #rospy.loginfo("motion")
        if motion['back']:
            persentvalu = int((255-speed)*persent)
            #writeNumber("01")
            duty1 = max(0,min(speed+offset+persentvalu,255))
            #writeNumber(duty)
            #writeNumber("10")
            duty2 = max(0,min(speed-offset-persentvalu,255))
            #writeNumber(duty)
            motion['back']=False
            data = [1, 10, duty1, duty2]
            bus.write_i2c_block_data(address, 0, data)
        elif motion['front']:
            #rospy.loginfo('front')
            persentvalu = int((255-speed)*persent)
            #writeNumber("10")
            duty1 = max(0,min(speed+offset+persentvalu,255))
            #writeNumber(duty)
            #writeNumber("01")
            duty2 = max(0,min(speed-offset-persentvalu,255))
            #writeNumber(duty)
            motion['front']=False
            data = [10, 1, duty1, duty2]
            bus.write_i2c_block_data(address, 0, data)
        elif motion['left']:
            #writeNumber("10")
            #writeNumber(speed)
            #writeNumber("10")
            #writeNumber(speed)
            motion['left']=False
            data = [10, 10, speed, speed]
            bus.write_i2c_block_data(address, 0, data)
        elif motion['right']:
            #writeNumber("01")
            #writeNumber(speed)
            #writeNumber("01")
            #writeNumber(speed)
            motion['right']=False
            data = [1, 1, speed, speed]
            bus.write_i2c_block_data(address, 0, data)
        elif motion['stop']:
            #rospy.loginfo("stop motor");
            #writeNumber("00")
            #writeNumber("0")
            #writeNumber("00")
            #writeNumber("0")
            motion['stop']=False
            data = [0, 0, 0, 0]
            bus.write_i2c_block_data(address, 0, data)
        r.sleep()

except rospy.ROSInterruptException:
    #writeNumber("00")
    #writeNumber("0")
    #writeNumber("00")
    #writeNumber("0")
    data = [0, 0, 0, 0]
    bus.write_i2c_block_data(address, 0, data)
    ser.close()
