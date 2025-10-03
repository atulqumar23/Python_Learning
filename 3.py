'''Find all the unique strike prices: 
• Similar to the ticker symbol task, use `set()` or `list` methods to remove duplicate 
strike values from the 'StrkPx' column. 
• Using pandas, you can also apply `drop_duplicates()` to get a unique list of strike 
prices.'''

file_path  = R"E:\SEPTEMBER\contract_file\contract -3.txt"
unique_StrkPx = set()
with open(file_path, 'r') as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) < 10 :
            continue
        strike_price = file_data[7].strip()
        if strike_price == "":
            continue
        unique_StrkPx.add(strike_price)
print(unique_StrkPx)


# #########################################

unique_StrkPx_list = []
with open(file_path, 'r') as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) < 10 :
            continue
        strike_price = file_data[7].strip()
        if strike_price != "" and strike_price not in unique_StrkPx_list:
            unique_StrkPx_list.append(strike_price)
print(unique_StrkPx_list)


####################################################


import pandas as pd
df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)
df[7] = pd.to_numeric(df[7], errors="coerce")
uinque_stk_px = df[7].drop_duplicates().dropna()
print(uinque_stk_px)

          

