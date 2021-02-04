#coding:utf-8
import pandas as pd
s = pd.Series([3,5,6,0,2])
print(s)
s = pd.Series([3,5,6,0,2] ,index=range(20,25)) #自訂索引範圍 print(s)
#自訂索引名稱
s = pd.Series([3,5,6,0,2] ,index=['a','b','c','d','e'])
print(s)
data = {'a' : 0., 'b' : 1., 'c': 2.}
#準備字典資料 s = pd.Series(data) print(s)
s = pd.Series(data,index=['b','a','d','c'])
print(s)
print(s['b'])
