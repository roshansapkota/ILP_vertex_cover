#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gurobipy import *
import random
from random import randint 
import numpy as np
import matplotlib.pyplot as plt 
import math


# In[2]:


N = int (input("Enter the number of Vertices: "))  #Aking users to enter the number of vertices


# In[3]:


vertices  = range(N)   #creating the range of vertices 


# In[4]:


random.seed(1)        #Given seed value to 1 to preserve the random values generated by randint

E =[]   #Generating the random number of edges

num_edges=randint(1, math.ceil(len(vertices)/2))   #Since one vertex can have n/2 edges at maximum. Ceiling value is taken.
for i in vertices:
    for a in range(num_edges):
        j = randint(0,len(vertices)-1)
        while j == i:
            j = randint(0,len(vertices)-1)
        if j < i:
            E.append((j, i))
        else: 
            E.append((i, j)) 
             
        
print(f"Initial Edges: {E}")   #Total number of edges
setE= set(E)  #Converting to set to avoid the same edge twice in the list if there are any.
edges= list(setE)  #Converting agian to list. 
print (f"Final Edges: {edges}")  #Final list of edges

            


# In[5]:


m= Model("MINIMUM vertex cover")


# In[6]:


# Creating binary varaibles of dictionary

V = {}

for v in vertices:
    V[v] = m.addVar(vtype=GRB.BINARY,obj=1.0, name="x%d" % v) 


# In[7]:


#Constraints

for edge in edges:
    u = edge[0]
    v = edge[1]
    xu = V[u]
    xv = V[v]
    m.addConstr(xu + xv >= 1) 


# In[8]:


#Creating the graph

ver_x = np.random.rand(N) * 200 
ver_y = np.random.rand(N) * 200

gra_vertex= [i for i in vertices]

plt.scatter(ver_x, ver_y, s=100, facecolors='none',edgecolors='b', zorder=2)
for i,j in edges:
    plt.plot([ver_x[i],ver_x[j]],[ver_y[i],ver_y[j]], c='g')
for i in gra_vertex:
    plt.annotate('$V  %d$' % (i), (ver_x[i]+2, ver_y[i]))
plt.title('GRAPH')


# In[9]:


m.optimize()  #opimizing the model


# In[10]:


cover = []
for v in vertices:
    if V[v].X > 0.5:
        print ('Vertex', v, 'is in the minimum set cover.')
        cover.append(v)


# In[ ]:



