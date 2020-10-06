#%%
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import operator
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)

#%%
tr = ExtraTreesRegressor(n_estimators=100, random_state=0)
tr = tr.fit(X_train, y_train)

#%%
cv = KFold(5, shuffle=True, random_state=0)
cvs = cross_val_score(tr, feature_data, target_data, scoring='neg_mean_absolute_error', cv=cv)
print(cvs.mean())