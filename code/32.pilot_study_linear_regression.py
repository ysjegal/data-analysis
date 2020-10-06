#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

#%%
data = pd.read_csv('../11.data/19.data/04.data_interim_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']

feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)
#feature_data = data

#%%
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data)

#%%
lr = LinearRegression()
lr.fit(X_train, y_train)
result_score = lr.score(X_test, y_test)
print("R-square of Linear Regression")
print("score = %0.6f" %(result_score))

#%%
parameter_list = np.linspace(1,10,100)
score_list = []
score = 0

for i, para in enumerate(parameter_list):
    ridge = Ridge(alpha = para)
    ridge.fit(X_train, y_train)
    result_score = ridge.score(X_test, y_test)
    if i > 1 and result_score > score:
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
l = Lasso()
l.fit(X_train, y_train)
print(l.score(X_test, y_test))

#%%
parameter_list = np.linspace(0,1,10)
score_list = []
score = 0

for i, para in enumerate(parameter_list):
    lasso = Lasso(alpha = para)
    lasso.fit(X_train, y_train)
    result_score = lasso.score(X_test, y_test)
    if i > 1 and result_score > score:
        alpha = para
        score = result_score
    score_list.append(result_score)

plt.plot(parameter_list, score_list)
plt.title('Score of Ridge Regression')
plt.xlabel('Alpha')
plt.ylabel('Score')
plt.show()
print("Highest R-square of Lasso Regression: alpha = %s, score = %s" %(alpha, score))