#%%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

#%%
data = pd.read_csv('../11.data/19.data/04.data_interim_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']

feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)
#feature_data = data

#%%
lr = LinearRegression()

#%%
cv = KFold(5, shuffle=True, random_state=0)
cvs = cross_val_score(lr, feature_data, target_data, scoring='neg_mean_absolute_error', cv=cv)
print(cvs.mean())