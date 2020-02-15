from flask import Flask

#from Tkinter import *
import time
import datetime
#from RPIO import PWM
import RPi.GPIO as GPIO
import sys


app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    return 'Flask app is running at: %s' % (now)


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


@app.route('/open')
def open():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    p = GPIO.PWM(18, 50)
    p.start(4)

    #servo = PWM.Servo()
    #servo.set_servo(18, 1800)
    time.sleep(2)
    #servo.stop_servo(18)
    p.stop()
    GPIO.cleanup()
    return 'Dog Door Open!'


@app.route('/close')
def close():
    #servo = PWM.Servo()
    #servo.set_servo(18, 810)
    #time.sleep(1.5)
    #servo.stop_servo(18)

    #https://rpi.science.uoit.ca/lab/servo/
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    #GPIO.PWM(PIN, frequency in Hz)
    p = GPIO.PWM(18, 50)
    #p.start(duty_cycle)
    #The duty cycle describes the proportion of on time 
    # to the regular interval or period of time.
    p.start(10)
    time.sleep(2)
    p.stop()
    GPIO.cleanup()
    return 'Dog Door Closed!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
