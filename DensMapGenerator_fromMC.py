# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:22:42 2019

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

# SETTINGS: ---
dens_graph = sim_graph_0
n_lig = 132
cutoff = 0.5

dx,dy=1,1
y,x = np.mgrid[slice(0,132,dy),slice(0,132,dx)]
densmap = x*0


adj = np.array(dens_graph.get_adjacency().data)
#
#for i in range(1,5+1):
#    # Add density to points around location of each ligand
#    for x in range(int((i-cutoff)*10),int((i+cutoff)*10)):
#        for y in range(int((i-cutoff)*10),int((i+cutoff)*10)):
#            densmap[x][y]+=1
#    
#    for j in range(0,n_lig):
#        con = adj[i][j]
#        



fig, ax = plt.subplots(figsize=(3,3))

ax.pcolor(x,y,adj,cmap='hot')
plt.show()

#
#
#plt.grid()
#
#pickle_in = open("paramsearch0.5-2.0.pickle","rb")
#param2 = pickle.load(pickle_in)
#ax.bar([1,2,3],np.mean(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),yerr=np.std(param2[0][:,start:end],axis=1)/np.sum(np.mean(param2[0][:,start:end],axis=1)),width=0.5)
#pickle_in.close()

#plt.show()
