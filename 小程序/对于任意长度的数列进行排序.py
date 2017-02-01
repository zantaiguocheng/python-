# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 20:51:33 2017

@author: kyc11
"""
import ast
a=raw_input('''请按以","分割''')#把数字作为字符型输入
a="["+a+"]"
b=ast.literal_eval(a)#会判断需要计算的内容计算后是不是合法的python类型,并将其转化
for i in range(len(b)-1,0,-1):
    for j in range(i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
print b
