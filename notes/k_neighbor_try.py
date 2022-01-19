
import pandas as pd
import numpy as np
from sklearn import preprocessing, neighbors
from sklearn import model_selection

data_frame = pd.read_csv("/home/groot/.pylint.d/pokemon_data.csv") 
# Name,  Type 1,  Type 2,  HP,  Attack,  Defense,  Sp. Atk,  Sp. Def,  Speed,  Generation,  Legendary

#print(data_frame.columns) # shows index 

data_frame = data_frame.drop(['#', 'Name', "Type 1", "Type 2", 'Generation', 'HP'], axis=1)
#data_frame = data_frame.drop(['#', 'Name', "Type 1", "Type 2", 'Generation'], axis=1)
#data_frame = data_frame.drop(['#', 'Name', "Type 1", "Type 2", 'Sp. Atk', 'Sp. Def', 'Generation'], axis=1)
# different combo gives different perdiction percentage(final score)

#print(data_frame.columns) # shows index
# ['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Legendary']
# print(data_frame[522:568])

x = np.array(data_frame.drop(["Legendary"], axis=1))
y = np.array(data_frame["Legendary"])

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
# this test samples are different so percidiction might differ

#print(y_train)
clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)
accuracy_02 = clf.score(x_test, y_test)
print("score :", accuracy_02*100)

my_test = np.array([[98, 98, 88, 88, 97], [100, 100, 100, 100, 90], [130, 130, 120, 120, 110]]) # shape => (3, 5)
#print(my_test.shape)
my_test = my_test.reshape(len(my_test), -1)
my_perd = clf.predict(my_test)
print(my_perd) # might differ

 
