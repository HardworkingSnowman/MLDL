# coding=utf-8
import csv
import numpy as np
from numpy.linalg import inv
import random
import math
import sys

# 放18個觀測數值，連續放12*20*24個
data=[]
for i in range(18):
  data.append([])

# 把每一行csv讀進來
n_row=0 # 第幾行，第一行沒要的東西
text=open('01-Data/train.csv', 'r')
row=csv.reader(text, delimiter=',')
for r in row:
  if n_row!=0:
    for i in range(3, 27):
      # 有的雨量會填NR表示沒下雨
      if r[i]!='NR':
        data[(n_row-1)%18].append(float(r[i]))
      else:
        data[(n_row-1)%18].append(float(0))
  n_row+=1
text.close()

# x存每個月的每天的每十小時中的1~9小時的所有物質的數值; y存每個月的每天的每十小時中的第10小時的PM值
x=[]
y=[]
# 每個月
for i in range(12):
  # 每個月會有471個十小時。因為一個月20天，每天24小時，總共480小時，1~10, 2~11, 3~12,......, 471~480
  for j in range(471):
    x.append([])
    # 18種物質
    for t in range(18):
      # 每個十小時的前9小時
      for s in range(9):
        x[471*i+j].append(data[t][480*i+j+s])
    y.append(data[9][480*i+j+9])

# 把x變成維度為 [12*471, 9*18] 的矩陣; y則是 [1, 12*471]
x=np.array(x)
y=np.array(y)

# 在x的每一row的最前面放1，那個是bias，也就是y=wx+b的常數b
x=np.concatenate((np.ones((x.shape[0], 1)), x), axis=1)

# 初始化weight, learning rate, repeat
# 把所有weight初始為0，維度 [1, 9*18+1]
w=np.zeros(len(x[0]))
l_rate=10
# 最多做repeat次(怕永遠沒結果)
repeat=10000

# 開始training
x_t=x.transpose()
s_gra=np.zeros(len(x[0]))
rate_mod=np.zeros(len(x[0]))
for i in range(repeat):
  # hypo是預測的y
  hypo=np.dot(x, w)
  # loss是預測的y-真正的y
  loss=hypo-y
  # cost才是真正的Loss function
  cost=np.sum(loss**2)
  # 分別對每個w做偏微分
  gra=2*np.dot(x_t, loss)
  # 調整learning rate
  rate_mod+=np.abs(gra)**2
  # 更新weight
  w=w-l_rate*gra/np.sqrt(rate_mod)
print(w)

# 開始test
n_row=0
text=open('01-Data/test.csv', 'r')
row=csv.reader(text, delimiter=',')
data_x=[]
for r in row:
  if n_row%18==0:
    data_x.append([])
  for i in range(2, 11):
    if r[i] !='NR':
      data_x[n_row/18].append(float(r[i]))
    else:
      data_x[n_row/18].append(float(0))
  n_row+=1
text.close

data_x=np.array(data_x)
data_x=np.concatenate((np.ones((data_x.shape[0], 1)), data_x), axis=1)

answer=[]
for i in range(len(data_x)):
  answer.append(['id_'+str(i)])
  answer[i].append(np.dot(data_x[i], w))

text=open('answer/predict.csv', 'w+')
s=csv.writer(text, delimiter=',', lineterminator='\n')
s.writerow(['id', 'value'])
for i in range(len(answer)):
  s.writerow(answer[i])
text.close()