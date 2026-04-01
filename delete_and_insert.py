import pandas as pd
new_dict = {
    "a": [1,2,3,4,5,6],
    "b": [5,6,7,8,9,10]
}
var = pd.DataFrame(new_dict)
# print(var)
# print(var['a'])
var.insert(2, 'new_clm', var['a'])
print(var)