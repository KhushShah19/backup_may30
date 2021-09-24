
# Why Pandas? Working with big data and flexibility of pandas

import pandas as pd
import numpy as np

pokenew = 0

if pokenew == 10:
    
    poke = pd.read_csv("/home/groot/.pylint.d/pokemon_data.csv") # reading the file
    # Name,  Type 1,  Type 2,  HP,  Attack,  Defense,  Sp. Atk,  Sp. Def,  Speed,  Generation,  Legendary

    if pokenew > 20: # read the data in different ways

        print(poke) 
        print(poke.head(10)) # shows top 10 
        print(poke.tail(10)) # shows bottom 10
        print(poke.columns) # shows index 
        print(poke["Speed"][33:44]) # show specific thing and range of it 
        print(poke[["Name", "Speed", "Attack", "Defense"]]) # to read coloums
        print(poke.iloc[33:44]) # to read rows
        print(poke.iloc[2:3, 1]) # read specific location [R, C]
        print(poke.loc[poke["Type 1"] == "Fire"])  # read one type of it 
        for index, row in poke.iterrows(): # read only one specific type
            print(index, row["Name"]) # not a MultuIndex  """

    elif pokenew > 30: # Describing and Sorting

        print(poke.describe()) # cool status about data
        print(poke.sort_values("Name", ascending=False)) # sorting
        print(poke.sort_values(["HP", "Speed"], ascending=[0, 0]))

    elif pokenew > 40: # Making Changes to a Data

        poke["ad"] = poke["Attack"] + poke["Defense"] # adding coloums
        poke["ads_01"] = poke.iloc[:, 7:9].sum(axis=1)
        poke["ads"] = poke["Sp. Atk"] + poke["Sp. Def"] # ads = ads_01 ....different ways
        poke = poke.drop(columns="Attack") # remove only one coloum """

        cols = list(poke.columns)
        poke = poke[cols[4: 9] + cols[9:11] + cols[1:4] +  cols[11:]] # rearranging it

        print(poke.sort_values("ad", ascending=0)) 

        #HP,  [[Attack]],  Defense,  Sp. Atk,  Sp. Def,  Speed,  Generation,  Legendary, Name,  Type 1,  Type 2, ad, ads_01, ads

    elif pokenew > 100: # saving the file with changes

        poke.to_csv("pokenew.csv", index=False)  


# pokenew end here.........................................

try_stuff = 0

if try_stuff == 10:
    var1 = pd.Series(([1, 3, 5, 7], [2, 4, 6, 8])) 
    var2 = pd.Series([1, 3, 5, 7], [2, 4, 6, 8]) # basic
    print(var1, type(var1))
    print(var2, type(var2)) # This () makes lots of difference

elif try_stuff == 20:
    date1 = pd.date_range("20021215", periods=8, freq="D", normalize=4)
    date2 = pd.date_range("20000201", "20000216")
    print(date1)
    print(date2)

elif try_stuff == 30: # making table
    random_int = np.random.randint(1, 9, size=(9, 4)) # rows first(left to right)
    list1 = [s for s in range(1, 10)]
    table1 = pd.DataFrame(random_int) # basic
    table2 = pd.DataFrame(random_int, index=list1)
    table3 = pd.DataFrame(random_int, columns=["A", "B", "C", "D"])
    table4 = pd.DataFrame(random_int, index=list1, columns=["A", "B", "C", "D"])
    print(table4)
    table4["T"] = table4.iloc[:, :].sum(axis=1)
    table4["M"] = table4.iloc[:, :].mean(axis=1)
    print(table4)

# try_stuff end here.........................................

try_graph = 10

if try_graph == 10:
    pass
    y_axis = {"f(x)": [2, 4, 6, 9], "g(x)": [-1, 3, -2, 1]}
    x_axis = [1, 5, 7, 9]
    graph1 = pd.DataFrame(y_axis, x_axis) # values, index
    graph1.plot(kind="line", grid=True)
    print(graph1.plot(kind="line"))




