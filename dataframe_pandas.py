# DataFrame is two Dimensional
# and no of date must be equal otherwise it will throw error 
import pandas as pd
numbers = [4,5,6,7,8]
num = pd.DataFrame(numbers)
print(num)


num_dict = {"a":[2,3,4,5,6], "b": [7,8,9,4,5]}
num1 = pd.DataFrame(num_dict)
print(num1["a"])
print(num1["a"][3])

numbers1 = [5,5,15,14,25]
num2 = pd.DataFrame(numbers1)

print(numbers1 + numbers)