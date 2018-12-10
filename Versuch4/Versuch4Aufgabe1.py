# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:15:55 2018

@author: ds-03
"""

import numpy as np
import matplotlib.pyplot as plt

tmparray = ['1','2','3','4','5']
decoded = []

for x in range(len(tmparray)):
    decoded = np.load('./ErsteAufnahme/Rechts' + tmparray[x] + '.npy')
    print(x)
    plt.plot(decoded)
    axes = plt.gca()
    axes.plot(decoded)
    axes.set_xlim([70000,120000])    
    