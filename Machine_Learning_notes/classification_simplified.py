
# pandas to get help with Machine Learning
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# reading file with read_csv(which is in csv format)
pok = pd.read_csv("/home/groot/.pylint.d/pokemon_data.csv")

print(pok.columns) # to know the names of all the columns
# ('#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
# 'Sp. Def', 'Speed', 'Generation', 'Legendary'],dtype='object')

new_names = {'Type 1':'type1', 'Type 2':'type2', 'HP':'hp', 'Attack':'atk', 'Defense':'dfn', 
'Sp. Atk':'atk_spd', 'Sp. Def':'dfn_spd', 'Speed':'spd', 'Legendary':'leg'}
pok = pok.rename(columns={'Generation':'gen'}) # (columns={'oldName1': 'newName1'})
pok = pok.rename(columns=new_names) # to change multi columns => columns = names_dic
pok = pok.drop(columns=['Name', '#']) # to drop multi columns => columns = drop_list (or 'to_chnage')

#pok['type2'] = pok['type2'].str.lower() 
#print(pok.head())

print(pok.info()) # to know data_type(int, bool, object), number of NaN values (if any) and total values
pok['type2'] = pok['type2'].replace(np.nan, 1) # replacing NaN with 0(int)
pok['leg'] = pok['leg'].astype(int) # to change from boolean to int 


############### Without removing out liers ###############

x = pok.loc[:, pok.columns!='leg'] # full pok exculeding leg
y = pok['leg']

#x['type2'] = x['type2'].str.lower() # to make type2 different from type1 

xdt1 = pd.get_dummies(pok['type1']) # making dummies to get str category into readable form
xdt2 = pd.get_dummies(pok['type2'])
x = pd.concat([x, xdt1, xdt2], axis='columns') # merging all dummies to main data set
x = x.drop(columns=['type1', 'type2']) # removing the main value(dummies creators)


# split into train test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # ((640, 44) (160, 44) (640,) (160,)

# fit the model (Random Forest)
model = RandomForestClassifier(random_state=1)
model.fit(x_train, y_train)

# make predictions
pred = model.predict(x_test)

# evaluate predictions
acc = accuracy_score(y_test, pred)
print('Accuracy :  %.3f' % acc) # 93 - 97 (%.3f = upto 3 decimal)

