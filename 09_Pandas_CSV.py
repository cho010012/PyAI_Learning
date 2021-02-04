import pandas as pd
df = pd.read_csv('https://bit.ly/uforeports')
print(df.columns)
print('')
print(df.count()) # 每個欄位累計筆數 不含 NAN
print('')
df1 =df[df.City.isnull()]
print(df1)  # 列出 City 缺 值 的資料
print('')
print(len(df1)) # 列出 City 缺 值 的列數
print('')
#撈取第0,3,4欄位的值
# df = pd.read_csv('https://bit.ly/uforeports', usecols=[0,3,4])
print(df.head(5)) #先列出頭5筆
