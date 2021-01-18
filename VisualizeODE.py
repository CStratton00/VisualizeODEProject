# Collin Stratton
# CST-305
# Topic 1 Project 1: Visualize ODE with SciPy
# Dr. Ricardo Citro

# For this project, I am simulating an ODE for the GCU Internet Speed
# Packages used: numpy, matplotlib, scipy
# Implementation approach: developed an ODE function using scypi.odeint (outlined in documentation)
# Found internet speed and graphed results using plt.plot() from matplotlib

import numpy as np                          # import numpy for array space
import matplotlib.pyplot as plt             # import matplotlib to graph function
from scipy.integrate import odeint          # import scipy to use the ordinary differencial equation integral function

# function dx_dt solves for the Number of Packets per Second 
# by taking the Number of Packets times Time
def dx_dt(x, t, k):                         # dx/dt = Number of Packets per Second
    return k * t                            # return the value generated from k * t

ts = np.linspace(0, 10, 100)                # t     = Time(Seconds)
x = 1000                                    # x     = Number of Packets
k = 1000                                    # k     = Initial Number of Packets

xs = odeint(dx_dt, k, ts, args=(x,))        # function to find the ODE Integral of x and t

# matplotlib graph displaying number of packets over time
plt.xlabel("t")
plt.ylabel("x")
plt.plot(ts, xs)
plt.show()