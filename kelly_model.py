"""
Final revise: May 8, 2018

This is a simulation of the famous kelly model.

@author: chenkai
"""

from pandas import DataFrame
import random
import math
import string
import matplotlib.pyplot as plt  
import numpy as np
base = 100
pwin = 0.57
ploss = 1-pwin
b = 0.2
c = 0.2
# stopline
stopline = 1
rnd_position = 0.6
rnd_position2 = 0.9
kelly_position = (pwin/c - ploss/b)*stopline
print ('kelly position is %s'%kelly_position)
port_A = DataFrame()
port_B = DataFrame()
port_C = DataFrame()
port_D = DataFrame()
# num of simulations
for i in range(1000):
    port1 = [base]
    port2 = [base]
    port3 = [base]
    port4 = [base]
    # dt
    for step in range(500):
        rnd = random.random()
        if rnd < pwin:
            next_step = b
        else:
            next_step = -c
        if port1[-1] > base*(1-stopline):
            port1.append(port1[-1]*(1+next_step))
        else:
            port1.append(port1[-1])
        if port2[-1] > base*(1-stopline):
            port2.append(port2[-1]*(1+next_step*kelly_position))
        else:
            port2.append(port2[-1])
        if port3[-1] > base*(1-stopline):
            port3.append(port3[-1]*(1+next_step*rnd_position))
        else:
            port3.append(port3[-1])
        if port4[-1] > base*(1-stopline):
            port4.append(port4[-1]*(1+next_step*rnd_position2))
        else:
            port4.append(port4[-1])
    port_A[i] = port1
    port_B[i] = port2
    port_C[i] = port3
    port_D[i] = port4
plt.figure(figsize = (8,5))


plt.plot(np.exp(np.log(port_A.T).sum()/1000),label = 'port1:full')
plt.plot(np.exp(np.log(port_B.T).sum()/1000),label = 'port2:kelly')
plt.plot(np.exp(np.log(port_C.T).sum()/1000),label = 'port3:position = 0.6')
plt.plot(np.exp(np.log(port_D.T).sum()/1000),label = 'port3:position = 0.9')
plt.legend(loc = 0)
print ('\nReturns of all the portfolios')
print ('full position %s'%np.exp(np.log(port_A.T).sum()/1000).iloc[-1])
print ('kelly position %s'%np.exp(np.log(port_B.T).sum()/1000).iloc[-1])
print ('position = 0.6 %s'%np.exp(np.log(port_C.T).sum()/1000).iloc[-1])
print ('position = 0.9 %s'%np.exp(np.log(port_D.T).sum()/1000).iloc[-1])