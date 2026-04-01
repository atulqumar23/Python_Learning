'''Read the contract file using three different methods: 
• Using the basic `open()` method to manually open the file and read it line-by-line 
• Using the 'with open() as' context manager to ensure the file is automatically closed 
after reading. 
• Using pandas `read_csv()` to load the contract file as a DataFrame which allows for 
easy data analysis and manipulation.'''




# # ----------- 1. Using basic open() method -----------
file_path = "contracts.txt"

f = open(file_path, "r")
lines = f.readlines()     
f.close()                 
print("Total lines read:", len(lines))
print("First line:", lines[0].strip())


# # ----------- 2. Using with open() as (context manager) -----------
with open(file_path, "r") as f:   
    for line in f:
       print(line)


# ----------- 3. Using pandas read_csv() -----------
import pandas as pd
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)
# print("Shape of DataFrame:", df.shape)
print(df)
