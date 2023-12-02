#quant_test
#퀀트 투자 포트 폴리오 만들기
#https://github.com/hyunyulhenry/quant_py

import seaborn as sns
import pandas as pd
#iris = sns.load_dataset('iris')

dic_data = {'a' : 1, 'b' : 2, 'c' : 3}
series = pd.Series(dic_data)

print(series)
print(type(series))
print(series.index)
print(series.values)

dic_dataframe = {'col_1' : [0, 1, 2, 3, 4], 'col_2' : [10, 11, 12, 13, 14]}
df = pd.DataFrame(dic_dataframe, index=['index1', 'index2', 'index3', 'index4', 'index5'])
print(df)

df.columns = ['c1', 'c2']
df.index = ['0', '1', '2', '3', '4']
print(df)
print(df['c1'])

d = df.c1
print(d)

data_csv = pd.read_csv('kospi.csv')

df2 = sns.load_dataset('titanic')

print(df2)
