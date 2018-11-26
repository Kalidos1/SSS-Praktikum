# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:12:39 2018

@author: ds-03
"""

import numpy as np
from TekTDS2000 import *



def read_from_oszi():
    scope = TekTDS2000()
    scope.saveCsv(filename='./Messergebnisse/BoxKlein/100HzKlein.cvs',ch=2)
    scope.plot(2,filename='./Messergebnisse/BoxKlein/100HzKlein.png')
    
    

def read_from_file():
    data = np.genfromtxt('./Mundharmonika.cvs')
    return data


def transform(f):
    f = np.fft.fft(f)
    
    

def main():
    #read_from_oszi()
    
    scope = TekTDS2000()
    freq = scope.getFreq()
    x,y= scope.getData(1)
    
    print(freq)
    ab = abs(x[0])-abs(x[1]) 
    print(ab,1/ab)
    print(ab * 2500)
    
    
    

if __name__ == '__main__':
    main()


