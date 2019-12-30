import sys, os
sys.path.append(os.path.realpath('../..'))
# sys.path.append('/home/sashank/stoch2_gym_env')
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pybRL.utils.logger import DataLog
import pybRL.utils.make_train_plots as plotter 
import pybRL.envs.stoch2_gym_bullet_env_bezier as e

import pybullet as p
import numpy as np
import time
PI = np.pi
#fl. fr. bl. br
walk = [0, PI, PI/2, 3*PI/2]
pace = [0, PI, 0, PI]
bound = [0, 0, PI, PI]
trot = [0, PI, PI , 0]
custom_phase = [0, PI, PI+0.1 , 0.1]

env = e.Stoch2Env(render = True, phase = trot, stairs = False, on_rack = False, gait ="trot+turn")

path = '/pybRL/ARS/24Dec1/iterations/best_policy.npy'
path = os.path.realpath('../..') + path
state = env.reset()
logger = DataLog()
i = 0
policy = np.load(path)
print(policy)
total_reward = 0
states = []
# action = np.array([ 0.24504616, -0.11582746,  0.71558934, -0.46091432, -0.36284493,  0.00495828,
#  -0.06466855, -0.45247894,  0.72117291, -0.11068088])
mul_ref =0
action = policy.dot(state)

if(action.size == 10):
  mul_ref = np.array([0.08233419, 0.07341638, 0.04249794, 0.04249729, 0.07341638, 0.08183298,0.07368498, 0.04149645, 0.04159619, 0.07313576])
elif(action.size == 20):
  mul_ref = np.array([0.08733419, 0.07801237, 0.07310331, 0.05280192, 0.04580373, 0.04580335, 0.05280085, 0.07310168, 0.07801237, 0.08683298, 0.11530908, 0.07157067, 0.05135627, 0.0447909,  0.04467491, 0.05151569, 0.0710504,  0.11530908])

steps = 0
roll_list = []
pitch_list = []
while steps<20:
  action = policy.dot(state)
  action = np.clip(action, -1, 1)
  print(action[1])
  actionf = np.multiply(action[2:], mul_ref) * 0.5
  action_spline_ref = np.multiply(np.ones(action[2:].size),mul_ref) * 0.5
  actionf = actionf + action_spline_ref
  actionf = actionf*0.9
  actionf = np.append(actionf, actionf[0])
  action_str = '{'
  for x in actionf:
    action_str = action_str + str(round(x,4)) + ','
  action_str = action_str[:-1] + '};\n'
  # print(action_str)
  # print("frequency_factor is {}". format(action[0]))
  state, reward, done, info = env.step(action)

# np.save("rolldata",np.array(roll_list))
# np.save("pitchdata",np.array(pitch_list))

# plt.plot(np.array(roll_list))
# plt.plot(np.array(pitch_list))
# plt.show()



# plotter.plot_traj(logger, ['x_leg1', 'x_leg2'], ['y_leg1', 'y_leg2'], ['Leg1 Trajectory, rep:5', 'Leg2 Trajectory, rep:5'], save_loc= '/home/kartik/RBC/quadruped/ICRA2020_ARS/pybRL/ARS/3Sept1/logs')