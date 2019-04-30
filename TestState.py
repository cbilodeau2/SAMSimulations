# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:21:10 2019

@author: camil
"""

def TestState(graph,A,B,C):
    w1 = float(np.shape(graph.get_edgelist())[0])
    w2 = np.shape(graph.maximal_cliques(min=3,max=3))[0]
    w3 = np.shape(FindTetrahedraFast(graph))[0] 
    #w3 = (np.shape(graph.maximal_cliques(min=3,max=3))[0]==2)*1
    ener = w1*A - w2*B + w3*C  #w1*0.25-w2*1.5
    return ener