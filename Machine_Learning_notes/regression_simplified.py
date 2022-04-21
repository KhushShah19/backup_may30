

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = [49, 62, 82, 100, 52, 64, 84, 130, 104, 58]
y = [49, 63, 83, 93, 43, 58, 78, 115, 98, 55]


m_np, c_np = np.polyfit(x, y, 1) # letting numpy find m and c 
# print(m_np, c_np)


x_train, x_test, y_train, y_test = train_test_split(x, y,test_size =0.2, random_state=8) 
# test_size = percent(decimal*100) of data to be tested (0.1 = 10% to test) and random state = to not take random values
# print(x_train, x_test, y_train, y_test)


x_train_array, y_train_array = np.array(x_train).reshape(8, 1), np.array(y_train)
x_test_array, y_test_array = np.array(x_test).reshape(2, 1), np.array(y_test)


pred = LinearRegression()
pred.fit(x_train_array, y_train_array)
pred.predict(x_test_array) 
my_pred = pred.score(x_test_array, y_test_array)

print("\nmy prediction percentage :", my_pred*100)
print("Thank You")

