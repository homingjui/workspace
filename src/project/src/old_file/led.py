import Jetson.GPIO as GPIO
import time as time

LED_Pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_Pin, GPIO.OUT)

for i in range(2):
    GPIO.output(LED_Pin, GPIO.HIGH)
    print "on"
    time.sleep(1)
    GPIO.output(LED_Pin, GPIO.LOW)
    print "off"
    time.sleep(1)

GPIO.cleanup()

