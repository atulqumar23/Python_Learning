'''15. Write all generated contract strings (from question 14) into a new text file, each on a 
separate line: 
• Use a loop or pandas `.to_csv()` method with no headers and index to save the 
lines.'''

import pandas as pd

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)

# Convert datetime column
df[48] = pd.to_datetime(df[48], errors="coerce")
df[48] = df[48].dt.strftime('%Y-%m-%d')
mask = (
    df[3].notna() & (df[3] != "") & (df[3] != "0") &
    df[48].notna() & (df[48] != "0") &
    df[7].notna() & (df[7] != "") & (df[7] != "0") &
    df[8].notna() & (df[8] != "") & (df[8] != "0")
)

df = df[mask]

# make contract string
df["ContractString"] = (
    df[3].astype(str) + "|" +
    df[48].astype(str) + "|" +
    df[7].astype(str) + "|" +
    df[8].astype(str)
)

# Save output
df["ContractString"].to_csv("output_contracts.txt", index=False, header=False)


