import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

df = pd.read_csv("/home/groot/.pylint.d/possum.csv")
#  'case', 'site', 'age', 'hdlngth', 'skullw', 'totlngth', 'taill', 'footlgth', 'earconch', 'eye', 'chest', 'belly'

df['age'] = df['age'].fillna(df['age'].mode()) 
df['footlgth'] = df['footlgth'].fillna(df['footlgth'].mode()) # 73.2

# print(df['age'], df['footlgth'])
df = df.drop(df[(df['footlgth']<75) & (df['totlngth']<78)].index)
#df = df.drop(df[(df['taill']<33) & (df['totlngth']<82)].index)
#df = df.drop(df[(df['taill']>42) & (df['totlngth']<94)].index)
#print(df.describe())

df['tf'] = df['totlngth'] + df['footlgth']
#df['tailfoot'] = df['taill'] + df['footlgth']
df['htf'] = df['hdlngth'] + df['taill'] + df['footlgth']
df['cs'] = df['chest'] + df['skullw']
df['cb'] = df['chest'] + df['belly'] 

fig, ax = plt.subplots()
ax.scatter(x = df['htf'], y = df['cs'])
plt.xlabel('X axis', fontsize=13)
plt.ylabel('Y asis', fontsize=13)
#plt.xlabel('GrLivArea', fontsize=13)
plt.show()

'''


df = df.drop(columns="Pop") 
df = df.drop(columns="case") 
df = df.drop(columns=['site', 'age', 'hdlngth', 'skullw', 'earconch', 'eye', 'chest', 'belly', 'sex', 'totlngth', 'taill', 'footlgth'])
print(df)
#print(df.isna().any())

x = df.drop(columns='ttf')
y = df['ttf']


x_train, x_test, y_train, y_test = train_test_split(x, y,test_size =0.2)

pred = LinearRegression()
pred.fit(x_train, y_train)
pred.predict(x_test) 
my_pred = pred.score(x_test, y_test)

print("\nmy prediction percentage :", my_pred*100) # 95 highest
print("Thank You") '''


