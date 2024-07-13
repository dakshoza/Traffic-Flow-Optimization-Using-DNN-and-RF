from sklearn.ensemble import RandomForestClassifier
import dataframe
from sklearn.metrics import classification_report, accuracy_score
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    report = classification_report(y, predictions, output_dict=True, zero_division=1)
    return accuracy, report

# Create train-test split
X_train, X_test, y_train, y_test = train_test_split(dataframe.X, dataframe.y, test_size=0.2, random_state=42)

# Train the model
model1 = RandomForestClassifier(random_state=42, criterion='entropy', n_estimators=100, max_depth=15, max_features='log2')
model1.fit(X_train, y_train)

# Save the model to a pickle file
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(model1, file)

# Load the model from the pickle file
with open('random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# loaded_model = model1

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

# Plot feature importances
feature_importance = model1.feature_importances_
feature_names = dataframe.X.columns

plt.figure(figsize=(12, 6))
plt.bar(feature_names, feature_importance)
plt.title('Feature Importances in Random Forest Model')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
