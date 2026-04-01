# arithmetic operation in pnadas
import pandas as pd
num1_dict  = {"A": [1,2,3,4],"B": [4,5,6,7]}
num1 = pd.DataFrame(num1_dict)
num1["C"] = num1["A"] + num1["B"]
print(num1)
# print(num1_dict)
# num1["D"] = num1["A" + "B"]
num1["big"] = (num1["A"] <=6) & (num1["B"] <= 6)
print(num1)

