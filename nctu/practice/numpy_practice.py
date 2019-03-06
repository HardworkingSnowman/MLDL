#! python2
# coding=utf-8
import numpy as np

a=np.array([[1,2,3], [4,5,6]])
b=np.array([[1,3], [5,2], [4,6]])
print np.dot(a,b)

c=np.array([[1,3,5], [2,4,6]])
print a*c

print 'a.ndim:{0}'.format(a.ndim)
print 'a.shape:{0}'.format(a.shape)
print 'a.dtype:{0}'.format(a.dtype)
print 'a.itemsize:{0}'.format(a.itemsize)

print 'np.zeros(3, 5):{0}'.format(np.zeros((3, 5)))
print 'np.ones(3, 5):{0}'.format(np.ones((3, 5)))
print 'np.empty(2, 6):{0}'.format(np.empty((2, 6)))

# 從1~100的等差數列
print 'np.arange(1, 100, 3):{0}'.format(np.arange(1, 100, 3))

# 從1~100等切200段
print 'np.linspace(1, 100, 200):{0}]'.format(np.linspace(1, 100, 200)) 
