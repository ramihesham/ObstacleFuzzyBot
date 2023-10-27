from machine import Pin,PWM
from obstacle_avoidance import motion_control as mc
from obstacle_avoidance import fuzzy_logic as fz

if 0 <= fz.avoidance_decision.output < 34:
    mc.left()
elif 34 <= fz.avoidance_decision.output <= 66:
    mc.forward()
elif 67 <= fz.avoidance_decision.output <= 100:
    mc.right()
else:
    mc.stop()
        