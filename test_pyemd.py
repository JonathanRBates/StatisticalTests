# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:58:51 2015

@author: jon
"""
# pip install F:\python\pyemd-0.1.1-cp34-none-win_amd64.whl
# this is from Pele and Werman's algorithm

import sys
sys.path.append('C:\\Users\\jon.cmsT1b-PC\\Desktop\\python')

import numpy as np
from pyemd import emd
import scipy.spatial.distance as dist

coords = np.reshape(np.linspace(1,6,num=6), (6,1))      # eg histogram centers
dmat = dist.squareform(dist.pdist(coords,metric='cityblock'))
print(dmat)


sig1 = np.array([.5,0.,.5,0.,0.])
sig2 = np.array([0.,0.,0.,0.,1.])
print(emd(sig1,sig2,dmat))

x = np.array([1.,2.,3.,4.,5.])
sig1 = x/np.sum(x)
y = np.array([2.,3.,4.,5.,6.])
sig2 = y/np.sum(y)

print(emd(x,y,dmat))
print(emd(sig1,sig2,dmat))



# examples in Pele, Werman...
coords = np.reshape(np.linspace(1,2,num=2), (2,1))      # eg histogram centers
dmat = dist.squareform(dist.pdist(coords,metric='cityblock'))
print(dmat)

sig1 = np.array([1.,0.])
sig2 = np.array([0.,1.])
print(emd(sig1,sig2,dmat), ' 1' )

sig1 = np.array([9.,0.])
sig2 = np.array([0.,9.])
print(emd(sig1,sig2,dmat), ' 9')

sig1 = np.array([1.,0.])
sig2 = np.array([1.,7.])
print(emd(sig1,sig2,dmat), ' 7')