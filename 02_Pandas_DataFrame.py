import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.rand(6,4),columns=list('ABCD'))
# 數值在 0 到 1 之間 , 6 列 4 行的資料
print(df1)
print('')
#Random Normal distr 隨機常態 分配 , 6 列 4 行的資料
df2 = pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))
print(df2)
print('')
df1 = df1.append(df2,ignore_index=True) # 附加df2 到 df1, 忽略索引
print(df2)
print('')
df1 = df1.drop(list(range(2,8))) # 刪 掉一個範圍的列
print(df2)
print('')
df1 = df1.drop(columns = ['A','D']) # 刪掉 A 欄 跟 D 欄
print(df2)
print('')
df1 = df1.drop(11)  # 刪掉 第 11 列
print(df1)
print('')