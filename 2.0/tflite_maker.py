# supervised

import dataframe
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from tensorflow.python.keras.models import Sequential, load_model
from tensorflow.python.keras.layers import Dense
import matplotlib.pyplot as plt

# def evaluate_model(model, X, y):
#     predictions = model.predict(X)
#     predictions = (predictions >= 0.5).astype(int)
#     accuracy = accuracy_score(y, predictions)
#     report = classification_report(y, predictions, output_dict=True, zero_division=1)
#     return accuracy, report

# # Create train-test split
# X_train, X_test, y_train, y_test = train_test_split(dataframe.X, dataframe.y, test_size=0.2, random_state=42)

# Load the model
loaded_model = load_model('deepnn_model.h5')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(loaded_model)
tflite_model = converter.convert()

# Save the TFLite model
with open('deepnn.tflite', 'wb') as f:
    f.write(tflite_model)

# # Load the TFLite model
# interpreter = tf.lite.Interpreter(model_path="deepnn.tflite")
# interpreter.allocate_tensors()

# # Get input and output tensors
# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# # Prepare input data (assuming X_test is your test data)
# input_data = X_test.to_numpy().astype(np.float32)

# # Convert input_data to numpy array if it's a DataFrame
# if isinstance(input_data, pd.DataFrame):
#     input_data = input_data.to_numpy()

# # Make predictions
# tflite_predictions = []
# for i in range(len(input_data)):
#     interpreter.set_tensor(input_details[0]['index'], [input_data[i]])
#     interpreter.invoke()
#     output = interpreter.get_tensor(output_details[0]['index'])
#     tflite_predictions.append(output[0])

# tflite_predictions = np.array(tflite_predictions)
# tflite_predictions = (tflite_predictions >= 0.5).astype(int)

# # Evaluate TFLite model predictions
# tflite_accuracy = accuracy_score(y_test, tflite_predictions)
# tflite_report = classification_report(y_test, tflite_predictions, output_dict=True, zero_division=1)

# print(f"TFLite Model Test Accuracy: {tflite_accuracy:.4f}")
# print(f"TFLite Model Test F1 Score: {tflite_report['weighted avg']['f1-score']:.4f}")