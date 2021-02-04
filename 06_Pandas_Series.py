import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(5), index= pd.date_range('20200301',periods=5))
# 預設 頻率 為日
print(ts)
print('')
ts = pd.Series(np.random.randn(5), index= pd.date_range('20200301 12:59:30',periods=5))
# 預設 頻率 為日
print(ts)
print('')
pd.date_range('2017-6-27',periods = 7,freq = '1h30min')
ts = pd.Series(np.random.randn(5), index= pd.date_range('20200301 12:59:30','20200306'))
# 頻率為日
print(ts)
print('')
ts = pd.Series(np.random.randn(5), index= pd.date_range('2020-03-01',periods = 5,freq = '1h5min'))
# 頻率為 65T (65 分鐘 )
print(ts)
print('')
ts = pd.Series(np.random.randn(5), index= pd.date_range('2020-02-01',periods=5, freq='M'))
# 頻率為 月 , 顯示每個月最後一天
print(ts)
print('')
ts = pd.Series(np.random.randn(5), index= pd.date_range('2020/03/02',periods=5, freq='W'))
# 頻率為 周 ( 禮拜天為每周第一天 )
print(ts)