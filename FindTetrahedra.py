# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:07:25 2019

@author: camil
"""

def FindTetrahedra(graph):
    tetra_list = []
    
    
    
    for i in range(0, (np.shape(graph.get_edgelist())[0]-4)):
        edge1 = np.array(graph.get_edgelist()[i])
    
        for j in range(i+1,np.shape(graph.get_edgelist())[0]-3):
            edge2 = np.array(graph.get_edgelist()[j])
        
            if (np.size(np.unique([edge1,edge2]))==3): # Edges 1 and 2 share a vertex
                for k in range(j+1,np.shape(graph.get_edgelist())[0]-2):
                    edge3 = np.array(graph.get_edgelist()[k])    
                
                    for l in range(k+1,np.shape(graph.get_edgelist())[0]-1):
                        edge4 = np.array(graph.get_edgelist()[l])
                    
                        if (np.size(np.unique([edge1,edge2,edge3,edge4]))==4):
                            for m in range(l+1,np.shape(graph.get_edgelist())[0]):
                                edge5 = np.array(graph.get_edgelist()[m])
                                if np.size(np.unique([edge1,edge2,edge3,edge4,edge5]))==4:
                                    tetra_list.append([edge1,edge2,edge3,edge4,edge5])
    return tetra_list