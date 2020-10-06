#%%
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.linear_model import Lasso
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import pickle

from sklearn.model_selection import train_test_split

#%%
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

#%%
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, random_state=1)

#%%
"""
ls = Lasso(alpha=0.000056)

#%%
print(ls.score(X_test, y_test))

#%% importance가 어떻게 산출되는지 알아볼 것! (높을수록 중요한 feature)
coef_dict = {feature: coef for feature, coef in zip(feature_data.columns, ls.coef_)}
sorted_coef_dict =  sorted(coef_dict.items(), key=operator.itemgetter(1))

#%%
with open('../11.data/40.2.Lasso.pickle', 'wb') as w:
    pickle.dump(sorted_coef_dict, w)
"""

#%% 
"""
alpha = 5.6e-05에서 최고 score (score=0.6884, random_state=1)
train_test_split의 random_state를 바꿔가면서 높은 score 찾기!
"""

"""
parameter_list = np.linspace(0.000001,0.0001,10)
score_list = []
score = 0

for i, para in enumerate(parameter_list):
    print("iteration ", i, ": ", para)
    lasso = Lasso(alpha = para)
    
    cv = KFold(5, shuffle=True, random_state=1)
    cvs = cross_val_score(lasso, feature_data, target_data, scoring=None, cv=cv)
    
    if cvs.mean() > score:
        alpha = para
        score = cvs.mean()
        
    score_list.append(cvs.mean())

plt.plot(parameter_list, score_list)
plt.title('Score of Lasso Regression')
plt.xlabel('Alpha')
plt.ylabel('Score')
plt.show()
print("Highest R-square of Lasso Regression: alpha = %s, score = %s" %(alpha, score))
"""


#%%
lasso = Lasso(alpha = 0.0000056)
lasso.fit(X_train, y_train)

#%%
coef_dict = {feature: coef for feature, coef in zip(feature_data.columns, lasso.coef_)}

#%%
sorted_coef_dict =  sorted(coef_dict.items(), key=operator.itemgetter(1))

#%%
sorted_feature = []
sorted_coef = []

for feature, coef in sorted_coef_dict:
    sorted_feature.append(feature)
    sorted_coef.append(coef)

#%%
plt.figure(figsize=(30,10))

y_pos = np.arange(len(sorted_coef))
plt.bar(y_pos, sorted_coef, align='center', alpha=0.5)
plt.title('Coef. of Features')

plt.savefig('../11.data/LASSO_coef')

#%% 
plt.figure(figsize=(30,10))

#y_pos = np.arange(len(sorted_coef))
y_pos = np.arange(25)
plt.bar(y_pos, sorted_coef[-25:], align='center', alpha=0.5)
.
plt.xticks(y_pos, sorted_feature[-25:])
plt.title('Positive Coef. Features')

plt.show()
#plt.savefig('../11.data/LASSO_positive_coef')

#%%
plt.figure(figsize=(30,10))

#y_pos = np.arange(len(sorted_coef))
y_pos = np.arange(25)
plt.bar(y_pos, sorted_coef[:25], align='center', alpha=0.5)
plt.xticks(y_pos, sorted_feature[:25])
plt.title('Negative Coef. Features')

plt.show()
#plt.savefig('../11.data/LASSO_negative_coef')
