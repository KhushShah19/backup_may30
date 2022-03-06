

# ctrl + k + c -> keep multi '#' and clrt + k + u -> remove them
print(777)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from income_project.modified_col_income import df # load dataset
# to run: python3 -m income_project.pred_income

# split into inputs and outputs
x = df.loc[:, df.columns!='salary>50k']
y = df['salary>50k']

#print(x.columns)

# split into train test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (35011, 24) (8753, 24) (35011,) (8753,)

# fit the model (Random Forest)
model = RandomForestClassifier(random_state=1)
model.fit(x_train, y_train)

# make predictions
pred = model.predict(x_test)

# evaluate predictions
acc = accuracy_score(y_test, pred)
print('Accuracy :  %.3f' % acc) # 84 - 85 (%.3f = upto 3 decimal)
