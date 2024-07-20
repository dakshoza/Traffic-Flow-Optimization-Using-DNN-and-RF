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

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    predictions = (predictions >= 0.5).astype(int)
    accuracy = accuracy_score(y, predictions)
    report = classification_report(y, predictions, output_dict=True, zero_division=1)
    return accuracy, report

# Create train-test split
X_train, X_test, y_train, y_test = train_test_split(dataframe.X, dataframe.y, test_size=0.2, random_state=42)

# Build and train the model
model1 = Sequential([
    Dense(35, activation='relu', input_shape=(13,)),
    Dense(35, activation='relu'),
    Dense(35, activation='relu'),
    Dense(4, activation='softmax')
])
model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Train on the training set
history = model1.fit(X_train, y_train, epochs=15, verbose=0)

# # Save the model
# model1.save('deepnn_model.h5')

# Load the model
# loaded_model = load_model('deepnn_model.h5')
loaded_model = model1

# Evaluate the loaded model
train_accuracy, train_report = evaluate_model(loaded_model, X_train, y_train)
test_accuracy, test_report = evaluate_model(loaded_model, X_test, y_test)

results = [{
    'train_accuracy': train_accuracy,
    'test_accuracy': test_accuracy,
    'train_f1': train_report['weighted avg']['f1-score'],
    'test_f1': test_report['weighted avg']['f1-score']
}]

for result in results:
    print(f"Train Accuracy: {result['train_accuracy']:.4f}")
    print(f"Test Accuracy: {result['test_accuracy']:.4f}")
    print(f"Train F1 Score: {result['train_f1']:.4f}")
    print(f"Test F1 Score: {result['test_f1']:.4f}")

# Plot training history
# plt.figure(figsize=(12, 4))

# # Plot accuracy
# plt.subplot(1, 2, 1)
# plt.plot(history.history['accuracy'], label='Training Accuracy')
# plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
# plt.title('Model Accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.legend()

# # Plot loss
# plt.subplot(1, 2, 2)
# plt.plot(history.history['loss'], label='Training Loss')
# plt.plot(history.history['val_loss'], label='Validation Loss')
# plt.title('Model Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.legend()

# plt.tight_layout()
# plt.show()


# Get predictions
y_pred = loaded_model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

print("\nTrue Labels and Predictions:")
print("Index | True Label | Predicted Label | Prediction Probabilities")
print("-" * 70)

for idx in range(len(y_test)):
    true_label = y_true_classes[idx]
    pred_label = y_pred_classes[idx]
    pred_probs = y_pred[idx]
    
    # Format the prediction probabilities as a string with 4 decimal places
    pred_probs_str = '[' + ', '.join([f'{x:.4f}' for x in pred_probs]) + ']'
    
    print(f"{idx:5d} | {true_label:10d} | {pred_label:15d} | {pred_probs_str}")

print(f"\nTotal samples: {len(y_test)}")

# Calculate and print accuracy
accuracy = np.mean(y_pred_classes == y_true_classes)
print(f"Accuracy: {accuracy:.4f}")

# Print confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true_classes, y_pred_classes)
print("\nConfusion Matrix:")
print(cm)