# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:11:37 2018

@author: ds-03
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(14,16)
cap.set(15,-3)
cap.set(10,128)
cap.set(11,32)
cap.set(12,115)
gray = None

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    cv2.imshow('frame', gray)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Versuch2WeissbildTest.png",gray)
        break;    
  
print(np.max(gray))
print(np.min(gray))        
        
print("framewidth:" + str(cap.get(3)))
print("frameheight:" + str(cap.get(4)))
print("--------------------------------")
print("brightness:" + str(cap.get(10)))
print("contrast:" + str(cap.get(11)))
print("saturation:" + str(cap.get(12)))
print("--------------------------------")
print("gain:" + str(cap.get(14)))
print("exposure:" + str(cap.get(15)))
print("--------------------------------")
print("whitebalance:" + str(cap.get(17)))

        
cap.release()
cv2.destroyAllWindows()