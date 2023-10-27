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