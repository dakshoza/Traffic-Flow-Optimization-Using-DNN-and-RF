# import pandas as pd
# import numpy as np
# # from sklearn.preprocessing  import StandardScaler
# from tensorflow.python.keras.models import load_model
# from tensorflow.python.keras.models import Sequential
# import tensorflow as tf
# from tensorflow.python.keras.layers import Dense
# from tensorflow.python.keras.optimizers import Adam

# class model:
#     def __init__(self) -> None:
#         self.learningRate = 0.01
#         self.trainShape = (13,)
#         self.model = Sequential([
#             Dense(28, activation = 'relu', input_shape = self.trainShape),
#             Dense(28, activation = 'relu'),
#             Dense(4, activation = 'sigmoid')
#         ])
#         self.model.compile(loss = 'categorical_crossentropy', optimizer=Adam(learning_rate=self.learningRate), metrics=['accuracy'])

#         self.model.load_model('2.0\model_weights.h5')

        