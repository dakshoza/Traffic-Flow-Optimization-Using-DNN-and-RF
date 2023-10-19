import pandas as pd
from sklearn.preprocessing  import StandardScaler

dataframe = pd.read_csv('2.0\TrainingDataset.csv')

columns = ['target state 1', 'target state 2', 'target state 3', 'target state 4']

X = dataframe.drop(columns= columns, axis= 1)
y = dataframe[columns]

