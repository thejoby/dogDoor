from flask import Flask

import time
import datetime
import RPi.GPIO as GPIO
import sys


app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    return 'Flask app is running at: %s' % (now)


@app.route('/open', methods=['GET','POST'])
def open():
    if request.method == 'GET':
        return "POST to this endpoint instead"
    if request.method == 'POST':
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        p = GPIO.PWM(18, 100)
        p.start(17.5)

        time.sleep(1.2)

        p.stop()
        GPIO.cleanup()
        return 'Dog Door Open!'


@app.route('/close', methods=['GET','POST'])
def close():
    if request.method == 'GET':
        return "POST to this endpoint instead"
    if request.method == 'POST':
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        #GPIO.PWM(PIN, frequency in Hz)
        p = GPIO.PWM(18, 100)
        #p.start(duty_cycle)
        #The duty cycle describes the proportion of on time 
        # to the regular interval or period of time.
        p.start(7)
        
        time.sleep(1)
        p.stop()
        GPIO.cleanup()
        return 'Dog Door Closed!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
