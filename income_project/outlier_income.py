
#to use : from income_project.outlier_income import df

import numpy as np
from income_project.intro_income import df
# to run: python3 -m income_project.outlier_income

out_liers_ = []

def find_outlier(x): # z_score method 

    threshold = 2.5 # limit 
    means = np.mean(x)
    stds  = np.std(x)
    #print("means :", means, "stds :", stds, "threshold :", threshold)

    for i in x:
        z_score = (i - means)/stds
        if np.abs(z_score) > threshold:
            out_liers_.append(i)

    return min(out_liers_)


# .................................................................

out_liers_77 = []

def iqr_method(y): # iqr method
    quantile1, quantile3 = np.percentile(y, [25, 75])
    #print("quantile1 :", quantile1,"quantile2 :", quantile3)
    iqr_value = quantile3 - quantile1
    #print("iqr_value :", iqr_value)

    lower_val = quantile1 - (1.5*iqr_value)
    upper_val = quantile3 + (1.5*iqr_value)
    #print("lower_val :", lower_val, "upper_val :", upper_val)

    for i in y:
        if i < lower_val:
            out_liers_77.append(i)
        elif i > upper_val:
            out_liers_77.append(i)

    return min(out_liers_77)


df_sorted = sorted(df["age"])
max_age = iqr_method(df_sorted) # age = 79
# print("age to remove from :", max_age) 

df = df.drop(df[df.age >= max_age].index) # (age >= 79) == drop

# print("Done ...")


