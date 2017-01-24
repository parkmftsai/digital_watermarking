#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;
extern "C"
{
    __declspec(dllexport) void trance(int* a,int k);
    __declspec(dllexport) void dwt(int* a,int width,int height);
    __declspec(dllexport) void input_file(char dataname[],int* red,int* green,int* blue,int width,int height);
    __declspec(dllexport) void output_file(char dataname[],int* red,int* green,int* blue,int width,int height);
}

