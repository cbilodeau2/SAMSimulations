# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:52:46 2019

Code 2

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

Asearch = [0.6] #[0.6] #,0.6,0.7,0.8,0.9] # 0.7, 0.8, 0.9] #[0.39] #np.arange(0,1.2,0.2)
Bsearch = [0.4] #[0.4] #,1.6,1.7,1.8,1.9,2.0] # 1.5, 1.6, 1.7, 1.8, 1.9,2.0,2.1,2.2,2.3] #[2.11] #np.arange(0.6,1.0,0.1)
Csearch = [-2.7] #[-3.1]
# Preallocate varaibles:
clique_list = []
n_edges_list = []
prob_list = []

for A in Asearch:
    for B in Bsearch:
        for C in Csearch:
        
            print 'Parameter Search: A = ', A, 'B = ', B, 'C= ', C
        
            clique_mon,n_edges_mon,prob_mon = MonteCarloSAM(sam_full,10000,A,B,C)
        
       
        #pickle_out = open("tri-paramsearch"+str(A)+'-'+str(B)+".pickle","wb")
        #pickle.dump([clique_mon,n_edges_mon,prob_mon], pickle_out)
        #pickle_out.close()
        
        
        