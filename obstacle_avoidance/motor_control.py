from machine import Pin,PWM
import time 
#import fuzzy_w_ultrasonic

ENA = PWM(Pin(4)) #The main control on IN1 and IN2
IN1 = Pin(5,Pin.OUT)
IN2 = Pin(6,Pin.OUT)
IN3 = Pin(7,Pin.OUT)
IN4 = Pin(8,Pin.OUT)
ENB = PWM(Pin(9)) #The main control on IN3 and IN4

ENA.freq(1000) #PWM interval periods per second
ENB.freq(1000)

speed = 30000 #the speed of the robot
 
#enable1.duty_u16(20000) #motor speed
#enable2.duty_u16(20000) 

# Define IR sensor pins
#left_sensor = Pin(9, Pin.IN)
#right_sensor = Pin(10, Pin.IN)

def forward():
    ENA.duty_u16(speed)
    IN1.value(0)
    IN1.value(1)
    ENB.duty_u16(speed)
    IN1.value(1) 
    IN1.value(0)
    
def backward():
    ENA.duty_u16(speed)
    IN1.value(1)
    IN1.value(0)
    ENB.duty_u16(speed)
    IN1.value(0) 
    IN1.value(1)

def right():
    ENA.duty_u16(speed)
    IN1.value(0)
    IN1.value(1)
    ENB.duty_u16(speed)
    IN1.value(0) 
    IN1.value(1)
    
def left():
    ENA.duty_u16(speed)
    IN1.value(1)
    IN1.value(0)
    ENB.duty_u16(speed)
    IN1.value(1) 
    IN1.value(0)
   
def stop():
    ENA.duty_u16(0)
    IN1.value(0)
    IN1.value(0)
    ENB.duty_u16(0)
    IN1.value(0) 
    IN1.value(0)


    #if the avoidance decision has a output from the ultrasonic
#while True:

        #obsticale avoider
#    if 0 <= fuzzy_w_ultrasonic.avoidance_decision.output < 34:
 #       left()
  #  elif 34 <= fuzzy_w_ultrasonic.avoidance_decision.output <= 66:
   #     forward()
    #elif 67 <= fuzzy_w_ultrasonic.avoidance_decision.output <= 100:
     #   right()
    #else:
     #   stop()
        
    #time.sleep(0.1) 

#else: 
        #line follower

 #   left_detected = left_sensor.value() #read IR
  #  right_detected = right_sensor.value()   
        
   # if left_detected and not right_detected:   
    #    left()
    #elif not left_detected and right_detected:
     #   right()
    #elif left_detected and right_detected:
     #   forward()
    #else:
     #   stop()  



####---------------------------------------Kalman filter--------------------------------------------------------####

import RPi.GPIO as GPIO
import time
import numpy as np

# 2 ultrasonic sensor
TRIG1 = 2
ECHO1 = 3
TRIG2 = 4
ECHO2 = 5

# pins setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

# KF parameters
initial_state = 0.0
initial_estimate_error = 1.0
process_noise = 0.01
measurement_noise = 0.1

# Initialize KF variables
state_estimate = initial_state
estimate_error = initial_estimate_error

def read_ultrasonic_sensor(trigger_pin, echo_pin):
    # Send a trigger signal
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    # Wait echo signal
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # The distance
    distance = pulse_duration * 17150

    return distance

# KF loop
try:
    while True:
        distance1 = read_ultrasonic_sensor(TRIG1, ECHO1)
        distance2 = read_ultrasonic_sensor(TRIG2, ECHO2)

        # Average of the two sensros
        measurement = (distance1 + distance2) / 2

        # Prediction (uncertainty)
        predicted_state = state_estimate
        predicted_estimate_error = estimate_error + process_noise

        # Update step
        kalman_gain = predicted_estimate_error / (predicted_estimate_error + measurement_noise)
        state_estimate = predicted_state + kalman_gain * (measurement - predicted_state)
        estimate_error = (1 - kalman_gain) * predicted_estimate_error

        # Obstacle detection and avoidance logic 
        if state_estimate < 10.0:  # Adjust the threshold for your specific needs
            print("Obstacle detected. Take evasive action.")

        time.sleep(0.1)  

except KeyboardInterrupt:
    GPIO.cleanup()

