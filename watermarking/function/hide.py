import sys
import os
import numpy
from PIL import Image
from numpy import zeros
from binascii import hexlify
import math
import random



def hiding_data(TEMP2,filename,complex,flag,writedata):
    width=512
    height=512
    outdata = Image.new("RGB",( 256,256))
    outputwm = zeros((256*256),int)
    wm_pixel = zeros((256*256),int)
    watermark=Image.open(filename)
    mk=watermark.load()
    wm_width,wm_height=watermark.size;
 
    u=256
    k=5

    position_pixel=0
    for i in range(0,wm_height,+1):
        for j in range(0,wm_width,+1):        
                wm_pixel[position_pixel]=int(mk[i,j][flag])
                position_pixel+=1
    
    random.seed(12)
    random.shuffle(wm_pixel)
    
 
    position_pixel=0
    for i in range(height / 2,height,+1):
        for j in range(width / 2,width,+1): 
            a=math.fabs(TEMP2[i, j])
            
            flag=1
          
            if(TEMP2[i, j]<0):
              flag=-1
           
            diwm=round(math.sqrt(wm_pixel[position_pixel]))
            complex[position_pixel]=math.sqrt(wm_pixel[position_pixel])-diwm
    
            if(diwm>=10):
                g = a - (a%10) 
                p=g/10
                if(p%2==1):
                    g=g-10+(diwm/10) + (diwm%10)
                else:
                    g=g+(diwm/10) + (diwm%10)
                
            else:
                g = a - (a%10) 
                p=g/10
                if(p%2==0):
                    if(g==240):
                        g=g-20
                    g=g+10+diwm
                else:
                    g=g+diwm 
                 
            g=g*flag
        
            if(writedata):
                TEMP2[i, j]=g

         
            position_pixel+=1
  
    print("the message has been hided" )

    
