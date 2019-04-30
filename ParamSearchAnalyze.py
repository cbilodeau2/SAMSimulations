# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:08:39 2019

# Code 3

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

start=10000
end=20000

fig, ax = plt.subplots(figsize=(3,2))


plt.grid()

pickle_in = open("paramsearch0.0-2.0.pickle","rb")
param2 = pickle.load(pickle_in)
ax.bar([0.25,2.25,4.25],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.25)
pickle_in.close()

pickle_in = open("paramsearch0.2-2.0.pickle","rb")
param2 = pickle.load(pickle_in)
ax.bar([0.2,2.5,4.5],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.25)
pickle_in.close()

pickle_in = open("paramsearch0.4-2.0.pickle","rb")
param2 = pickle.load(pickle_in)
ax.bar([0.75,2.75,4.75],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.25)
pickle_in.close()

pickle_in = open("paramsearch0.6-2.0.pickle","rb")
param2 = pickle.load(pickle_in)
ax.bar([1.0,3.0,5.0],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.25)
pickle_in.close()

pickle_in = open("paramsearch0.8-2.0.pickle","rb")
param2 = pickle.load(pickle_in)
ax.bar([1.25,3.25,5.25],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.25)
pickle_in.close()

pickle_in = open("paramsearch1.0-2.0.pickle","rb")
param2 = pickle.load(pickle_in)
ax.bar([1.5,3.5,5.5],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.25)
pickle_in.close()

plt.ylim(0,1)

