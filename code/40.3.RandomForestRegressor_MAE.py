#%%
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.model_selection import train_test_split

#%%
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

# tr = RandomForestRegressor(n_estimators=100, random_state=0)
tr = RandomForestRegressor(n_estimators=100, random_state=1)
tr.fit(X_train, y_train)

cv = KFold(5, shuffle=True, random_state=0)
cvs = cross_val_score(tr, feature_data, target_data, scoring='neg_mean_absolute_error', cv=cv)
print(cvs.mean())
