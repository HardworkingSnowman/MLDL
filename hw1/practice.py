# coding=utf-8
import numpy as np
import math

np1=np.array([[1,2,3],[3,4,5]])
np2=np.array([[6,7],[8,9],[1,2]])
print('np1.ndim:'+str(np1.ndim)+', np1.shape:'+str(np1.shape)+', np1.dtype:'+str(np1.dtype))

#下面改不了QAQ
np1.reshape([3, 2])
np1.astype('float')
print(np1.shape[0])

np3=np.ones((3,2))
print(np3)

np4=np.zeros(3)
print(np4)

np5=np.array([[4,5],[6,7],[8,9]])
print(np.dot(np1, np4))

print(np.sum(np2))

print(np2**2)

print(len(np2))

np6=np.array([[float(3),2,1],[1,2,3]])
print(np1/np6)