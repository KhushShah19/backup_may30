
from matplotlib import colors
import numpy as np
from numpy import square 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
POK = 0 

if POK == 1111: # way to get data

    import pandas as pd
    import numpy as np
    
    poke = pd.read_csv("/home/groot/.pylint.d/pokemon_data.csv") # reading the file, around 800 data

    xx = list(poke.iloc[0:10, 5]) # x values
    yy = list(poke.iloc[0:10, 6]) # y values
    print(xx, yy)


x = [49, 62, 82, 100, 52, 64, 84, 130, 104, 58]
y = [49, 63, 83, 93, 43, 58, 78, 115, 98, 55]
x_ar, y_ar = np.array(x), np.array(y)

if POK == 10: # finding m and c using formula
    x_sum, y_sum = sum(x), sum(y) # sum of xs and ys
    x_squar, y_squar = sum(square(x)), sum(square(y)) # sum of square of xs and ys
    print(x_squar, y_squar)

    X_x_Y = 0
    X_x_Y = [X_x_Y+ (int(x[i])*int(y[i])) for i in range(len(x))] # list of (x(i)*y(i))
    print(sum(X_x_Y))

    mformula = ((y_sum*x_squar) - (x_sum*(sum(X_x_Y)))) / (((x_squar) - (x_sum)**2))
    cformula = (sum(X_x_Y) - (x_sum*(y_sum))) / (((x_squar) - (x_sum)**2))
    print(mformula, cformula)

m_np, c_np = np.polyfit(x, y, 1) # letting numpy find m and c 
print(m_np, c_np)

if POK == 99: # for seeeing Graph
    points = plt.scatter(x, y)
    pointsss = plt.scatter(x[-2:], y[-2:], color="red")
    lines = plt.plot(x_ar, m_np*x_ar + c_np)

    print(plt.show()) # see in terminal

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size =0.2, random_state=8) 
# test_size = percent(decimal*100) of data to be tested (0.1 = 10% to test) and random state = to not take random values
print(x_train, x_test, y_train, y_test)


x_train_array, y_train_array = np.array(x_train).reshape(8, 1), np.array(y_train)
x_test_array, y_test_array = np.array(x_test).reshape(2, 1), np.array(y_test)


pred = LinearRegression()
pred.fit(x_train_array, y_train_array)
pred.predict(x_test_array) 
my_pred = pred.score(x_test_array, y_test_array)

print("\nmy prediction percentage :", my_pred*100)
print("Thank You")











