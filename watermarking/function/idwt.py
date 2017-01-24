import sys
import os
import numpy
from PIL import Image
from numpy import zeros
from binascii import hexlify
import math
import random
import dwt

def idwt(TEMP2,pixel,width, height):
    #blue1 = zeros((512,512),int) 
    for j in range(0,width,+1):
        ct = 0;
        for i in range(0,height/2,+1):      
            tmp = (TEMP2[i + (height / 2),j]) + 1;
            if ((tmp < 0 or tmp == (-1) or tmp / 2 == (-1)) and ((TEMP2[i + (height / 2),j] + 1) % 2) != 0):
                pixel[ct,j] =TEMP2[i,j] + (tmp / 2 - 1)
            else:
                pixel[ct,j] =TEMP2[i,j] + tmp / 2

            pixel[ct + 1, j] = pixel[ct, j] - TEMP2[i + (height / 2), j];
            ct += 2;
                 
        
    for i in range(0,width,+1):
        ct = 0;
        for j in range(0,height/2,+1):  
                
            tmp = (pixel[i,j + (width / 2)]) + 1;
            if ((tmp < 0 or tmp == (-1) or tmp / 2 == (-1)) and((pixel[i,j + (width / 2)] + 1) % 2) != 0):
                TEMP2[i,ct] = pixel[i,j] + (tmp / 2 - 1)
            else:
                TEMP2[i,ct] = pixel[i,j] + tmp / 2

            TEMP2[i,ct + 1] = TEMP2[i,ct] - pixel[i,j + (width / 2)]
            ct += 2

