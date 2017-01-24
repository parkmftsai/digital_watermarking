import sys
import os
import numpy
from numpy import zeros
from binascii import hexlify

def process_data(charimage):
    pixel = zeros((512,512),int)
    for i in range(0,256,+1):
        for j in range(0,256,+1):
            try:

                hex = hexlify(charimage[i,j])
                if(hex==''):
                    pixel[i,j] =34
                else:
                    pixel[i,j] =int(hex,16)
               
                
                hex = hexlify(charimage[i,256+j])
                if(hex==''):
                     pixel[i,256+j] =34
                else:
                    pixel[i,256+j] =int(hex,16)
            
              
                hex = hexlify(charimage[256+i,j])
                if(hex==''):
                    pixel[256+i,j] =34
                else:
                    pixel[256+i,j] =int(hex,16)
                hex = hexlify(charimage[256+i,256+j])
                if(hex==''):
                    pixel[256+i,256+j] =34
                else:
                    pixel[256+i,256+j] =int(hex,16)
               
                
            except:
                k=0
    return pixel


    

