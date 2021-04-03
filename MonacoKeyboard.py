# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:40:43 2020

@author: Iris
"""


import numpy as np
#from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D, Space, F12, PageDown

#countdown
# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)



def fivepages():
    #5 pages
    PressKey(F12)
    time.sleep(0.5)
    ReleaseKey(F12)
    time.sleep(0.5)
    
    for i in list(range(4))[::-1]:    
        PressKey(PageDown) 
        time.sleep(0.5)
        ReleaseKey(PageDown)
        time.sleep(3)
        
        PressKey(F12)
        time.sleep(0.5)
        ReleaseKey(F12)
        time.sleep(0.5)



def nextpage():
    PressKey(D)
    time.sleep(0.5)




#https://www.youtube.com/watch?v=tWqbl9IUdCg