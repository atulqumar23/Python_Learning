'''14. For each row, create a string combining `TckrSymb`, `XpryDt`, `StrkPx`, and `OptnTp`, 
separated by a pipe character '|': 
• Example output: NIFTY|2025-05-08|19500|CE 
• Add this new formatted column to the DataFrame. 
'''

import pandas as pd
from datetime import datetime
with open(R"E:\SEPTEMBER\contract_file\contract -3.txt", 'r') as file:
    for line in file:
        parts=  line.strip().split("|")
        if len(parts) < 54 :
            continue
        symbol = parts[3].strip()
        if symbol == "0" or symbol == "":
            continue
        # print(symbol)
        expiry = int(parts[26])
        if expiry == "0" or expiry == "":
            continue
        # print(expiry)
        dt = datetime.fromtimestamp(expiry).strftime("%Y-%m-%d")
        strike = parts[7].strip()
        if strike == "0" or strike == "":
            continue
        option_type = parts[8].strip().replace('XX', 'FE')
        # print(option_type, end="")
        if option_type == '-1' or option_type == "":
            continue
        print(f"{symbol}|{dt}|{strike}|{option_type}")

####################################################################

file_path =R"E:\SEPTEMBER\contract_file\contract -3.txt"
df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)
df[48] = pd.to_datetime(df[48], errors="coerce") 

# Create new column with formatted string
df['Formatted'] = df[3].astype(str) + '|' + \
                  df[48].dt.strftime('%Y-%m-%d') + '|' + \
                  df[7].astype(str) + '|' + \
                  df[8].astype(str).replace('XX', 'FE')
print(df['Formatted'])
