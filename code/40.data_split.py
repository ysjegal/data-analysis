#%%
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.preprocessing import StandardScaler

#%%
data = pd.read_csv('../11.data/19.data/05.data_final.csv', encoding='cp949', index_col=0)

#%%
target_data = data['평균 거래금액 (로그 스케일)']
feature_data = data.drop(['평균 거래금액 (로그 스케일)'], axis=1)

#%%
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, shuffle = True, random_state=2)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, shuffle = True, random_state=2)

#%%
print(X_train.shape)
print(y_train.shape)
print()
print(X_val.shape)
print(y_val.shape)
print()
print(X_test.shape)
print(y_test.shape)
print()

#%%
f, ax = plt.subplots(figsize=(8, 6))
sns.distplot(y_train)
plt.show()

#%%
f, ax = plt.subplots(figsize=(8, 6))
sns.distplot(y_val)
plt.show()

#%%
f, ax = plt.subplots(figsize=(8, 6))
sns.distplot(y_test)
plt.show()

#%%
y_train.describe()

#%%
y_val.describe()

#%%
y_test.describe()

#%%
with open('../11.data/19.data/10.X_train.pickle', 'wb') as w:
    pickle.dump(X_train, w)
with open('../11.data/19.data/10.y_train.pickle', 'wb') as w:
    pickle.dump(y_train, w)
    
with open('../11.data/19.data/10.X_val.pickle', 'wb') as w:
    pickle.dump(X_val, w)
with open('../11.data/19.data/10.y_val.pickle', 'wb') as w:
    pickle.dump(y_val, w)
    
with open('../11.data/19.data/10.X_test.pickle', 'wb') as w:
    pickle.dump(X_test, w)
with open('../11.data/19.data/10.y_test.pickle', 'wb') as w:
    pickle.dump(y_test, w)

#%%
scaler = StandardScaler()

X_trian = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

X_val = scaler.transform(X_val)

#%%
with open('../11.data/19.data/11.X_train.pickle', 'wb') as w:
    pickle.dump(X_train, w)
    
with open('../11.data/19.data/11.X_val.pickle', 'wb') as w:
    pickle.dump(X_val, w)
    
with open('../11.data/19.data/11.X_test.pickle', 'wb') as w:
    pickle.dump(X_test, w)