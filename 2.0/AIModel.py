import dataframe
import tensorflow as tf
import numpy as np
from sklearn.metrics import mean_squared_error
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

model1 = Sequential([
    Dense(20, activation = 'relu', input_shape = (13,)),
    Dense(13, activation = 'relu'),
    Dense(13, activation = 'relu'),
    Dense(4, activation = 'sigmoid')
])
model1.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model1.fit(dataframe.X, dataframe.y, epochs = 20)

model1.save_weights('2.0\model_weights.h5')

# model1.load_weights('2.0\model_weights.h5')

# predictions = model1.predict(dataframe.X)
# predictions = (predictions >= 0.5).astype(int)
# for i in predictions:
#     print(i)
# for i in np.array([dataframe.y])[0]:
#     print(i)
# print(mean_squared_error(dataframe.y, predictions))


