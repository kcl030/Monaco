
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:19:14 2020

@author: Iris
"""

# import the necessary packages
from PIL import Image,ImageOps
import pytesseract
import argparse
import cv2
import os
import numpy as np
import re


def mainReadScreen(path):    
    #####################
    #Get OCR EXE
    ##################
    
    
    
    
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = cv2.imread(path)
    
    ##################################
    
    ###########
    #Declare Crop Coordinates 
    ###########
    
    
    #Name
    y1=420
    x1=500
    h1=295
    w1=350
    
    #Clock
    y2=420
    x2=1327
    h2=295
    w2=95
    
    #Seconds
    sy1=420
    sx1=1381
    sh1=30
    sw1=31
    #https://stackoverflow.com/questions/61134400/pytesseract-ocr-on-image-with-text-in-different-colors
    
    
    
    
    
    
    ##########################
    
    class PicOutput:
        def __init__(self,finaltext,finalgray,finalcrop_img):
            self.finaltext = finaltext
            self.finalgray = finalgray
            self.finalcrop_img = finalcrop_img
    
    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)
    
    def Get_Text_From_Coordinates(y,x,h,w,image,column,extra):
    
        
     
        #CROPPING
        crop_img1 = image[y:y+h, x:x+w]
    
        #cv2.imshow("cropped", crop_img1)
        
        hsv=cv2.cvtColor(crop_img1,cv2.COLOR_BGR2HSV)
    
        # Define lower and upper limits of what we call "brown"
        brown_lo=np.array([0,0,0])
        
        if column == 1:
            brown_hi=np.array([170,160,170])
        elif column==2:
            brown_hi=np.array([173,173,173])
        elif column==3:
            brown_hi=np.array([extra,extra,extra])      
            # brown_hi2=np.array([150,150,150])
            
            # mask2 = cv2.inRange(hsv,brown_lo,brown_hi2)
            # crop_img2[mask2>0]=(0,0,0)
            
        # Mask image to only select browns
        mask=cv2.inRange(hsv,brown_lo,brown_hi)
        
        
        # Change image to red where we found brown
        crop_img1[mask>0]=(0,0,0)
        
        
        
        #Grayscales
        
        if column !=3:
            gray1 = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)
            gray1 = cv2.threshold(gray1, 0, 90,
            		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        else:
            
            gray = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)
            gray1 = cv2.adaptiveThreshold(gray, 250, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1 )
            
            
            # gray3 = cv2.cvtColor(crop_img2, cv2.COLOR_BGR2GRAY)
            # gray4 = cv2.adaptiveThreshold(gray3, 250, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1 )  
    
        
        ############################
        
        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        
        filename = "{}.png".format(os.getpid())
        
        
        if column ==3:
            gray1 = np.invert(gray1)
            #gray4 = np.invert(gray4)
        
        
        
        cv2.imwrite(filename, gray1)
    
        
        text1 = pytesseract.image_to_string(Image.open(filename), config='--psm 6')
        os.remove(filename)
        
        textlower = text1.lower()
        something = textlower.islower()
        
        
        # if column == 3:    
        #     filename2 = "{}.png".format(os.getpid())
        #     cv2.imwrite(filename2, gray4)
        #     text2 = pytesseract.image_to_string(Image.open(filename2), config='--psm 6')
        #     os.remove(filename2)  
            
        
        
        # if text isnt numeric and column = 3
        
        if column == 3:
            if something == True: 
           
                textoutput = PicOutput('ER',gray1,crop_img1)
            else:
            
                textoutput = PicOutput(text1,gray1,crop_img1)
        else:
    
            textoutput = PicOutput(text1,gray1,crop_img1)
        
        return textoutput   
            
     
    
    #############################
    
    
    
    ##########
    #GET Text Main
    #######
    
    
    output1 = Get_Text_From_Coordinates(y1,x1,h1,w1,image,1,0)
    name = output1.finaltext
    
    output2 = Get_Text_From_Coordinates(y2,x2,h2,w2,image,2,0)
    clock = output2.finaltext
    
    # output3 = Get_Text_From_Coordinates(sy1,sx1,sh1,sw1,image,3)
    # seconds = output3.finaltext
    
    
    
    #loop through 270-xxx with intervals of 30
    #generate array
    
    
    
    # output3 = Get_Text_From_Coordinates(sy1,sx1,sh1,sw1,image,3)
    # seconds = output3.finaltext
    
    
    
    milisecs = []
    
    testrange = [150, 170, 100, 160, 130, 90, 120]   
    
    for i in range (420,720,30):   
        # output3 = Get_Text_From_Coordinates(i,sx1,sh1,sw1,image,3,150)    # make argument to repeat with different parameters
        
        # if output3.finaltext == 'ER':
        #     output4 = Get_Text_From_Coordinates(i,sx1,sh1,sw1,image,3,170)
        #     milisecs.append(output4.finaltext[:2])
        
        # else:
        #     milisecs.append(output3.finaltext[:2])
    
    
        for x in testrange[:-1]:  #add more ranges, loop through them
            output3 = Get_Text_From_Coordinates(i,sx1,sh1,sw1,image,3,x) 
            
            if output3.finaltext != 'ER' and output3.finaltext != '':
                milisecs.append(output3.finaltext[:2])
                break
        else:
            output3 = Get_Text_From_Coordinates(i,sx1,sh1,sw1,image,3,testrange[-1])
            milisecs.append(output3.finaltext[:2])
        
        # cv2.imshow("Crop Image Output", output3.finalcrop_img)
        # cv2.imshow("Output", output3.finalgray)
        # cv2.waitKey(0)
    
        
                
    
    
    
    # gray = output2.finalgray
    # crop_img = output2.finalcrop_img
    
    # # #show the output images
    # cv2.imshow("Crop Image Output", crop_img)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)
    
    
    class FinalOutput:
        def __init__(self,name,clock,milisecs):
            self.name = name
            self.clock = clock
            self.milisec = milisecs
    
    
    final = FinalOutput(name,clock,milisecs)
    return final
    
