import os
import numpy
from PIL import Image
from numpy import zeros
from binascii import hexlify
import math
import random

def extract_watermark(TEMP2,width,height,complex):
    outdata = Image.new("RGB",( 256,256))
    outputwm = zeros((256*256),int)
    
    order= zeros((256*256),int)
    tmp= zeros((256*256),int)
    u=256
    k=5

    """---------getting data----------"""
    
    position_pixel=0

    for i in range(height / 2,height,+1):
        for j in range(width / 2,width,+1):
            p=math.fabs(TEMP2[i, j])
            k=p%10
                         
            outputwm[position_pixel]=p%10

            p=int(p/10)
            if(p%2==0):
                outputwm[position_pixel]=9+outputwm[position_pixel];

            outputwm[position_pixel]=math.pow(outputwm[position_pixel]+complex[position_pixel],2)
 
            
            if(outputwm[position_pixel]>255 and(k>=7 and k<10) ):
                outputwm[position_pixel]=math.pow(k+complex[position_pixel],2)
            if(outputwm[position_pixel]>sum):
               outputwm[position_pixel]=outputwm[position_pixel]

            else:
               outputwm[position_pixel]=outputwm[position_pixel]
           
            position_pixel+=1 

 
    random.seed(12)     
    for i in range(0,position_pixel,+1):
         order[i] = i
         
    
    random.shuffle(order)

    for i in range(0,position_pixel,+1):
         tmp[order[i]]= outputwm[i]
    
    for i in range(0,position_pixel,+1):
        outputwm[i] = tmp[i];
            
    return outputwm