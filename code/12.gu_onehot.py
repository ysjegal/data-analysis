#%%
import pandas as pd
import numpy as np
import pickle

#%%
with open('../11.data/00.adjacent_gu.pickle','rb') as r:
    adjacent_gu = pickle.load(r)
    
#%%
hi = np.eye(len(adjacent_gu.keys()))

#%%
df = pd.DataFrame(hi, columns=adjacent_gu.keys())

#%%
df['gu'] = adjacent_gu.keys()

#%%
y = pd.read_csv('../11.data/02.2.building_geometry/00.y_geometry.csv', encoding='cp949')

#%%
hello = y.merge(df, left_on='gu', right_on='gu')

#%%
hello.to_csv('../11.data/10.features/26.건물소속자치구.csv', encoding='cp949')