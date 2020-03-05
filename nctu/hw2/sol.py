#! python3
# coding=utf-8
import numpy as np
import random
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import ComplementNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

dataset=open('car.txt', 'r').read().split('\n')
organize=[]
for data in dataset:
  data_subset=[]
  data=data.split(',')
  for d in data:
    data_subset.append(d)
  organize.append(data_subset)
random.shuffle(organize)
organize=np.array(organize)

# how many cars have 4 doors
count=0
for o in organize:
  if o[2]=='4':
    count+=1
print('4 doors:{0}'.format(count))

# how many cars for each values(unacc,acc,good,vgood)
value=np.zeros(4)
for o in organize:
  if o[6]=='unacc':
    value[0]+=1
  elif o[6]=='acc':
    value[1]+=1
  elif o[6]=='good':
    value[2]+=1
  else:
    value[3]+=1
print('unacc:{0}, acc:{1}, good:{2}, vgood:{3}'.format(value[0], value[1], value[2], value[3]))

# the corresponding labels and target name
le = preprocessing.LabelEncoder()
le.fit(['small', 'low', 'med', 'high', 'vhigh', '2', '3', '4', '5more', 'more', 'unacc', 'acc', 'good', 'vgood', 'big'])
encode=[]
for o in organize:
  e=le.transform(o)
  encode.append(e)
encode=np.array(encode)
print(encode)

# Split dataset to the training dataset and testing dataset
print('the number of testing dataset:{0}'.format(int(len(organize)*0.2)))

test_data=encode[:int(len(organize)*0.2)]
training_data=np.array(encode[int(len(organize)*0.2):])

def method(clf):
  clf.fit(training_data[:, 0:6], training_data[:, -1])
  result=clf.predict(test_data[:, 0:6])
  correct=0
  for i in range(len(result)):
    if(result[i]==test_data[i][-1]):
      correct+=1
  print(correct/float(len(result)))

# Gaussian Naive Bayes' method
clf = GaussianNB()
method(clf)

# Bernoulli Naive Bayes'
clf = BernoulliNB()
method(clf)

# Complement Naive Bayes' method
clf = ComplementNB()
method(clf)

# Multinomial Naive Bayes' method
clf = MultinomialNB()
method(clf)

# confusion matrix of the highest accuracy method
clf = GaussianNB()
clf.fit(training_data[0:, 0:6], training_data[0:, 6])
result=clf.predict(test_data[0:, 0:6])
print(confusion_matrix(test_data[0:, 6], result))
print('acc has the most wrong prediction')

