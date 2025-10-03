'''9. For each unique ticker symbol, find its nearest expiry date: 
• Group data by ticker symbol. 
• For each group, find the nearest expiry date by using `min()` on the expiry date 
column.'''

from datetime import datetime

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"

expiry_dict = {}

with open(file_path, "r") as f:
    next(f)  # skip first line
    for line in f:
        parts = line.strip().split("|")
        if len(parts) > 48 and parts[48] and parts[3]:  # check columns exist aur empty na ho
            try:
                ticker = parts[3]
                expiry = datetime.fromtimestamp(int(parts[48]))
                if ticker in expiry_dict:
                    expiry_dict[ticker].append(expiry)
                else:
                    expiry_dict[ticker] = [expiry]
            except ValueError:
                pass  # invalid timestamp skip kar do

# nearest expiry per ticker
nearest_per_symbol = {ticker: min(dates) for ticker, dates in expiry_dict.items()}

# print nicely
for ticker, expiry in nearest_per_symbol.items():
    print(f"{ticker}: {expiry.strftime('%Y-%m-%d')}")


####################################################################
import pandas as pd

df = pd.read_csv(R"E:\SEPTEMBER\contract_file\contract -3.txt",
                 sep="|", header=None, skiprows=1)

# convert expiry column to datetime
df[48] = pd.to_datetime(df[48], errors="coerce")

# nearest expiry per ticker symbol (column 3)
nearest_per_symbol = df.groupby(3)[48].min()

print(nearest_per_symbol)
