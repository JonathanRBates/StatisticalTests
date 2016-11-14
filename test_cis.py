# -*- coding: utf-8 -*-

# cf. R. G. Newcombe
# [1] Two-sided confidence intervals for the single proportion, 1998
# [2] Interval Estimation for the difference between independent proportions: 
#       comparison of eleven methods, 1998

import numpy as np
from statsmodels.stats.proportion import proportion_confint


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def propci_wilson_cc(count, nobs, alpha=0.05):
    # get confidence limits for proportion
    # using wilson score method w/ cont correction
    # i.e. Method 4 in Newcombe [1]; 
    # verified via Table 1
    from scipy import stats
    n = nobs
    p = count/n
    q = 1.-p
    z = stats.norm.isf(alpha / 2.)
    z2 = z**2   
    denom = 2*(n+z2)
    num = 2.*n*p+z2-1.-z*np.sqrt(z2-2-1./n+4*p*(n*q+1))    
    ci_l = num/denom
    num = 2.*n*p+z2+1.+z*np.sqrt(z2+2-1./n+4*p*(n*q-1))
    ci_u = num/denom
    if p == 0:
        ci_l = 0.
    elif p == 1:
        ci_u = 1.
    return ci_l, ci_u


def dpropci_wilson_nocc(a,m,b,n,alpha=0.05):
    # get confidence limits for difference in proportions
    #   a/m - b/n
    # using wilson score method WITHOUT cont correction
    # i.e. Method 10 in Newcombe [2]
    # verified via Table II    
    theta = a/m - b/n        
    l1, u1 = proportion_confint(count=a, nobs=m, alpha=0.05, method='wilson')
    l2, u2 = proportion_confint(count=b, nobs=n, alpha=0.05, method='wilson')
    ci_u = theta + np.sqrt((a/m-u1)**2+(b/n-l2)**2)
    ci_l = theta - np.sqrt((a/m-l1)**2+(b/n-u2)**2)     
    return ci_l, ci_u


def dpropci_wilson_cc(a,m,b,n,alpha=0.05):
    # get confidence limits for difference in proportions
    #   a/m - b/n
    # using wilson score method w/ cont correction
    # i.e. Method 11 in Newcombe [2]    
    # verified via Table II  
    theta = a/m - b/n    
    l1, u1 = propci_wilson_cc(count=a, nobs=m, alpha=alpha)
    l2, u2 = propci_wilson_cc(count=b, nobs=n, alpha=alpha)    
    ci_u = theta + np.sqrt((a/m-u1)**2+(b/n-l2)**2)
    ci_l = theta - np.sqrt((a/m-l1)**2+(b/n-u2)**2)     
    return ci_l, ci_u


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# single proportion testing 
# these come from Newcombe [1] (Table 1)
a_vec = np.array([81, 15, 0, 1])
m_vec = np.array([263, 148, 20, 29])
for (a,m) in zip(a_vec,m_vec):
    l1, u1 = proportion_confint(count=a, nobs=m, alpha=0.05, method='wilson')
    l2, u2 = propci_wilson_cc(count=a, nobs=m, alpha=0.05)
    print(a,m,l1,u1,'   ',l2,u2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# difference in proportions testing 
# these come from Newcombe [2] (Table II)
a_vec = np.array([56,9,6,5,0,0,10,10],dtype=float)
m_vec = np.array([70,10,7,56,10,10,10,10],dtype=float)
b_vec = np.array([48,3,2,0,0,0,0,0],dtype=float)
n_vec = np.array([80,10,7,29,20,10,20,10],dtype=float)

print('\nWilson without CC')
for (a,m,b,n) in zip(a_vec,m_vec,b_vec,n_vec):
    l, u = dpropci_wilson_nocc(a,m,b,n,alpha=0.05)
    print('{:2.0f}/{:2.0f}-{:2.0f}/{:2.0f} ; {:6.4f} ; {:8.4f}, {:8.4f}'.format(a,m,b,n,a/m-b/n,l,u))

print('\nWilson with CC')
for (a,m,b,n) in zip(a_vec,m_vec,b_vec,n_vec):
    l, u = dpropci_wilson_cc(a,m,b,n,alpha=0.05)
    print('{:2.0f}/{:2.0f}-{:2.0f}/{:2.0f} ; {:6.4f} ; {:8.4f}, {:8.4f}'.format(a,m,b,n,a/m-b/n,l,u))

