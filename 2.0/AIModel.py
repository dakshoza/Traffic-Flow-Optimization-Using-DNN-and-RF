import dataframe
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np

model1 = Sequential([
    Dense(20, activation = 'relu', input_shape = (13,)),
    Dense(24, activation = 'relu'),
    Dense(10, activation = 'relu'),
    Dense(4, activation = 'sigmoid')
])
model1.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model1.fit(dataframe.X, dataframe.y, epochs = 10)

model1.load_weights('2.0\model_weights.h5')

