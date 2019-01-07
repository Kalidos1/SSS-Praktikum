# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:05:21 2019

@author: ds-03
"""

import redlab as rl

#print("-------einzelneWerte-------------------------")
#print("16BitValue:" + str(rl.cbAIn(0,0,1)))
print("VoltageValue:" + str(rl.cbVIn(0,0,1)))
#print("-------Messreihe-------------------------")
#print("Messreihe:" + str(rl.cbAInScan(0,0,0,300,8000,1)))
#print("Messreihe:" + str(rl.cbVInScan(0,0,0,300,8000,1)))
#print("Samplerate:" + str(rl.cbInScanRate(0,0,0,8000)))
#print("-------Ausgabe-------------------------")
print("VoltageValue:" + str(rl.cbVOut(0,0,101,5.0)))




