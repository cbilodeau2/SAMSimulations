# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:29:58 2019

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

#FullSAM = open("tet-paramsearch0.6-3.0.pickle","rb")
kT=2.48
#sam_stats = pickle.load(FullSAM)
sam_stats = [clique_mon,n_edges_mon,prob_mon]
first=5000
last=100000


n_edges_mon = sam_stats[1]

# Probability that nothing contacts
p_null=np.mean([int(i==0) for i in n_edges_mon[first:last]])

# Probability exactly one edge forms
p_single = np.mean([int(i==1) for i in n_edges_mon[first:last]])

# Probability exactly two edges forms
p_dim = np.mean([int(i==2) for i in n_edges_mon[first:last]])

# Probability that exactly one trimer forms
p_tri = np.mean([int(i==1) for i in sam_stats[0][2][first:last]])

# Probability that two trimers form
p_tet = np.mean([int(i==2) for i in sam_stats[0][2][first:last]])

# Free energy of exactly one edge forming:
dF_single = -kT*np.log(p_single/p_null) +kT*np.log(5)
print 'Free Energy of One Edge', dF_single

# Free energy of exactly two edge forming:
dF_dim = -kT*np.log(p_dim/p_null) +kT*np.log(10)
print 'Free Energy of Two Edges',dF_dim

# Free energy of a single closed trimer forming:
dF_tri = -kT*np.log(p_tri/p_null) +kT*np.log(2)
print 'Free Energy of One Closed Triplet',dF_tri

# Free energy of a single closed trimer forming:
dF_tet = -kT*np.log(p_tet/p_null) +kT*np.log(1)
print 'Free Energy of Two Closed Triplets',dF_tet

#compare = [sam_stats[0][1], sam_stats[0][3],sam_stats[0][5],sam_stats[0][7]]
#compare_std = [sam_stats[1][1], sam_stats[1][3],sam_stats[1][5],sam_stats[1][7]]
#ax.bar(range(1,5),compare/np.sum(compare),yerr=compare_std/np.sum(compare),width=0.75)



#fig, ax = plt.subplots(figsize=(3,2))
#print 0, np.mean([int(i==0) for i in n_edges_mon[first:last]]) #np.mean(p_null)
#print 1,    np.mean([int(i==1) for i in n_edges_mon[first:last]]) #- np.mean([int(i==0) for i in n_edges_mon[first:last]])                              #np.mean(p_dimer)
#print 2,  np.mean([int(i==2) for i in n_edges_mon[first:last]]) #- np.mean([int(i==0) for i in n_edges_mon[first:last]])                                #np.mean(p_double_dimer)
#print 3,   np.mean([int(i==3) for i in n_edges_mon[first:last]]) #- np.mean([int(i==0) for i in n_edges_mon[first:last]])                    #np.mean([p_trimer1,p_trimer2])
#print 5,                     #np.mean(p_tetramer)
