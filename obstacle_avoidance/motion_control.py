from machine import Pin,PWM
import time
import utime


ENA = PWM(Pin(4)) #The main control on IN1 and IN2
IN1 = Pin(5,Pin.OUT)
IN2 = Pin(6,Pin.OUT)
IN3 = Pin(7,Pin.OUT)
IN4 = Pin(8,Pin.OUT)
ENB = PWM(Pin(9)) #The main control on IN3 and IN4

ENA.freq(1000) #PWM interval periods per second
ENB.freq(1000)

speed = 30000 #the speed of the robot
 
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
