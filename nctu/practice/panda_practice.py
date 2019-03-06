#! python2
# coding=utf-8
import pandas as pd

f=pd.read_csv("https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv")
# print type(f)
# print 'f.shape:{0}'.format(f.shape)
# print 'f.columns:{0}'.format(f.columns)
# print 'f.index:{0}'.format(f.index)
# f.info()
# print f.describe()

# SELECT
print f[['continent', 'year']]

# WHERE
print f[(f['country']=='Afghanistan') & (f['year']>1970)]

print f['country'].apply(lambda x:x[:3])

print f['pop'].sum()

print f['pop'].mean()