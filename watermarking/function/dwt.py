import sys
import os
import numpy
from PIL import Image
from numpy import zeros
from binascii import hexlify
import math
import random
def dwt(blue,width, height):
    """----------DWT------------------------"""
    TEMP1 = zeros((512,512),int)
    TEMP2 = zeros((512,512),int)
    for i in range(0,height,+1):
        for j in range(0,width/2,+1):  
            tmp = (blue[i,j*2] + blue[i,j * 2 + 1])
            if((tmp < 0 or (tmp == (-1) or tmp / 2 == (-1))) and ((blue[i,j * 2] + blue[i,j * 2+1]) % 2) != 0):        
                TEMP1[i,j] = tmp / 2 - 1;
            else:
                TEMP1[i,j] = tmp / 2;

        ct = width / 2;
        for j in range(0,width/2,+1): 
            TEMP1[i,ct] = (blue[i,j * 2] - blue[i,j * 2 + 1]);
            ct+=1
                     
                     
                     
    for j in range(0,width,+1):
        for i in range(0,height/2,+1):      
        
            tmp = (TEMP1[i * 2,j] + TEMP1[i * 2 + 1,j]);
        
            if ((tmp < 0 or tmp == (-1) or tmp / 2 == (-1)) and ((TEMP1[i * 2,j] + TEMP1[i * 2 + 1,j]) % 2) != 0):
                TEMP2[i,j] = tmp / 2 - 1;
            else:
                TEMP2[i,j] = tmp / 2;
              
        ct = height/ 2;
    
        for i in range(0,height/2,+1): 
                
            TEMP2[ct,j] = (TEMP1[i * 2,j] - TEMP1[i * 2 + 1,j]);
            ct+=1
    return TEMP2
    