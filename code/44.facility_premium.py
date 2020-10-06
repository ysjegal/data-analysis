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

#%% 구 별 주택가격의 표준편차 확인 -> 금천구, 중랑구가 작게 나옴!
gu_list = ['강서구', '양천구', '구로구', '영등포구', '동작구', '금천구', '관악구', '서초구', '강남구', '송파구', '강동구', '마포구', '용산구', '성동구', '광진구', '은평구', '서대문구', '중구', '종로구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구']
gu_price = pd.DataFrame()
for gu in gu_list:
    gu_price[gu] = np.exp(y_test.loc[X_test.loc[X_test[gu]==1].index]).describe()
    
#%%
feature_list = ['영화관_2nd','대형마트_2nd','학문/교육','유치원_1st','대학교_1st','치안기관_1st']
y_predict_list = []
y_max_list = []
y_min_list = []
target_gu = gu

for feature in feature_list:
    X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)
    X_train, X_original, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)
    X_train, X_max, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)
    X_train, X_min, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)

    X_original = X_test.loc[X_test[gu]==1]
    X_max = X_test.loc[X_test[gu]==1]
    X_min = X_test.loc[X_test[gu]==1]
    y_test = y_test.loc[X_test.loc[X_test[gu]==1].index]
    
    y_predict_list.append(np.exp(tr.predict(X_original)).mean())
    
    max_value = X_original[feature].max()
    min_value = X_original[feature].min()
    
    X_max[feature] = np.array([max_value]*len(X_original))
    y_max_list.append(np.exp(tr.predict(X_max)).mean())
    
    X_min[feature] = np.array([min_value]*len(X_original))
    y_min_list.append(np.exp(tr.predict(X_min)).mean())
    
df = pd.DataFrame([feature_list, y_min_list, y_predict_list, y_max_list])
df = df.T
df.columns=['변수명','최소','실제','최대']
df.to_csv('../11.data/60.premium/00.premium.csv', encoding='cp949', index=False)