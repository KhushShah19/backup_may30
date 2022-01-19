
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

df = pd.read_csv("/home/groot/.pylint.d/incomee.csv") 
# 'age', 'workclass', 'fnlwgt', 'education', 'educational-num', 'marital-status', 
# 'occupation', 'relationship', 'race', 'gender', 'capital-gain', 'capital-loss', 
# 'hours-per-week', 'native-country', 'income_>50K'

boring_names ={'fnlwgt':'salary', 'education':'edu', 'educational-num':'edu_num', 
    'marital-status':'marital', 'relationship':'relations', 'capital-gain':'cgain', 
    'capital-loss':'closs', 'workclass':'worktype', 'native-country':'native', 
    'income_>50K':'salary>50k', 'hours-per-week':'hours*7'}

df = df.rename(columns=boring_names) # changing names
lets_drop = ['edu', 'salary>50k', 'occupation'] 
df = df.drop(columns=lets_drop) # droping columns

# print(df.columns)
# 'age', 'worktype', 'salary', 'edu_num', 'marital', 'occupation',
# 'relations', 'race', 'gender', 'cgain', 'closs', 'hours*7', 'native'

# occ = df.groupby(['relations']).size() # number of times occured
# tl = df['relations'].tolist() # list of them (with repeation)
# print(occ)
# print(set(tl)) # to remove repeation 


# ctrl + k + c -> keep multi '#' and clrt + k + u -> remove them
# worktype, marital, relation, race, gender, native ... changing from object to int64
df['gender'] = df['gender'].replace({'Female':0, 'Male':1}) # changing str to int
df['race'] = df['race'].replace({'White':1, 'Black':2, 
    'Asian-Pac-Islander':3, 'Amer-Indian-Eskimo':4, 'Other':5})

df['marital'] = df['marital'].replace({'Married-spouse-absent':7, 'Divorced':3, 'Never-married':2, 
    'Married-AF-spouse':6, 'Married-civ-spouse':1, 'Separated':5, 'Widowed':4})

df['relations'] = df['relations'].replace({'Husband':1, 'Not-in-family':2, 
    'Own-child':3, 'Unmarried':4, 'Other-relative':6, 'Wife':5})

df['worktype'] = df['worktype'].replace({'Federal-gov':2, 'Private':1, 'Self-emp-not-inc':7, 
    'State-gov':4, 'Never-worked':8, 'Self-emp-inc':6, 'Without-pay':5, 'Local-gov':3})
df['worktype'] = df['worktype'].fillna(0)
df['worktype'] = df['worktype'].astype(int)

df['native'] = df['native'].replace({'United-States':1})
df['native'] = pd.to_numeric(df['native'], errors='coerce')
df['native'] = df['native'].fillna(2)
df['native'] = df['native'].astype(int)

x = df.drop(columns='salary')
y = df['salary']
li = []

for i in range(10):
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size =0.1)

    pred = LinearRegression()
    pred.fit(x_train, y_train)
    pred.predict(x_test) 
    my_pred = pred.score(x_test, y_test)
    print(my_pred*100)
    li += [my_pred*100]

print("\nmy prediction percentage avg :", sum(li)/10) # 2 highest, avg 1.3
print("Thank You")








