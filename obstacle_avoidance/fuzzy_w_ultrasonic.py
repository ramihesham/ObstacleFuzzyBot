import numpy as np
import skfuzzy.control as ctrl
import skfuzzy as fuzz

# Define linguistic variables
distance = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')
action = ctrl.Consequent(np.arange(0, 101, 1), 'action')

# Membership functions for Distance
distance['near'] = fuzz.trimf(distance.universe, [0, 0, 25])
distance['medium'] = fuzz.trimf(distance.universe, [0, 50, 100])
distance['far'] = fuzz.trimf(distance.universe, [75, 100, 100])

# Membership functions for Action
action['turn_left'] = fuzz.trimf(action.universe, [0, 0, 50])
action['go_straight'] = fuzz.trimf(action.universe, [25, 50, 75])
action['turn_right'] = fuzz.trimf(action.universe, [50, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(distance['near'], action['turn_left'])
rule2 = ctrl.Rule(distance['medium'], action['go_straight'])
rule3 = ctrl.Rule(distance['far'], action['turn_right'])

# Control system
obstacle_avoidance = ctrl.ControlSystem([rule1, rule2, rule3])
avoidance_decision = ctrl.ControlSystemSimulation(obstacle_avoidance)

# Test
avoidance_decision.input['distance'] = 15
avoidance_decision.compute()

print(avoidance_decision.output['action'])
action.view(sim=avoidance_decision)
