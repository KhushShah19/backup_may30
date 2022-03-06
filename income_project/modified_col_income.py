
# to use: from income_project.modified_col_income import df

import pandas as pd
from income_project.outlier_income import df
# to run: python3 -m income_project.modified_col_income 

""" Non-Null(0), data_type = all int

modified : ['gender', 'relations', 'marital', 'mar3', 'worktype', 'race', 'native']

columns : ['age', 'edu_num', relations', 'gender', 'cgain', 'closs', 'hours*7', 
    'native', 'salary>50k', 'divided', 'married', 'not_married', 'black', 
    'others', 'white', 'Nan', 'Federal-gov', 'Local-gov', 'Never-worked', 
    'Private', 'Self-emp-inc', 'Self-emp-not-inc', 'State-gov', 'Without-pay']

total(24 columns), int64(9), uint8(15 -> all dummies) ... memory usage: 3.6 MB
removed : ['marital', 'mar3', 'worktype', 'race'] """

df['gender'] = df['gender'].replace({'Female':0, 'Male':1}) # changing str to int

# look_after == to_take_care == takecare = 1 : ['Husband', 'Own-child', 'Other-relative', 'Wife']
df['relations'] = df['relations'].replace({'Husband':1, 'Not-in-family':0, 
    'Own-child':1, 'Unmarried':0, 'Other-relative':1, 'Wife':1})

""" mar3 = ['married', 'not_married', 'divided']

    married = ['Married-AF-spouse', 'Married-civ-spouse']
    divided = ['Separated', 'Widowed', 'Married-spouse-absent']
    not_married = ['Never-married', 'Divorced'] """

df['mar3'] = df['marital'].replace({'Married-spouse-absent':"married", 'Divorced':"not_married", 
    'Never-married':"not_married", 'Married-AF-spouse':"divided", 'Married-civ-spouse':"married", 
    'Separated':"divided", 'Widowed':"divided"})

dumi_mar3 = pd.get_dummies(df["mar3"]) # making 3 dummies

df['worktype'] = df['worktype'].fillna('Nan')
#worktype_name = ['Private', 'State-gov', 'Self-emp-not-inc', 'Federal-gov',
#           'Local-gov', 'Self-emp-inc', nan, 'Never-worked', 'Without-pay']
dumi_worktype = pd.get_dummies(df["worktype"]) # making 9 dummies


df["race"] = df["race"].replace({'White':'white', 'Black':'black', 'Other':'others',
        'Asian-Pac-Islander':'others', 'Amer-Indian-Eskimo':'others'})

dumi_race = pd.get_dummies(df["race"]) # making 3 dummies

# might make it simpler
df['native'] = df['native'].replace({'United-States':1})
df['native'] = pd.to_numeric(df['native'], errors='coerce')
df['native'] = df['native'].fillna(0)
df['native'] = df['native'].astype(int)


# adding all the dummy columns to df at once
df = pd.concat([df, dumi_mar3, dumi_race, dumi_worktype], axis="columns")

not_needed = ['marital', 'mar3', 'worktype', 'race']
df = df.drop(columns=not_needed)



