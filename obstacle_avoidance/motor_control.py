from machine import Pin, PWM
import time 
import utime
import fuzzy_w_ultrasonic

Lfwd_motor = Pin(5,Pin.OUT)
Rfwd_motor = Pin(6,Pin.OUT)
Lrev_motor = Pin(7,Pin.OUT)
Rrev_motor = Pin(8,Pin.OUT)

enable1 = PWM(Pin(12)) #allows you to give analogue behaviours to digital devices
enable2 = PWM(Pin(13))

enable1.freq(1000) #PWM interval periods per second
enable2.freq(1000)

enable1.duty_u16(20000) #motor speed
enable2.duty_u16(20000) 

# Define IR sensor pins
left_sensor = Pin(9, Pin.IN)
right_sensor = Pin(10, Pin.IN)

def forward():

    Lfwd_motor.high()
    Rfwd_motor.high()
    Lrev_motor.low() 
    Rrev_motor.low()
    
def backward():

    Lfwd_motor.low()
    Rfwd_motor.low()
    Lrev_motor.high() 
    Rrev_motor.high()

def right():

    Rfwd_motor.low()
    Lfwd_motor.high()
    Lrev_motor.high() 
    Rrev_motor.low()
    
def left():
    Rfwd_motor.high()
    Lfwd_motor.low()
    Lrev_motor.high() 
    Rrev_motor.low()
   
def stop():

    Lfwd_motor.low()
    Rfwd_motor.low()
    Lrev_motor.low()
    Rrev_motor.low()


    #if the avoidance decision has a output from the ultrasonic
while True:

        #obsticale avoider
    if 0 <= fuzzy_w_ultrasonic.avoidance_decision.output < 34:
        left()
    elif 34 <= fuzzy_w_ultrasonic.avoidance_decision.output <= 66:
        forward()
    elif 67 <= fuzzy_w_ultrasonic.avoidance_decision.output <= 100:
        right()
    else:
        stop()
        
    time.sleep(0.1) 

else: 
        #line follower

    left_detected = left_sensor.value() #read IR
    right_detected = right_sensor.value()   
        
    if left_detected and not right_detected:   
        left()
    elif not left_detected and right_detected:
        right()
    elif left_detected and right_detected:
        forward()
    else:
        stop()  
