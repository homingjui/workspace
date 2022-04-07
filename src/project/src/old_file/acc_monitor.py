#!/usr/bin/env python3

#import matplotlib.pyplot as plt

import rospy
from project.msg import gyro_msg
import smbus
import time
class Gyro(object):
    def __init__(self, addr):
        self.addr = addr
        self.i2c = smbus.SMBus(0)





    def get_acc(self):
        try:
            self.raw_acc_x = self.i2c.read_i2c_block_data(self.addr, 0x34, 2)
            self.raw_acc_y = self.i2c.read_i2c_block_data(self.addr, 0x35, 2)
            self.raw_acc_z = self.i2c.read_i2c_block_data(self.addr, 0x36, 2)
        except IOError:
            print("ReadError: gyro_acc")
            return (0, 0, 0)
        else:
            self.k_acc = 16 

            self.acc_x = float(self.raw_acc_x[1] << 8 | self.raw_acc_x[0]) / 32768 * self.k_acc
            self.acc_y = float(self.raw_acc_y[1] << 8 | self.raw_acc_y[0]) / 32768 * self.k_acc
            self.acc_z = float(self.raw_acc_z[1] << 8 | self.raw_acc_z[0]) / 32768 * self.k_acc
            #print(float(self.raw_acc_x[1] << 8 | self.raw_acc_x[0])/ 32768 * self.k_acc)
            if self.acc_x >= self.k_acc:
                self.acc_x -= 2 * self.k_acc

            if self.acc_y >= self.k_acc:
               self.acc_y -= 2 * self.k_acc

            if self.acc_z >= self.k_acc:
                self.acc_z -= 2 * self.k_acc
            return (self.acc_x, self.acc_y, self.acc_z)
    def get_gyro(self):
        try:
            self.raw_gyro_x = self.i2c.read_i2c_block_data(self.addr, 0x37, 2)
            self.raw_gyro_y = self.i2c.read_i2c_block_data(self.addr, 0x38, 2)
            self.raw_gyro_z = self.i2c.read_i2c_block_data(self.addr, 0x39, 2)
        except IOError:
            print("ReadError: gyro_gyro")
            return (0, 0, 0)
        else:
            self.k_gyro = 2000
            self.gyro_x = float(self.raw_gyro_x[1] << 8 | self.raw_gyro_x[0]) / 32768 * self.k_gyro
            self.gyro_y = float(self.raw_gyro_y[1] << 8 | self.raw_gyro_y[0]) / 32768 * self.k_gyro
            self.gyro_z = float(self.raw_gyro_z[1] << 8 | self.raw_gyro_z[0]) / 32768 * self.k_gyro

            if self.gyro_x >= self.k_gyro:
                self.gyro_x -= 2 * self.k_gyro

            if self.gyro_y >= self.k_gyro:
                self.gyro_y -= 2 * self.k_gyro

            if self.gyro_z >= self.k_gyro:
                self.gyro_z -= 2 * self.k_gyro

            return (self.gyro_x, self.gyro_y, self.gyro_z)


    def get_angle(self):
        try:
            self.raw_angle_x = self.i2c.read_i2c_block_data(self.addr, 0x3d, 2)
            self.raw_angle_y = self.i2c.read_i2c_block_data(self.addr, 0x3e, 2)
            self.raw_angle_z = self.i2c.read_i2c_block_data(self.addr, 0x3f, 2)
        except IOError:
            print("ReadError: gyro_angle")
            return (0, 0, 0)
        else:
            self.k_angle = 180
            self.angle_x = float(self.raw_angle_x[1] << 8 | self.raw_angle_x[0]) / 32768 * self.k_angle
            self.angle_y = float(self.raw_angle_y[1] << 8 | self.raw_angle_y[0]) / 32768 * self.k_angle
            self.angle_z = float(self.raw_angle_z[1] << 8 | self.raw_angle_z[0]) / 32768 * self.k_angle
            if self.angle_x >= self.k_angle:
                self.angle_x -= 2 * self.k_angle

            if self.angle_y >= self.k_angle:
                self.angle_y -= 2 * self.k_angle

            if self.angle_z >= self.k_angle:
                self.angle_z -= 2 * self.k_angle
            return (self.angle_x, self.angle_y, self.angle_z)

    #def LED_OFF(self):
        smbus.SMBus(1).write_word_data(self.addr,0x1b,0x00)
        

def talker():
    head_gyro = Gyro(0x50)
    pub = rospy.Publisher('acc', gyro_msg, queue_size=10)
    rospy.init_node('acc_monitor')
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        gyro_data = gyro_msg()
        gyro_data.acc_x = head_gyro.get_acc()[0]
        gyro_data.acc_y = head_gyro.get_acc()[1]
        gyro_data.acc_z = head_gyro.get_acc()[2]
        
        gyro_data.gyro_x = head_gyro.get_gyro()[0]
        gyro_data.gyro_y = head_gyro.get_gyro()[1]
        gyro_data.gyro_z = head_gyro.get_gyro()[2]


        gyro_data.angle_x = head_gyro.get_angle()[0]
        gyro_data.angle_y = head_gyro.get_angle()[1]
        gyro_data.angle_z = head_gyro.get_angle()[2]
        #data = 0x01
    #    head_gyro.LED_OFF()   
        #print('gyro =' ,gyro_data.gyro_x,gyro_data.gyro_y,gyro_data.gyro_z)

        
        #head_gyro.get_acc()
        #head_gyro.get_gyro()
        #head_gyro.get_angle()

        pub.publish(gyro_data)
        rate.sleep()
 


#ef RATE():
#   data_rate = 0x0c
#   smbus.SMBus(1).write_word_data(0x50,0x03,data_rate)


#def read():

 #   b = smbus.SMBus(1).read_byte_data(0x50 , 0x00)
  #  print(b)

#def SAVE():
#    smbus.SMBus(1).write_word_data(0x50,0x00,0x00)

if __name__ == '__main__':

    try:

 #      RATE()
 #       SAVE()
 #       read()
        talker()
    except rospy.ROSInterruptException:
        pass

