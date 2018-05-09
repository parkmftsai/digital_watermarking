"""
As long as you retain this notice 
you can do whatever with this stuff ,just you want. 
If we meet some day, and you think this stuff is worth it, 
you can buy me a beer in return park tsai  and share your idea with me .
Let us change the world
"""
import sys

import os
from PIL import Image
from numpy import zeros
from ctypes import *
from function.input_file import input_file
from function.process_data import process_data
from function.dwt import dwt
from function.idwt import idwt
from function.hide import hiding_data
from function.extract import extract_watermark
from function.output_cover_image import output_image


if __name__=="__main__":

    red   = zeros((512,512),str)
    green   = zeros((512,512),str)
    blue = zeros((512,512),str)

  

    pixelred = zeros((512,512),int)
    pixel= zeros((512,512),int)
    pixelgreen = zeros((512,512),int)
    pixelblue = zeros((512,512),int)
    
    

    dwtred = zeros((512,512),int)
    dwtgreen = zeros((512,512),int)
    dwtblue = zeros((512,512),int)

   

    red_wm   = zeros((256*256),int)
    green_wm   = zeros((256*256),int)
    blue_wm = zeros((256*256),int)

    
   
    complex1= zeros((256*256),float)
    complex2= zeros((256*256),float)
    complex3= zeros((256*256),float)
    file_process = CDLL(".\\function\\dwt.dll")
    

    filename="kuas1.jpg"
    hostfilename="OMG_Goldhill_RGB_n.raw"
    outdata = Image.new("RGB",( 256,256))
    width=512
    height=512
    c_s = c_char_p()
    c_s.value = hostfilename
    file_process.input_file(c_s,c_void_p(pixelred.ctypes.data),c_void_p(pixelgreen.ctypes.data),c_void_p(pixelblue.ctypes.data),width,height)
    
    
    dwtred=dwt(pixelred,width, height)
    dwtgreen=dwt(pixelgreen,width, height)
    dwtblue=dwt(pixelblue,width, height)
   
    
    hiding_data(dwtred,filename,complex1,0,bool(1))
    hiding_data(dwtgreen,filename,complex2,1,bool(1))
    hiding_data(dwtblue,filename,complex3,2,bool(1))
    print 'The process of Embed from host image is end!!!!!!!!!'
   

    idwt(dwtred, pixel,width, height)
    idwt(dwtgreen, pixel,width, height)
    idwt(dwtblue, pixel,width, height)



    c_s1 = c_char_p()
    c_s1.value = "lenanew_TEST.raw"
    file_process.output_file(c_s1,c_void_p(dwtred.ctypes.data),c_void_p(dwtgreen.ctypes.data),c_void_p(dwtblue.ctypes.data),width,height)

  



    c_s = c_char_p()
    c_s.value ="lenanew_TEST.raw"
    file_process.input_file(c_s,c_void_p(pixelred.ctypes.data),c_void_p(pixelgreen.ctypes.data),c_void_p(pixelblue.ctypes.data),width,height)
    print "ok"
  

    
    dwtred=dwt(pixelred,width, height)
    dwtgreen=dwt(pixelgreen,width, height)
    dwtblue=dwt(pixelblue,width, height)

    red_wm=extract_watermark(dwtred,width,height,complex1)
    green_wm=extract_watermark(dwtgreen,width,height,complex2)
    blue_wm=extract_watermark(dwtblue,width,height,complex3)
    position_pixel=0

    for i in range(0,256,+1):
        for j in range(0,256,+1):      
            outdata.putpixel((i,j),(red_wm[position_pixel],green_wm[position_pixel],blue_wm[position_pixel]))
            position_pixel+=1

    outdata.save("out_watermarking(output).bmp")

    idwt(dwtred, pixel,width, height)
    idwt(dwtgreen, pixel,width, height)
    idwt(dwtblue, pixel,width, height)
    
    print 'The process of extracting from covered image process is end!!!!!!!!'

