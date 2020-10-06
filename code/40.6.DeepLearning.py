#%%
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from keras import losses
import pickle

#%%
np.random.seed(0)

#%%
with open('../11.data/19.data/11.X_train.pickle', 'rb') as r:
    X_train = pickle.load(r)
with open('../11.data/19.data/10.y_train.pickle', 'rb') as r:
    y_train = pickle.load(r)
    
with open('../11.data/19.data/11.X_test.pickle', 'rb') as r:
    X_test = pickle.load(r)
with open('../11.data/19.data/10.y_test.pickle', 'rb') as r:
    y_test = pickle.load(r)
    
with open('../11.data/19.data/11.X_val.pickle', 'rb') as r:
    X_val = pickle.load(r)
with open('../11.data/19.data/10.y_val.pickle', 'rb') as r:
    y_val = pickle.load(r)
    
#%%
#optimizer = optimizers.Adam(lr=0.00001)
optimizer = optimizers.RMSprop(lr=0.000001)
model = Sequential()
model.add(Dense(256, activation='sigmoid', input_shape=(X_train.shape[1],)))
model.add(Dense(256, activation='sigmoid'))
model.add(Dense(64, activation='sigmoid'))
model.add(Dense(1))
model.compile(optimizer=optimizer, loss=losses.mean_absolute_error)

#%%
hist_256 = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10000)

#%%
model.evaluate(X_test, y_test)

#%%
model.save('../11.data/50.deeplearning_model/hist_256_256')

#%%
from keras.layers import Dropout

#optimizer = optimizers.Adam(lr=0.00001)
#optimizer = optimizers.RMSprop(lr=0.000001)
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='rmsprop', loss='mae')

#%%
hist_reduced = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10000)