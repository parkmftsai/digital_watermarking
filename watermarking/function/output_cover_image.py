import sys
import os
import numpy
from numpy import zeros
from binascii import hexlify

def output_image(imagename,dwtred,dwtgreen,dwtblue):
    f = open(imagename, "wb")
    for i in range(0,512,+1):
        for j in range(0,512,+1):
           
            try:
                if(dwtred[i,j]>255):
                 dwtred[i,j]=255
                else:
                   if(dwtred[i,j]<0):
                       dwtred[i,j]=0
                f.write(chr(dwtred[i,j]))
                if(dwtgreen[i,j]>255):
                 dwtgreen[i,j]=255
                else:
                   if(dwtgreen[i,j]<0):
                       dwtgreen[i,j]=0

                f.write(chr( dwtgreen[i,j]))
                if(dwtblue[i,j]>255):
                 dwtblue[i,j]=255
                else:
                   if(dwtblue[i,j]<0):
                       dwtblue[i,j]=0

                f.write(chr(dwtblue[i,j]))
            except:
                print  'no',dwtred[i,j]
    f.close()