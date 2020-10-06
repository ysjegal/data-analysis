#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

#%%
data = pd.read_csv('../11.data/19.data/04.data_interim_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']

feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)
#feature_data = data

#%%
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, random_state=1)

#%%
parameter_list = np.linspace(1,10,100)
score_list = []
score = 0

for i, para in enumerate(parameter_list):
    ridge = Ridge(alpha = para)
    ridge.fit(X_train, y_train)
    result_score = ridge.score(X_test, y_test)
    if result_score > score:
        alpha = para
        score = result_score
    score_list.append(result_score)

plt.plot(parameter_list, score_list)
plt.title('Score of Ridge Regression')
plt.xlabel('Alpha')
plt.ylabel('Score')
plt.show()
print("Highest R-square of Ridge Regression")
print("alpha = %0.6f" %(alpha))
print("score = %0.6f" %(score))

#%%
rd = Ridge(alpha = 3.72727)
cv = KFold(5, shuffle=True, random_state=0)
cvs = cross_val_score(rd, feature_data, target_data, scoring='neg_mean_absolute_error', cv=cv)
print(cvs.mean())