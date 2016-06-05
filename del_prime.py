#!/usr/bin/env python
#coding:utf-8
import math


def fil(n):    #定义fil函数
    '''return 1-100 prime'''
    flag = 0    #设置flag
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:    #判断是否是素数
            flag = 1     #如果不是，flag设为1
            break        #break
    if flag == 1:        #退出循环判断flag，若为1（即不是素数），则返回其值
        return n

print filter(fil, range(1,101))    #filter 1-100里的素数

#另一种方法，代码量少，计算量多：

def fil(x):
    for y in range(2,x):
        if x%y==0:
            return True
    return False
print filter(fil,range(2,101))



