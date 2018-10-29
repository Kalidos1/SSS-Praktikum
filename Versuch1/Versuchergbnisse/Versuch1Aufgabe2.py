# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:11:34 2018

@author: ds-03
"""

import numpy as np


def func0(x): 
    a = np.genfromtxt(x,delimiter=",",skip_header=1000)
    return a[:,3:5]

print(func0('10cmEntfernung.csv'))



#mittelwert
#standardbweichung
#graphische darstellung