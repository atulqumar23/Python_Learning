'''13. Given a specific expiry date, list all contracts that match the given expiry: 
• Convert the expiry column to dates. 
• Compare it with the input date and filter matching rows. '''

from datetime import datetime

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"

expiry_to_check = str(input("enter a date : "))   # input expiry date

results = []

with open(file_path, "r") as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) > 6: #and parts[6].isdigit():
            ts = int(parts[6])
            expiry_date = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            
            if expiry_date == expiry_to_check:
                results.append(line.strip())

# print matching contracts
for r in results:
    print(r)

##########################################################################
import pandas as pd

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"

expiry_to_check = input("Enter a date (YYYY-MM-DD): ")  # input expiry date
df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)

# Filter rows matching the input expiry date
filtered = df[pd.to_datetime(df[6], unit="s", errors="coerce").dt.strftime("%Y-%m-%d") == expiry_to_check]

print(filtered)



