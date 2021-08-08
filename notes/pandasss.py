
# Why Pandas? Working with big data and flexibility of pandas

import pandas as pd
import numpy as np

# poke = pd.read_csv("/home/groot/.pylint.d/pokemon_data.csv") # reading the file
# Name,  Type 1,  Type 2,  HP,  Attack,  Defense,  Sp. Atk,  Sp. Def,  Speed,  Generation,  Legendary

""" # read the data in different ways
# print(poke) 
# print(poke.head(10)) # shows top 10 
# print(poke.tail(10)) # shows bottom 10
# print(poke.columns) # shows index 
# print(poke["Speed"][33:44]) # show specific thing and range of it 
# print(poke[["Name", "Speed", "Attack", "Defense"]]) # to read coloums
# print(poke.iloc[33:44]) # to read rows
# print(poke.iloc[2:3, 1]) # read specific location [R, C]
# print(poke.loc[poke["Type 1"] == "Fire"])  # read one type of it 
#for index, row in poke.iterrows(): # read only one specific type
#    print(index, row["Name"]) # not a MultuIndex  """


# print() # Describing and Sorting
# print(poke.describe()) # cool status about data
# print(poke.sort_values("Name", ascending=False)) # sorting
# print(poke.sort_values(["HP", "Speed"], ascending=[0, 0]))

""" # Making Changes to a Data
poke["ad"] = poke["Attack"] + poke["Defense"] # adding coloums
poke["ads_01"] = poke.iloc[:, 7:9].sum(axis=1)
poke["ads"] = poke["Sp. Atk"] + poke["Sp. Def"] # ads = ads_01 ....different ways
poke = poke.drop(columns="Attack") # remove only one coloum """

# cols = list(poke.columns)
# poke = poke[cols[4: 9] + cols[9:11] + cols[1:4] +  cols[11:]] # rearranging it

# print(poke.sort_values("ad", ascending=0)) 

#HP,  [[Attack]],  Defense,  Sp. Atk,  Sp. Def,  Speed,  Generation,  Legendary, Name,  Type 1,  Type 2, ad, ads_01, ads

# poke.to_csv("pokenew.csv", index=False) # saving it

a = pd.Series([2, 3, 5, 7], [4, 6, 8, 2], dtype="int32") # basic
# print(a)

dates = pd.date_range("20020201", periods=10, freq="D", normalize=4)

# print(dates)

row_coloum = np.random.randint(1, 9, size=(10,4))

df = pd.DataFrame(row_coloum, index=dates, columns=["aa", "bb", "cc", "dd"])

df["tt"] = df.iloc[:, :].sum(axis=1)
df["mean"] = df.iloc[:, :].mean(axis=1)

print(df)













