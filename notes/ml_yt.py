
# firstly we import all in standard form

#import pandas as pd
#import quandl 
#import math

"""
# df = quandl.get("BBSE/BOM530393")
df = quandl.get("BSE/BOM530393") # df = data_frame
# Open, High, Low, Close, WAP, No. of Shares, No. of Trades, Total Turnover, 
# Deliverable Quantity, % Deli. Qty to Traded Qty, Spread H-L, Spread C-O.

df["vol"] = df["No. of Shares"] # volume = No. of Shares
df = df[["Open", "High", "Low", "Close", "vol"]]

# Briefly, feature is input; label is output. Applies to classification And regression problems.
# hence here close, vol = feature and hlow, change = lable
df["hlow"] = (df["High"] - df["Close"])/df["Close"]*100.0 # percentage difference of (H-L) 
df["change"] = (df["Close"] - df["Open"])/df["Open"]*100.0 # percentage difference of (C-O) 
# Open, High, Low, Close, vol, hlow, change

df = df[["Close", "vol", "hlow", "change"]]

# print(df)

forcest_coloum = "Close"
df.fillna(-9999, inplace=True)
forcest_out = int(math.ceil(0.1*len(df)))

""" # started from p7 and hope to get back

# from now on i'll mention things video(p-?) vise
# in p7
VIDEO = 0
if VIDEO == 10:
    pass
    # as we know y = mx + c (we just need to find m and c)
    # c = {y} - m{x} .... here {} = mean of, {a} = mean of a
    # m = [{x}*{y} - {xy}] / [{x}^2 - {x^2}] ..... {} = mean of

# in p8

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

if VIDEO == 0:
    
    x_values = np.array([2, 3, 4, 5, 6], dtype=np.float64) # some random values
    y_values = np.array([5, 4, 7, 6, 8], dtype=np.float64)

    if VIDEO > 20: # just to enjoy graph
        plt.scatter(x_values, y_values)
        print(plt.show())  

    def best_fit_line(xs, ys): # to get m, c
        
        m = ( ( (mean(xs)*mean(ys)) - mean(xs*ys) ) /
            ( (mean(xs)**2) - mean(xs*xs) ) ) # formula to find m

        c = mean(ys) - m*mean(xs) # formula for c = y -mx
        # m, c == 0.8000000000000007, 2.799999999999997 
        return m, c  

    m, c = best_fit_line(x_values, y_values)
    # print(m, c)

    # p9
    regression_line = [(m*x + c) for x in x_values] # line we wanted
    # regressione line = best fit line = Y hat (all are same)
    # print(regression_line)

    from  matplotlib import colors, style

    predict_x = 7 # value of x for which we need to predict y
    predict_y = m*predict_x + c
    
    if VIDEO > 10: # just to see the graph
        
        style.use("fivethirtyeight")
        plt.scatter(x_values, y_values,)
        plt.plot(x_values, regression_line)
        plt.scatter(predict_x, predict_y, color="r")
        print(plt.show())
        

# p10
# here was just simple explation about e^2 and r^2
# r^2 = 1 - ((e^2 of regression) / (e^2 of mean of y))
# e^2 = [(values_of_regression_line - values_of_y_orignal)]
# working in p11

# p11
def square_error(ys_orignal, ys_line):

    return sum((ys_line - ys_orignal)**2)

def coffecint_of_detemination(ys_orignal, ys_line):
    y_mean_line = [mean(y) for y in ys_orignal]
    pass


val = [2.0, 4.0, 6.0, 8.0]
f_mean = [( mean (f) for f in val )]
f_list = list(f_mean) + [0, 8]
fv = (i for i in f_list)

print(fv.__next__())
print(f_mean)
print(i for i in f_list)




