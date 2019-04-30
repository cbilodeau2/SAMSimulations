# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:34:48 2019
Intended for full/continuous SAM surface

Code 3

@author: camil
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm
import matplotlib.colors as col
from scipy.optimize import curve_fit
import pandas as pd
from math import factorial
import igraph
from igraph import *
import random
import time

nsteps=10000

fig, ax = plt.subplots(figsize=(5,4))
ax.plot(range(0,nsteps),clique_mon[0])
ax.plot(range(0,nsteps),clique_mon[1])
ax.plot(range(0,nsteps),clique_mon[2],'r')

ax.set_xlim(0,10000)
plt.show()


ax.plot(range(0,nsteps),n_edges_mon)


ax.set_xlim(90000,100000)
plt.show()


step_range = (1000,10000)

clique_avg = []
clique_avg.append(np.mean(clique_mon[0][step_range[0]:step_range[1]]))
clique_avg.append(np.mean(clique_mon[1][step_range[0]:step_range[1]]))
clique_avg.append(np.mean(clique_mon[2][step_range[0]:step_range[1]]))

clique_std = []
clique_std.append(np.std(clique_mon[0][step_range[0]:step_range[1]]))
clique_std.append(np.std(clique_mon[1][step_range[0]:step_range[1]]))
clique_std.append(np.std(clique_mon[2][step_range[0]:step_range[1]]))

fig2, ax2 = plt.subplots(figsize=(5,4))

ax2.bar(range(1,4),clique_avg/np.sum(clique_avg),yerr=clique_std/np.sum(clique_avg))

ax2.set_ylim(0,1)