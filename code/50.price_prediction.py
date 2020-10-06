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
X_test.iloc[0]

#%%
np.exp(tr.predict(np.array(X_test.iloc[0]).reshape(1,-1)))

#%%
X_trans = X_test.iloc[0]

#%%
X_trans[342] = 1000
X_trans[343] = X_test.iloc[0]['영화관_1st']
X_trans[344] = X_test.iloc[0]['영화관_2nd']

#%%
np.exp(tr.predict(np.array(X_trans).reshape(1,-1)))

#%%
X_trans_1 = X_test.iloc[0]

#%%
X_trans_1[345] = 500
X_trans_1[346] = X_test.iloc[0]['백화점_1st']
X_trans_1[347] = X_test.iloc[0]['백화점_2nd']

#%%
np.exp(tr.predict(np.array(X_trans_1).reshape(1,-1)))

#%%
np.exp(tr.predict(np.array(X_test.iloc[-1]).reshape(1,-1)))