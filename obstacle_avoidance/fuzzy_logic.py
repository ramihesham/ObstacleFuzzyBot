from machine import Pin, utime_pulse_us
import numpy as np
import skfuzzy.control as ctrl
import skfuzzy as fuzz
import utime
from obstacle_avoidance import ultrasonic as us

# Define linguistic variables
right_sensor = ctrl.Antecedent(np.arange(2, 400, 50), 'right_sensor_reading')
left_sensor = ctrl.Antecedent(np.arange(2, 400, 50), 'left_sensor_reading')
front_sensor = ctrl.Antecedent(np.arange(2, 400, 50), 'front_sensor_reading')
left_motor = ctrl.Consequent(np.arange(-200, 200, 50), 'left_motor_RPM')
right_motor = ctrl.Consequent(np.arange(-200, 200, 50), 'right_motor_RPM')

# Membership functions for right_sensor
right_sensor['near'] = fuzz.trapmf(right_sensor_reading.universe, [2, 2, 50, 150])
right_sensor['medium'] = fuzz.trimf(right_sensor_reading.universe, [100, 200, 300])
right_sensor['far'] = fuzz.trapmf(right_sensor_reading.universe, [250, 350, 400, 400])

# Membership functions for left_sensor
left_sensor['near'] = fuzz.trapmf(left_sensor_reading.universe, [2, 2, 50, 150])
left_sensor['medium'] = fuzz.trimf(left_sensor_reading.universe, [100, 200, 300])
left_sensor['far'] = fuzz.trapmf(left_sensor_reading.universe, [250, 350, 400, 400])

# Membership functions for front_sensor
front_sensor['near'] = fuzz.trapmf(front_sensor_reading.universe, [2, 2, 50, 150])
front_sensor['medium'] = fuzz.trimf(front_sensor_reading.universe, [100, 200, 300])
front_sensor['far'] = fuzz.trapmf(front_sensor_reading.universe, [250, 350, 400, 400])

# Membership functions for left_motor
left_motor['-ve_fast'] = fuzz.trapmf(left_motor_RPM.universe, [-200, -200, 45, 90])
left_motor['zero'] = fuzz.trimf(left_motor_RPM.universe, [-90, 0, 90])
left_motor['+ve_slow'] = fuzz.trapmf(left_motor_RPM.universe, [76.4, 76.4, 104, 159])
left_motor['+ve_fast'] = fuzz.trapmf(left_motor_RPM.universe, [117.5, 172.5, 200, 200])

# Membership functions for right_motor
right_motor['-ve_fast'] = fuzz.trapmf(right_motor_RPM.universe, [-200, -200, 45, 90])
right_motor['zero'] = fuzz.trimf(right_motor_RPM.universe, [-90, 0, 90])
right_motor['+ve_slow'] = fuzz.trapmf(right_motor_RPM.universe, [76.4, 76.4, 104, 159])
right_motor['+ve_fast'] = fuzz.trapmf(right_motor_RPM.universe, [117.5, 172.5, 200, 200])

# Fuzzy rules
rule1 = ctrl.Rule(distance['near'], action['turn_left'])
rule2 = ctrl.Rule(distance['medium'], action['go_straight'])
rule3 = ctrl.Rule(distance['far'], action['turn_right'])

# Control system
obstacle_avoidance = ctrl.ControlSystem([rule1, rule2, rule3])
avoidance_decision = ctrl.ControlSystemSimulation(obstacle_avoidance)

# Test
sensor_distance = us.get_distance()
avoidance_decision.input['distance'] = sensor_distance
avoidance_decision.compute()

print(avoidance_decision.output['action'])
