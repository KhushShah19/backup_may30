
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/home/groot/.pylint.d/fertility_rate.csv")

x = df['fertility rate']
y = df['worker percent']

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size =0.2)

x_train_array, y_train_array = np.array(x_train).reshape(-1, 1), np.array(y_train)
x_test_array, y_test_array = np.array(x_test).reshape(-1, 1), np.array(y_test)

pred = LinearRegression()
pred.fit(x_train_array, y_train_array)
pred.predict(x_test_array) 
my_pred = pred.score(x_test_array, y_test_array)

print("\nmy prediction percentage :", my_pred*100) # 94.09003003852288 - changes everytime
print("Thank You")

