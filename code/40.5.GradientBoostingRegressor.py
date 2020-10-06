#%%
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import operator
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

#%%
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, random_state=1)

#%%
gbr = GradientBoostingRegressor(n_estimators=100, random_state=1)
gbr = gbr.fit(X_train, y_train)

#%%
print(gbr.score(X_test, y_test))

#%% importance가 어떻게 산출되는지 알아볼 것! (높을수록 중요한 feature)
importance_dict = {feature: importance for feature, importance in zip(feature_data.columns, gbr.feature_importances_)}
sorted_coef_dict =  sorted(importance_dict.items(), key=operator.itemgetter(1))

#%%
with open('../11.data/40.ExtraTreeRegressor.pickle', 'wb') as w:
    pickle.dump(sorted_coef_dict, w)
    
#%%
"""
cv = KFold(5, shuffle=True, random_state=0)
cvs = cross_val_score(gbr, feature_data, target_data, scoring='neg_mean_absolute_error'', cv=cv)
print(cvs.mean())
"""