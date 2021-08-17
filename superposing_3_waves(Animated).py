# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:13:58 2021

@author: kd34w
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')

t = np.linspace(0,1000,1000)
wt = 2*np.pi*t
phi = np.linspace(0,np.pi,50)
for alpha in phi:
    x1 = 5*np.sin(2*wt-alpha)
    x2 = 10*np.sin(wt)
    x3 = 10*np.cos(3*wt-alpha)
    
    plt.title('Superposition of two colinear waves\nDifferent amplitude') 
    plt.plot(x1+x2+x3,'r-',lw='3',label='Superposed Wave')
    plt.plot(x1,lw='0.9',label='$\phi$(x1)')
    plt.plot(x2,lw='0.9',label='$\phi$(x2)')
    plt.plot(x3,lw='0.9',label='$\phi$(x3)')
    plt.xlabel('$\phi$(x)')
    plt.ylabel('t')
    plt.legend()
    plt.show()


