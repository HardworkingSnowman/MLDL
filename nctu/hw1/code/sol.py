#! python2
# coding=utf-8
from sklearn.datasets import load_wine
import numpy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

wine=load_wine()

print ('shape:'+str(wine.data.shape))
print ('features:'+str(wine.feature_names))
print ('targets:'+str(wine.target_names))
print ('39th:'+str(wine.data[38])+',\n48th:'+str(wine.data[47])+',\n99th:'+str(wine.data[98])+',\n170th:'+str(wine.data[169]))


columns=[[] for i in range(len(wine.feature_names))]
for column in range(len(wine.feature_names)):
  for row in wine.data:
    columns[column].append(row[column])
for feature in range(len(wine.feature_names)):
  print (wine.feature_names[feature])
  print (str(numpy.min(columns[feature]))+', '+str(numpy.max(columns[feature]))+', '+str(numpy.median(columns[feature]))+', '+str(numpy.mean(columns[feature]))+', '+str(numpy.std(columns[feature])))

for i in range(len(wine.feature_names)):
  print ('feature '+str(i)+ ' alcohol')
  plt.title('feature '+str(i)+' alcohol')
  plt.scatter(wine.target[:59], columns[i][:59], c=['r'])
  plt.scatter(wine.target[59:130], columns[i][59:130], c=['g'])
  plt.scatter(wine.target[130:], columns[i][130:], c=['b'])
  plt.xticks([0, 1, 2], ['class_0', 'class_1', 'class_2'])
  plt.show()
  plt.savefig('Analysis-1.png')
  plt.close()


plt.xlabel('flavanoids')
plt.ylabel('alcohol')
plt.scatter(columns[6][:59], columns[0][:59], c=['r'])
plt.scatter(columns[6][59:130], columns[0][59:130], c=['g'])
plt.scatter(columns[6][130:], columns[0][130:], c=['b'])
plt.show()
plt.savefig('Analysis-2.png')

print '這樣會讓圖的區分比較明顯'
