import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Read Data
path = 'E:/__WB/Certified AI Engineer nach ISO  IEC 17024/digethik-software-engineering-2025'
data = pd.read_csv(f'{path}/data/auto-mpg.csv', sep=';')

print(data.head)

# Shuffle Data
data = data.sample(frac=1)

y_variable = data['mpg']

# Get all columns that contain attributes
x_variables = data.loc[:, data.columns != 'mpg']

x_train, x_test, y_train, y_test = train_test_split(x_variables, y_variable, test_size=0.2)

regressor = LinearRegression()
regressor = regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

file_to_write = open(f'{path}/data/models/auto-mpg.pickle', 'wb')
pickle.dump(regressor, file_to_write)
