from Tkinter import *
import time
from RPIO import PWM
import sys

servo = PWM.Servo()

servo.set_servo(18, 1800)

time.sleep(2)

servo.stop_servo(18)