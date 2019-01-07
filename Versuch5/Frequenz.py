# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:10:18 2019

@author: ds-03
"""

import redlab as rl
import numpy as np


print("Samplerate:" + str(rl.cbInScanRate(0,0,0,7674)))

a = (rl.cbVInScan(0,0,0,300,7674,1))
np.savetxt("2000Frequenz.csv",a,delimiter=',')
np.save("2000Frequenz",a)

print(a)


#Rate/AbtastFrequenz = 7674
#Tatsächliche Abtastfrequnz = 7692 (Siehe Rückgabewert)
#Nyquist-Frequenz = Rate / 2 = 3837


#SinusFrequenz = 0.01
#1.Frequenz = 2500 HZ
#2.Frequenz = 3000 HZ
#3.Frequenz = 3500 HZ
#4.Frequenz = 4000 HZ
#5.Frequenz = 4500 HZ
#6.Frequenz = 5000 HZ
#7.Frequenz = 2000 HZ