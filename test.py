# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:51:32 2019

@author: camil
"""

for i in range(0,np.shape(sam_full.maximal_cliques(min=3,max=3))[0]-1):
    for j in range(i+1,np.shape(sam_full.maximal_cliques(min=3,max=3))[0]):
        #print sam_full.maximal_cliques(min=3,max=3)[i], sam_full.maximal_cliques(min=3,max=3)[j]
        print np.unique([sam_full.maximal_cliques(min=3,max=3)[i], sam_full.maximal_cliques(min=3,max=3)[j]])==1
        #print i,j