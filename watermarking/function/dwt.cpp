/* Replace "dll.h" with the name of your header */
#include "dwt.h"
#include <windows.h>
#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#include <iostream>
#include<string.h>


using namespace std;

short TEMP1[512][512]={0}; 
short TEMP2[512][512]={0};
__declspec(dllexport) void trance(int* a,int k)
{

    for(int i=0;i<k;i++)
       for(int j=0;j<k;j++)
            a[i*k+j]=i*k+j;
}

__declspec(dllexport) void input_file(char dataname[],int* red,int* green,int* blue,int width,int height)
{
    
      int i,j;
      FILE *fi;
      fi = fopen(dataname, "rb"); 
      for(i = 0; i < width; i++){
         for(j = 0; j < height; j++){
            red[(i*width)+j] = (int) fgetc(fi);
         }
      }
     
      for(i = 0; i < width; i++){
         for(j = 0; j < height; j++){
            green[(i*width)+j] = (int) fgetc(fi);
         }
      }
      
      
      for(i = 0; i < width; i++){
         for(j = 0; j < height; j++){
            blue[(i*width)+j] = (int) fgetc(fi);
         }
      }
      fclose(fi); 
}
__declspec(dllexport) void output_file(char dataname[],int* red,int* green,int* blue,int width,int height)
{
    
      int i,j;
      FILE *fo;
      fo = fopen(dataname, "wb"); 
      for(i = 0; i < width; i++){
         for(j = 0; j < height; j++){
             if(red[(i*width)+j]>255)
               red[(i*width)+j]=255;
             else if(red[(i*width)+j]<0)
               red[(i*width)+j]*=-1;
               
            fputc(red[(i*width)+j],fo);
         }
      }
     
      for(i = 0; i < width; i++){
         for(j = 0; j < height; j++){
            if(green[(i*width)+j]>255)
               green[(i*width)+j]=255;
             else if(green[(i*width)+j]<0)
               green[(i*width)+j]*=-1;
            fputc(green[(i*width)+j],fo);
         }
      }
      
      
      for(i = 0; i < width; i++){
         for(j = 0; j < height; j++){
            if(blue[(i*width)+j]>255)
               blue[(i*width)+j]=255;
             else if(blue[(i*width)+j]<0)
               blue[(i*width)+j]*=-1;
            fputc(blue[(i*width)+j],fo);
         }
      }
      fclose(fo); 
}

__declspec(dllexport) void dwt(int* a,int width,int height)
{
    
    int tmp,aval;
  
    for(int i=0;i<height;i++)
       for(int j=0;j<width/2;j++){
            tmp=a[(i*width)+(j*2+1)]-a[(i*width)+(j*2)];
            TEMP1[i][width/2+j]=tmp;
            aval=(int)floor((double)tmp/2);
            tmp=a[(i*width)+(j*2)]+aval;
            TEMP1[i][j]=tmp;
       }
    
    for(int j=0;j<width;j++)
       for(int i=0;i<height/2;i++){
            tmp=TEMP1[i*2+1][j]-TEMP1[i*2][j];
            TEMP2[height/2+i][j]=tmp;
            aval=(int)floor((double)tmp/2);
            tmp=TEMP1[i*2][j]+aval;
            TEMP2[i][j]=tmp;
    
       }
    
     for(int i=0;i<width;i++)
       for(int j=0;j<height;j++){
            a[(i*height)+j]=TEMP2[i][j];
       }
printf("\ndwt end\n");
}
