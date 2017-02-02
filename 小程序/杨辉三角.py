# -*- coding: utf-8 -*-

'''Spyder Editor

This is a temporary script file.'''


import numpy as np#调用numpy
k=input()
x=np.zeros((k,k))#生成由0填充的k*k阶矩阵
for i in range(k):
    for j in range(i+1):
        if j==0:
            x[i][j]=1
        else:
            x[i][j]=x[i-1][j]+x[i-1][j-1]
        
print x
end