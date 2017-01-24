import sys
import os
import numpy
from numpy import zeros
from binascii import hexlify


def input_file(fillname):

    file=open(fillname,'rb')
    flag=0
    red   = zeros((512,512),str)
    green   = zeros((512,512),str)
    blue = zeros((512,512),str)
    try:
        byte = file.read(1)
        while byte != "":
            for i in range(0,512,+1):
                for j in range(0,512,+1):  
                    
                    red[i,j]=byte
                  
                    hex = hexlify(red[i,j])
                    byte = file.read(1)
            
          
                    
                    green[i,j]=byte
                    hex = hexlify(green[i,j])
                    byte = file.read(1)
                    
                    blue[i,j]=byte
                    hex = hexlify(blue[i,j])
                    byte = file.read(1)   
                             
    finally:
        file.close()
    return red,green,blue;