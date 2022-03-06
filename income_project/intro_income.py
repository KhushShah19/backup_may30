
# to use: from income_project.intro_income import df
# to run: python3 -m income_project.(file_name) # ex: python3 -m income_project.trying_mapping

import pandas as pd

df = pd.read_csv("/home/groot/.pylint.d/incomee.csv") 
# 'age', 'workclass', 'fnlwgt', 'education', 'educational-num', 'marital-status', 
# 'occupation', 'relationship', 'race', 'gender', 'capital-gain', 'capital-loss', 
# 'hours-per-week', 'native-country', 'income_>50K'

boring_names ={'fnlwgt':'salary', 'education':'edu', 'educational-num':'edu_num', 
    'marital-status':'marital', 'relationship':'relations', 'capital-gain':'cgain', 
    'capital-loss':'closs', 'workclass':'worktype', 'native-country':'native', 
    'income_>50K':'salary>50k', 'hours-per-week':'hours*7'}

df = df.rename(columns=boring_names) # changing names
lets_drop = ['edu', 'occupation'] 
df = df.drop(columns=lets_drop) # droping columns

# print(df.columns)
# 'age', 'worktype', 'edu_num', 'marital', 'occupation', 'relations'
# 'race', 'gender', 'cgain', 'closs', 'hours*7', 'native, 'salary>50k'
