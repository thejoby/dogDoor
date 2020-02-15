from flask import Flask

#from Tkinter import *
import time
from RPIO import PWM
import sys


app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask app is running!'


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


@app.route('/open')
def open():
    servo = PWM.Servo()
    servo.set_servo(18, 1800)
    time.sleep(2)
    servo.stop_servo(18)


@app.route('/close')
def close():
    servo = PWM.Servo()
    servo.set_servo(18, 810)
    time.sleep(1.5)
    servo.stop_servo(18)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
