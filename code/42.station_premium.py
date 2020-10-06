#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

#%%
gu_list = ['강서구', '양천구', '구로구', '영등포구', '동작구', '금천구', '관악구', '서초구', '강남구', '송파구', '강동구', '마포구', '용산구', '성동구', '광진구', '은평구', '서대문구', '중구', '종로구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구']
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)

#%%
"""
모델 생성
모델 학습
"""

#%%
gu_price = pd.DataFrame()
for gu in gu_list:
    gu_price[gu] = np.exp(y_test.loc[X_test.loc[X_test[gu]==1].index]).describe()
    
#%%
nearest_building = X_test.loc[X_train['신사']==X_test['신사'].min()]

matrix = []
for feature in nearest_building.columns:
    matrix.append([nearest_building[feature]]*100)

X_station = pd.DataFrame(matrix, columns=nearest_building.columns)
    
new_dist = np.range(1, 101)
new_dist = new_dist*100

# 여기에다가 분석하고싶은 지하철역 이름 적으면 되욤
X_station['신사'] = new_dist

#%%

