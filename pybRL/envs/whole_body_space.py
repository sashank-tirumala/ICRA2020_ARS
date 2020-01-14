import matplotlib.pyplot as plt 
import numpy as np
from numpy import cos, sin
PI = np.pi

body_width = 0.24
body_length = 0.37
body_radius = ((body_width/2)**2 + (body_length/2)**2)**0.5
step_length = 0.068*2
step_length = 0.1*2


def get_world_coords(com_position, local_coordinates):
    th = com_position[2]
    trans = np.array([[cos(th), -sin(th), com_position[0]],
                    [sin(th), cos(th), com_position[1]],
                    [0,0,1]])
    world_coords = []
    for i in np.arange(local_coordinates.shape[0]):
        world_coords.append(trans@local_coordinates[i])
    return np.array(world_coords)

def plot_world_coords(axes, coordinates):
    x = []
    y = []
    for coord  in coordinates:
        x.append(coord[0])
        y.append(coord[1])
    x.append(x[0])
    y.append(y[0])
    axes.plot(x,y)

def plot_circle(axes, com):
    x_circ = np.zeros(100)
    y_circ = np.zeros(100)
    for i  in np.arange(100):
        x_circ[i] = com[0]+body_radius*np.cos(i*2*PI/100)
        y_circ[i] = com[1]+body_radius*np.sin(i*2*PI/100)
    axes.plot(x_circ, y_circ)

def get_new_com(com, state):
    mod = (state[0]**2 + state[1]**2 + state[2]**2)**0.5
    if(mod == 0):
        return com
    else:
        return np.array([com[0]+(state[1]/mod)*step_length,
                     com[1]+(state[0]/mod)*step_length,
                     com[2]+(state[2]/mod)*step_length ])
flx = -body_width/2
fly = body_length/2
frx = body_width/2
fry = body_length/2
blx = -body_width/2
bly = -body_length/2
brx = body_width/2
bry = -body_length/2

state = np.array([-1,1,1])

fltheta1 = np.arctan2(-body_width/2, body_length/2)
frtheta1 = np.arctan2(body_width/2, body_length/2)
brtheta1 = np.arctan2(body_width/2, -body_length/2)
bltheta1 = np.arctan2(-body_width/2, -body_length/2)
max_theta = step_length/body_radius
plt.figure(0)
fig,a = plt.subplots(1,4)
local_coords = np.array([[flx,fly,1],[frx,fry,1],[brx,bry,1],[blx,bly,1]])
com = np.array([0,0,0])
world_coords = get_world_coords(com, local_coords)
plot_world_coords(a[0], world_coords)
plot_circle(a[0],com)
a[0].set_title("t = 0")
a[0].set_xlim([-1,1])
a[0].set_ylim([-1,1])

com = get_new_com(com, state)
world_coords = get_world_coords(com, local_coords)
plot_world_coords(a[1], world_coords)
plot_circle(a[1],com)
a[1].set_title("t = T/2")
a[1].set_xlim([-1,1])
a[1].set_ylim([-1,1])

com = get_new_com(com, state)
world_coords = get_world_coords(com, local_coords)
plot_world_coords(a[2], world_coords)
plot_circle(a[2],com)
a[2].set_title("t = T")
a[2].set_xlim([-1,1])
a[2].set_ylim([-1,1])

com = get_new_com(com, state)
world_coords = get_world_coords(com, local_coords)
plot_world_coords(a[3], world_coords)
plot_circle(a[3],com)
a[3].set_title("t = 3T/2")
a[3].set_xlim([-1,1])
a[3].set_ylim([-1,1])

plt.show()
# theta_dash = Omega*max_theta/mod

# y[0] = y[0] + body_radius*(np.cos(fltheta1 + theta_dash) - np.cos(fltheta1))
# y[1] = y[1] + body_radius*(np.cos(frtheta1 + theta_dash) - np.cos(frtheta1))
# y[2] = y[2] + body_radius*(np.cos(brtheta1 + theta_dash) - np.cos(brtheta1))
# y[3] = y[3] + body_radius*(np.cos(bltheta1 + theta_dash) - np.cos(bltheta1))
# y[4] = y[4] + body_radius*(np.cos(fltheta1 + theta_dash) - np.cos(fltheta1))

# x[0] = x[0] + body_radius*(np.sin(fltheta1 + theta_dash) - np.sin(fltheta1))
# x[1] = x[1] + body_radius*(np.sin(frtheta1 + theta_dash) - np.sin(frtheta1))
# x[2] = x[2] + body_radius*(np.sin(brtheta1 + theta_dash) - np.sin(brtheta1))
# x[3] = x[3] + body_radius*(np.sin(bltheta1 + theta_dash) - np.sin(bltheta1))
# x[4] = x[4] + body_radius*(np.sin(fltheta1 + theta_dash) - np.sin(fltheta1))
# x_circ = np.zeros(100)
# y_circ = np.zeros(100)
# for i  in np.arange(100):
#     x_circ[i] = np.mean(x[:-1])+body_radius*np.cos(i*2*PI/100)
#     y_circ[i] = np.mean(y[:-1])+body_radius*np.sin(i*2*PI/100)

# a[1].plot(x,y)
# a[1].plot(x_circ, y_circ)
# a[1].set_title("t = T/2")
# a[1].set_xlim([-1,1])
# a[1].set_ylim([-1,1])

# plt.show()