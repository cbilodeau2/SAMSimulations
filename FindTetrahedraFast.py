# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:51:32 2019

@author: camil
"""
def FindTetrahedraFast(graph):
    count = 0
    for i in range(0,np.shape(graph.maximal_cliques(min=3,max=3))[0]-1):
        for j in range(i+1,np.shape(graph.maximal_cliques(min=3,max=3))[0]):
            vertices = np.unique([graph.maximal_cliques(min=3,max=3)[i], graph.maximal_cliques(min=3,max=3)[j]])
            if np.shape(vertices)[0]==4:
                count+=1
    return count 
 