# series is one dimensional array like one column
# it's is first strat of pandas
# syntax like pd.Series


import pandas as pd
# x = [4,5,6,7,8]
# y = pd.Series(x, index=["a",'b','c','d','e'], dtype=float)
# print(y)
# print(type(y))
# print(y[2])


x1 = pd.Series(5, index=[1,2,3,4,5,6,7,8,9])
# print(x1)
x2 = pd.Series(14, index=[4,5,6,7])
print(x1+x2)



name_dict = {"name": ["python","c","c++","java"], "rank":[1,4,3,2]}
name_var = pd.Series(name_dict)
print(name_var.iloc[1])