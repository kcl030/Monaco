# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:51:57 2021

@author: Iris
"""
from MainMonaco import MapEntries
import time
from MonacoKeyboard import fivepages
from MonacoKeyboard import nextpage


directory = r'C:\Program Files (x86)\Steam\userdata\82949594\760\remote\113020\screenshots'


#a = keyboard.read_key()
All_Entries = []

print('waiting')

Answer = input("press 0 to coninue")

if Answer == '0':
    
    #countdown
    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(1)
    
    
    for x in range(1,5):   #Goes up to 49
        
        #does fivepages of capture. 
        fivepages()
    
    
        #opens stored excel file, compares to folder's pictures, and gets new entries from it 
        All_Entries.append(MapEntries(directory,x,True))
    
        print('done')
        #goes to next map
        nextpage()
        print('next')

   