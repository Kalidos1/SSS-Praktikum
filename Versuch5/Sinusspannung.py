# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:32:36 2019

@author: ds-03
"""

import redlab as rl
import numpy as np
from time import sleep

x = np.arange(30)
sin = [np.sin(2*np.pi*2*(i/30)) for i in x]


while (True):
    for i in sin:
        rl.cbVOut(0,0,101,i + 2.0)
        sleep(0.01)
        
        
    
        

