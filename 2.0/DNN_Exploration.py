import dataframe
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import matplotlib.pyplot as plt

np.random.seed(40)
tf.random.set_seed(40)

# Create train-test split
X_t, X_test, y_t, y_test = train_test_split(dataframe.X, dataframe.y, test_size=0.2, random_state=40)
X_train,X_val,y_train,y_val = train_test_split(X_t, y_t, test_size=0.2, random_state=40)

def build_and_train_model(hidden_layers, neurons_per_layer, epochs=40):
    model = Sequential()
    model.add(Dense(neurons_per_layer, activation='relu', input_shape=(13,)))
    
    for _ in range(hidden_layers - 1):
        model.add(Dense(neurons_per_layer, activation='relu'))
    
    model.add(Dense(4, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    history = model.fit(X_train, y_train, epochs=epochs, validation_data = (X_val,y_val), verbose=0)
    
    return model, history

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    predictions = (predictions >= 0.5).astype(int)
    accuracy = accuracy_score(y, predictions)
    report = classification_report(y, predictions, output_dict=True, zero_division=1)
    return accuracy, report

# List of architectures to try
architectures = [
    (3, 20), (4, 20), (5, 20),
    (3, 35), (4, 35), (5, 35),
    (3, 50), (4, 50), 
    (5, 50)
]

results = []

for hidden_layers, neurons in architectures:
    print(f"\nTraining model with {hidden_layers} hidden layers and {neurons} neurons per layer")
    model, history = build_and_train_model(hidden_layers, neurons)
    if hidden_layers == 3 and neurons == 35: # change with config of whicever model performs best to be saved
        model.save('deepnn_model.h5')
                # Plot training history
        plt.figure(figsize=(12, 4))

        # Plot accuracy
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()

        # Plot loss
        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()

        plt.tight_layout()
        plt.show()
    train_accuracy, train_report = evaluate_model(model, X_train, y_train)
    test_accuracy, test_report = evaluate_model(model, X_test, y_test)
    
    results.append({
        'architecture': f"{hidden_layers} layers, {neurons} neurons",
        'train_accuracy': train_accuracy,
        'test_accuracy': test_accuracy,
        'train_f1': train_report['weighted avg']['f1-score'],
        'test_f1': test_report['weighted avg']['f1-score'],
        'history': history
    })

# Print results
for result in results:
    print(f"\nArchitecture: {result['architecture']}")
    print(f"Train Accuracy: {result['train_accuracy']:.4f}")
    print(f"Test Accuracy: {result['test_accuracy']:.4f}")
    print(f"Train F1 Score: {result['train_f1']:.4f}")
    print(f"Test F1 Score: {result['test_f1']:.4f}")

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Model Accuracy Comparison')
for result in results:
    plt.plot(result['history'].history['val_accuracy'], label=result['architecture'])
plt.xlabel('Epoch')
plt.ylabel('Validation Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Model Loss Comparison')
for result in results:
    plt.plot(result['history'].history['val_loss'], label=result['architecture'])
plt.xlabel('Epoch')
plt.ylabel('Validation Loss')
plt.legend()

plt.tight_layout()
plt.show()