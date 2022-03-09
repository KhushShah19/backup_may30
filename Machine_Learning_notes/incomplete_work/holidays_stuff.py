
import pandas as pd 

df = pd.read_csv("/home/groot/Downloads/holidays_events.csv")
#print(df.info())
#print(df.columns) # ['date', 'type', 'locale', 'locale_name', 'description', 'transferred']

#d1 = {} for i in df['transferred']:d1[i] = d1.get(i, 0) + 1, print(d1)
typed = {'Holiday': 1, 'Transfer': 2, 'Additional': 3, 'Bridge': 4, 'Work Day': 6, 'Event': 7}
localed = {'Local': 1, 'Regional': 2, 'National': 3} # making srt => int (readable form)

df = df.drop(columns =["locale_name", "description"])
#locale_name and description has to many different names, which won't be of mush use
#transferredd = {False: 338, True: 12}

df["locale"] =  df["locale"].replace(localed) 
df["type"] =  df["type"].replace(typed) # making them int64 (readable form)
df["date"] = pd.to_datetime(df["date"], dayfirst=False) # type = datetime64[ns]

print(type(df["date"]))
print(df.info())
#print(df.head())
#print(df.info()) # all this can be done with Only pandas liberay 

ml = 10 # here on ML starts ..........................................
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

if ml == 10: # regression 
    
    
    xre = np.array(df.drop(["transferred"], axis=1))
    #xre["date"] = xre["date"].to_numpy()
    print(xre)
    yre = np.array(df["transferred"])
    print(xre.shape) # (350, 3) == (rows --> , coloum)
    m1, m2, m3, cnp = np.polyfit(xre, yre, 3)
    print(m1, cnp)















