
# firstly we import all in standard form

 
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

VIDEO = 1000

if VIDEO == 1000:
    
    import pandas as pd
    import quandl 
    import math
    
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

    forcest_coloum = df["Close"]
    df.fillna(-9999, inplace=True)
    forcest_out = int(math.ceil(0.01*len(df)))

    df["label"] = df[forcest_coloum].shift(-forcest_out)
    df.dropna(inplace=True)
    print(df.tail())


# started from p7 and hope to get back

# from now on i'll mention things video(p-?) vise

# in p7 
if VIDEO == 10:
    pass
    # as we know y = mx + c (we just need to find m and c)
    # c = {y} - m{x} .... here {} = mean of, {a} = mean of a
    # m = [{x}*{y} - {xy}] / [{x}^2 - {x^2}] ..... {} = mean of

# in p8
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
    # r^2 = 1 - ((e^2 of regression line) / (e^2 of mean of y))
    # e^2 = [(values_of_regression_line - values_of_y_orignal)]
    # working in p11

    # p11 .....................................................................
    def square_error(ys_orignal, ys_line): # here (orignal, lines) are just some variable
    # e**2 = distance b/w given line and points(y-axis distance, not parpendecular)
        return sum((ys_line - ys_orignal)**2)  
 
    def coffecint_of_detemination(ys_orignal, ys_line): # coffecint_of_detemination = r**2
    # ys_orignal = values of y's and ys_line = regression_line(line we found)
        y_mean_line = [mean(ys_orignal) for y in ys_orignal] # y_mean_line = [6, 6, 6, 6, 6]
        square_error_regression = square_error(ys_orignal, ys_line) 
        square_error_y_mean_line = square_error(ys_orignal, y_mean_line) # only line difference
        return 1 - (square_error_regression / square_error_y_mean_line)

    r_square = coffecint_of_detemination(y_values, regression_line)

    print(r_square*100) # percentage accuracy here = 64% (wooow!!)
 
    # p12 creating more data ...........................................
    import random

    def create_dataset(how_many, variance, step=2, correlation=False): # variance = random variable
        pass
        val = 1
        y_new = []
        for i in range(how_many):
            y = val + random.randrange(-variance, +variance)
            y_new.append(y)
            if correlation == "pos":
                val+= step

        x_new = [i for i in range(len(y_new))]
        return np.array(x_new), np.array(y_new)

    x_new, y_new = create_dataset(50, 20, 2, correlation="pos")

    new_line = [(m*x + c) for x in x_new] # m, c = 0.8000000000000007, 2.799999999999997

    style.use("fivethirtyeight")
    plt.scatter(x_new, y_new)
    plt.plot(x_new, new_line)
    # plt.plot(x_values, regression_line)
    # plt.scatter(predict_x, predict_y, color="r")
    print(plt.show())
   
 

























print("End Here")

