#%%
import pandas as pd

#%%
y = pd.read_csv('../11.data/02.2.building_geometry/00.y_geometry.csv', encoding='cp949')

crime = pd.read_csv('../11.data/04.1.facilities/09.2.crime.csv', encoding='cp949')

#%%
hi = y.merge(crime, left_on='gu', right_on='gu')

#%%
hi[['gu','범죄율']].to_csv('../11.data/10.features/13.범죄율.csv', encoding='cp949')