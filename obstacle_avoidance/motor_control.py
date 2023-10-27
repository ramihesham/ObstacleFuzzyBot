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
