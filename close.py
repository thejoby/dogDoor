from Tkinter import *
import time
from RPIO import PWM
import sys

servo = PWM.Servo()

servo.set_servo(18, 810)

time.sleep(1.5)

servo.stop_servo(18)