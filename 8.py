'''8. Find the nearest (minimum) expiry date among all contracts: 
• After converting expiry dates, use the `min()` function to find the nearest expiry in 
the data. '''

import pandas as pd
df = pd.read_csv(
    R"E:\SEPTEMBER\contract_file\contract -3.txt",
    sep="|",          # pipe separator
    header=None,      # column names nahi hain
    skiprows=1        # first line skip kar do
)
df[6] = pd.to_datetime(df[6], errors="coerce", unit="s")

# nearest expiry date nikalna
nearest_expiry = df[6].min()
print("Nearest expiry date:", nearest_expiry)

###############################################

from datetime import datetime

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"

expiry_list = []

with open(file_path, "r") as f:
    next(f)  # skip first line
    for line in f:
        parts = line.strip().split("|")  # pipe separator
        if len(parts) > 6 and parts[6]:  # column 6 exist kare aur empty na ho
            try:
                # Convert Unix timestamp (seconds) to datetime
                dt = datetime.fromtimestamp(int(parts[6]))
                expiry_list.append(dt)
            except ValueError:
                pass  # invalid timestamp skip kar do

# nearest expiry
if expiry_list:
    nearest_expiry = min(expiry_list)
    print("Nearest expiry date:", nearest_expiry.strftime("%Y-%m-%d"))
else:
    print("No valid expiry dates found.")


