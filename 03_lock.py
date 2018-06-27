#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

#### GPIO setup ####

GPIO.setup(26, GPIO.output) # Red led
GPIO.setup(20, GPIO.output) # Green LED
GPIO.setup(18, GPIO.output) # PWM pin for servo
GPIO.setup(21, GPIO.output) # Buzzer
pwm = GPIO.PWM(18, 50)
pwm.start(5) ##### FINISH PWM SETUP

Buzzer.on = GPIO.output(21, GPIO.HIGH)
Buzzer.off = GPIO.output(21, GPIO.LOW)
GLED.on = GPIO.output(20, GPIO.HIGH)
GLED.off = GPIO.output(20, GPIO.LOW)
RLED.on = GPIO.output(26, GPIO.HIGH)
RLED.off =  GPIO.output(26, GPIO.LOW)
mode = 'LISTEN'
allowed_tags = []

def handle_listen_mode():
    global mode, allowed_tags
    
    id = reader.read_id_no_block()
    if id:
        if id in allowed_tags:
            unlock_door()
        else:
            print("Unknown Tag")
            flash(RED, 5, 0.1)

        
        
def unlock_door():
    print("Door UNLOCKED")
    flash(GREEN, 10, 0.5)
    print("Door LOCKED")
    


try:
    while True:
        if mode == "LISTEN":
            handle_listen_mode()
        elif mode == "GRANT":
            handle_grant_mode()

finally:
    print("cleaning up")
    GPIO.cleanup()
