# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:06:56 2015

@author: jon
"""

'''
library(survival)
fit <- survfit(Surv(time, status))  # KM estimator
plot(fit)
plot(-log(fit))
plot(basehaz(coxph(Surv(time, status)~1))) # Nelson Aalen estimator
fit <- survfit(Surv(time, status)~1)  #
str(fit)
plot(cumsum(fit$n.event/fit$n.risk))
plot(-log(fit$surv))
# survreg(Surv(time, status) ~ 1)
# coxfit <- coxph(Surv(time, status)~1)
'''

import rpy2.robjects as rx
from rpy2.robjects import IntVector, Formula
from rpy2.robjects.packages import importr
sv = importr('survival')
graphics = importr('graphics')
time = IntVector([1,2,3,4,5,6])
status = IntVector([1,1,0,0,0,0])
fmla = Formula('Surv(time, status) ~ 1')
fmla.environment['time'] = time
fmla.environment['status'] = status
fit = sv.coxph(fmla)
print(fit.names[5])
fmlb = Formula('-log(fit$surv)')
fmlb.environment['fit'] = fit
graphics.plot(fmlb)

# rx.globalenv['SURVTIMESTATUS'] = sv.Surv(time, status)
sv.coxph('SURVTIMESTATUS~1')

sv.survfit(sv.Surv(time, status))


rcode1 = '''
library(survival)
fit <- survfit(Surv(time, status)~1)  
cumsum(fit$n.event/fit$n.risk)
'''.format(time=IntVector([1,2,3,4,5,6]), status = IntVector([1,1,0,0,0,0]))

rcode2 = '''
library(survival)
fit <- survfit(Surv(time, status)~1)  
-log(fit$surv)
'''.format(time=IntVector([1,2,3,4,5,6]), status = IntVector([1,1,0,0,0,0]))

import matplotlib.pyplot as plt
plt.plot(rx.r(rcode1))
rx.r(rcode2)
