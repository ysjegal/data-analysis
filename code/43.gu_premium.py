#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)

#%%
tr = ExtraTreesRegressor(n_estimators=100, random_state=0)
tr = tr.fit(X_train, y_train)

#%%
gu_list = ['강서구', '양천구', '구로구', '영등포구', '동작구', '금천구', '관악구', '서초구', '강남구', '송파구', '강동구', '마포구', '용산구', '성동구', '광진구', '은평구', '서대문구', '중구', '종로구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구']
X_train, X_gangnam, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)

#%%
for gu in gu_list:
    X_gangnam[gu] = [0]*len(X_test)
    
X_gangnam['송파구'] = [1]*len(X_test)

#%%
y_gangnam = tr.predict(X_gangnam)

#%%
y_gangnam = pd.Series(y_gangnam)
y_gangnam.index = X_test.index

#%%
y_predict = tr.predict(X_test)

#%%
y_predict = pd.Series(y_predict)
y_predict.index = X_test.index

#%%
price_difference = []
for gu in gu_list:
    price_difference.append(np.exp(y_gangnam.loc[X_test.loc[X_test[gu]==1].index]).mean() - np.exp(y_test.loc[X_test.loc[X_test[gu]==1].index]).mean())
  
#%%
df = pd.DataFrame([gu_list, price_difference])
df = df.T
df.columns=['자치구','가격차']
df.to_csv('../11.data/60.premium/01.songpa_premium.csv', encoding='cp949', index=False)