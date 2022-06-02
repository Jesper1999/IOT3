import sys
import RPi.GPIO as GPIO
import time

signalPIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(signalPIN,GPIO.OUT)

def set_buzzer():
    GPIO.output(signalPIN,0)
    time.sleep(0.1)

    GPIO.output(signalPIN,1)
    time.sleep(0.1)

    GPIO.cleanup()
    sys.exit()


