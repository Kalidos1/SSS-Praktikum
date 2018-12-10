# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:44:51 2018

@author: ds-03
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

tmparray = ['1','2','3','4','5']

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220


for x in range(len(tmparray)):
    q = input('Enter Q to Begin Recording: ')
    if 'q' == q:
        p = pyaudio.PyAudio()
        print('running')        
        
        stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ
                        ,input=True,frames_per_buffer=FRAMESIZE)
        data = stream.read(NOFFRAMES * FRAMESIZE)
        
        decoded = np.fromstring(data, 'Int16');
        stream.stop_stream()
        stream.close()
        p.terminate()
        print('done')
        
        plt.plot(decoded)
        plt.xlabel('Zeit (ms)')
        plt.ylabel('Frequenz (Hz)')
        plt.show()
        np.save(('Tief' + tmparray[x]),decoded) 
    else:
        break




