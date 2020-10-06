#%%
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
import operator
import matplotlib.pyplot as plt
import pickle

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)

#%%
reg_ensemble = VotingRegressor([('rf',RandomForestRegressor(n_estimators=100, random_state=1)), 
                                ('etr',ExtraTreesRegressor(n_estimators=100, random_state=0))])

#%%
reg_ensemble.fit(X_train, y_train)

#%%
y_pred = reg_ensemble.predict(X_test)

#%%
mean_absolute_error(y_test, y_pred)