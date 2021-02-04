import pandas as pd
import numpy as np
#建立ABC欄日期從20200101~20200105的資料,匯入到DataFrame
d = { 'A' : pd.Series(data=np.random.randint(10,30,5),
                      index=pd.date_range('20200101',periods=5)),
'B': pd.Series(data=np.random.randint(50,80,5),
                index=pd.date_range('20200101',periods=5)),
'C': pd.Series(data=np.random.randint(100,150,5),
                index=pd.date_range('20200101',periods=5)) }
df = pd.DataFrame(d, index=pd.date_range('20200101',periods=5))
print(df)
print('')
df['D'] = df['B'] + df['C']
# 欄與欄進行 運算 , 結果產生新的 D 欄 , 附加上去
print(df)
print('')
print(df.loc['20200102':'20200104'])  # 按日期區間擷取
print('')
del df['A']  # 刪除 A 欄
print(df)
print('')