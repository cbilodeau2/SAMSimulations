# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:04:24 2019

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
import pickle


fig, ax = plt.subplots(figsize=(3,2))

FullSAM = open("cluster_hist.pickle","rb")

sam_stats = pickle.load(FullSAM)
compare = [sam_stats[0][1], sam_stats[0][3],sam_stats[0][5],sam_stats[0][7]]
compare_std = [sam_stats[1][1], sam_stats[1][3],sam_stats[1][5],sam_stats[1][7]]

#plt.bar(np.arange(0.5,3.5),clique_avg/np.sum(clique_avg),yerr=clique_std/np.sum(clique_avg),width=0.1)

#plt.grid()

ax.bar(range(1,5),compare/np.sum(compare),yerr=compare_std/np.sum(compare),width=0.25)
ax.bar([1.25,2.25,3.25],np.mean(clique_mon,axis=1)/np.sum(np.mean(clique_mon,axis=1)),yerr = np.std(clique_mon,axis=1)/np.sum(np.mean(clique_mon,axis=1)),width=0.25)

plt.ylim(0,1)
plt.show()