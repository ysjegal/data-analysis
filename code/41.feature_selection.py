#%%
import pickle
import numpy as np
import pandas as pd
import operator

#%%
with open('../11.data/40.feature_selection/02.Lasso.pickle', 'rb') as r:
    ls = pickle.load(r)
    
with open('../11.data/40.feature_selection/03.DecisionTreeRegressor.pickle', 'rb') as r:
    dt = pickle.load(r)

with open('../11.data/40.feature_selection/04.RandomForestRegressor.pickle', 'rb') as r:
    rf = pickle.load(r)

with open('../11.data/40.feature_selection/05.ExtraTreeRegressor.pickle', 'rb') as r:
    etr = pickle.load(r)
    
with open('../11.data/40.feature_selection/06.GradientBoostingRegressor.pickle', 'rb') as r:
    gbr = pickle.load(r)
    
#%%
feature = list(ls.keys())

#%%
ls_value = np.abs(np.array(list(ls.values())))
dt_value = np.array(list(dt.values()))
rf_value = np.array(list(rf.values()))
etr_value = np.array(list(etr.values()))
gbr_value = np.array(list(gbr.values()))

#%%
ls_value = (ls_value - min(ls_value)) / (max(ls_value) - min(ls_value))
dt_value = (dt_value - min(dt_value)) / (max(dt_value) - min(dt_value))
rf_value = (rf_value - min(rf_value)) / (max(rf_value) - min(rf_value))
etr_value = (etr_value - min(etr_value)) / (max(etr_value) - min(etr_value))
gbr_value = (gbr_value - min(gbr_value)) / (max(gbr_value) - min(gbr_value))

#%%
ls_score = 0.688152
dt_score = 0.615856
rf_score = 0.823002
etr_score = 0.824292
gbr_score = 0.781451

#%%
ls_weight = ls_score * ls_value
dt_weight = dt_score * dt_value
rf_weight = rf_score * rf_value
etr_weight = etr_score * etr_value
gbr_weight = gbr_score * gbr_value

#%%
ls_min_max = (min(ls_weight), max(ls_weight))
dt_min_max = (min(dt_weight), max(dt_weight))
rf_min_max = (min(rf_weight), max(rf_weight))
etr_min_max = (min(etr_weight), max(etr_weight))
gbr_min_max = (min(gbr_weight), max(gbr_weight))

#%%
dist_worst = []
dist_best = []
for i in range(len(ls_weight)):
    dist_worst.append(np.sqrt((ls_weight[i]-ls_min_max[0])**2 + (dt_weight[i]-dt_min_max[0])**2 + (rf_weight[i]-rf_min_max[0])**2 + (etr_weight[i]-etr_min_max[0])**2 + (gbr_weight[i]-gbr_min_max[0])**2))
    dist_best.append(np.sqrt((ls_weight[i]-ls_min_max[1])**2 + (dt_weight[i]-dt_min_max[1])**2 + (rf_weight[i]-rf_min_max[1])**2 + (etr_weight[i]-etr_min_max[1])**2 + (gbr_weight[i]-gbr_min_max[1])**2))
    
#%%
closeness = []
for i in range(len(dist_best)):
    closeness.append(dist_worst[i] / (dist_best[i] + dist_worst[i]))

#%%
df = pd.DataFrame([feature, closeness])
df = df.T
df.columns=['feature','closeness']
df.to_csv('../11.data/41.feature_topsis.csv', index=False, encoding='cp949')
    
#%%
priority = {feature[i]: closeness[i] for i in range(len(feature))}

#%%
sorted_coef_dict =  sorted(priority.items(), key=operator.itemgetter(1))