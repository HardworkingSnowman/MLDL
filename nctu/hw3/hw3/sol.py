import pandas as pd

df=pd.read_json('./data.json')

print(df[df['id']==1])
# print(data['cuisine'])
print(df.index)