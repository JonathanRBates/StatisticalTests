# -*- coding: utf-8 -*-
"""

This script is for sample size calculations, originally intended to test the 
feasibility of postmarket surveillance studies.
The sample size calculations are based on Poisson tests, mostly two-sample, 
but a few where the number of controls is fixed before running the tests.
In particular, two Poisson processes with failure rates gamma0, gamma1
are observed for fixed times s0, s1.  The number of outcomes observed X0, X1
are assumed to be Poisson random variables with means gamma0*s0 and gamma1*s1.
(If you don't like this assumption, consider negative binomial tests, etc.)
In the following, we test H0: gamma0=gamma1 against H1: gamma1 > gamma0.

Notation:
r = gamma1/gamma0         the "rate ratio"
d = s1/s0
alpha = significance level
beta = 1 - Power

    alpha = type I error
    beta = type II error

"""

def TwoSamplePoissonTestA(r,d,alpha,beta):
    """
    Shiue and Bain's test    
    
    Return:
        S1, the observation time need to treat
    """
    from scipy import stats
    from numpy import sqrt
    C = (r/d+1.)/(r-1.)**2
    D = sqrt((1.+d*r)/(d+r))
    ka = stats.norm.ppf(1.-alpha)
    kb = stats.norm.ppf(1.-beta)
    lambda0 = C*(D*ka+kb)**2
    return lambda0
        
        
def TwoSamplePoissonTestB(r,d,alpha,beta):
    """
    Huffman's test    
    
    Return:
        S1, the observation time need to treat
    """
    from scipy import stats
    from numpy import sqrt
    C = (d+1.)/(4*d*(sqrt(r)-1.)**2)    
    ka = stats.norm.ppf(1.-alpha)
    kb = stats.norm.ppf(1.-beta)
    lambda0 = C*(ka+kb)**2    
    return lambda0
        
        
def TwoSamplePoissonTestC(r,d,alpha,beta):
    """
    Wu & Makuch's Approximate Test    
    
    Return:
        S1, the observation time need to treat
    """
    from scipy import stats
    from numpy import sqrt
    C = 1./(d*(r-1.)**2)    
    ka = stats.norm.ppf(1.-alpha)
    kb = stats.norm.ppf(1.-beta)
    lambda0 = C*(ka*sqrt(r+d)+kb*sqrt(r))**2    
    return lambda0
    
    
    
    
##############################################################################
# Test Code
##############################################################################

# Planes example in Huffman    
alpha = 0.05
beta = 0.10
r = 2.
d = 2.
tA = TwoSamplePoissonTestA(r,d,alpha,beta)
tB = TwoSamplePoissonTestB(r,d,alpha,beta)
tC = TwoSamplePoissonTestC(r,d,alpha,beta)
print('{:10.4f} {:10.4f} {:10.4f} {:10.4f} {:10.4f}'.format(d, r, tA, tB, tC))

# Table 1 in Wu & Makuch
alpha = 0.025
beta = 0.2
gamma0 = 0.001
gamma1 = 0.003
r = gamma1/gamma0
d = 0.681
tA = TwoSamplePoissonTestA(r,d,alpha,beta) / gamma0
tB = TwoSamplePoissonTestB(r,d,alpha,beta) / gamma0
tC = TwoSamplePoissonTestC(r,d,alpha,beta) / gamma0       
print('{:10.4f} {:10.4f} {:12.0f} {:12.0f} {:12.0f}'.format(gamma0, r*gamma0, tA, tB, tC))
