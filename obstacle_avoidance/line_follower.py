from machine import Pin
from obstacle_avoidance import motion_control as mc

left_sensor = Pin(9, Pin.IN)
right_sensor = Pin(10, Pin.IN)

left_detected = left_sensor.value() #read IR
right_detected = right_sensor.value()   
        
if left_detected and not right_detected:   
    mc.left()
elif not left_detected and right_detected:
    mc.right()
elif left_detected and right_detected:
    mc.forward()
else:
    mc.stop()  