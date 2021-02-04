import pandas as pd
#建立一個不完整的字典資料,3列4行
data = [{'A': 1, 'B': 2}, {'A': 5, 'B': 10, 'C': 20}, {'B':20,'C':5,'D':22}]
df = pd.DataFrame(data,columns=list('ABCD'),index=['r0','r1','r2'])
print(df)
print('')
print(df.loc['r0']) # 指定第 r0 列 , 切出來
print('')
print(df.iloc[1]) #iloc 指定列的索引值, 指定第 1 列 , 切出來
print('')
print(df['B'])  # 指定第 B 欄 , 切出來
print('')
print(df.loc['r1':'r2', 'C':'D'])  # 同時 指定 列與欄的範圍 , 切出來
print('')
print(df.shape)