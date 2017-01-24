# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:59:31 2015

@author: vhaconbatesj
"""

# [1] Sparse kernel methods for survival data

import numpy as np
import matplotlib.pyplot as plt
import random

def simulation1():
    # from [1]
    # gene expression levels with 5 groups

    n = 10    # number of samples    
    p = 1600  # number of genes
    gA = random.sample(range(n),int(np.floor(0.5*n)))
    gB = random.sample(range(n),int(np.floor(0.5*n)))
    gC = random.sample(range(n),int(np.floor(0.333*n)))
    gD = random.sample(range(n),int(np.floor(0.333*n)))
    gE = random.sample(range(n),int(np.floor(0.333*n)))
    
    x = np.random.normal(0.,1.,(n,p)) # gene expression levels    
    
    x[gA,0:10] = np.random.normal(2.,1.,(len(gA),10))
    x[gB,10:30] = np.random.normal(-3.,1.,(len(gB),20))
    x[gC,30:50] = np.random.normal(4.,1.,(len(gC),20))
    x[gD,50:75] = np.random.normal(5.,1.,(len(gD),25))
    x[gE,75:100] = np.random.normal(-4.,1.,(len(gE),25))
    
    beta = np.zeros(p)
    beta[range(0,len(beta),10)] = np.random.normal(0.,1.,int(0.1*p))
    
    alpha = np.zeros(n)
    alpha[list(set(gA).intersection(gB))] = 3.
    
    # hazard = alpha+np.dot(x,beta)
    hazard = np.exp(alpha+np.dot(x,beta))
    
    t_obs = np.random.uniform(0,2,n)
    t_surv = np.random.exponential(hazard)
    censored = t_obs < t_surv
    
    