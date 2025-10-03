'''16. Group all contracts by Ticker Symbol and Option Type (CE/PE) and count the number of 
contracts in each group: 
• Use `groupby(['TckrSymb', 'OptnTp'])` followed by `.size()` to get the count per 
group. 
• Helps analyze market interest per symbol/type combination.'''

import pandas as pd
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
df  = pd.read_csv(file_path, sep="|", header=None, skiprows=1)
grouped_counts = df.groupby([df[3],df[8].replace('XX','FE')]).size()
print(grouped_counts)

##############################################################

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
grouped_counts = {}
# Read the file and skip the first line (header)
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()[1:]
    for line in lines:
        columns = line.strip().split('|')
        # Ensure columns 3 and 8 exist
        if len(columns) > 8:
            symbol_col = columns[3].strip()
            if symbol_col == "":
                continue
            opt_type = columns[8].strip()
            if opt_type == "":
                continue
            key = (symbol_col,opt_type)
            if key in grouped_counts:
            # print(key)
                grouped_counts[key] += 1
            # print(key, end="")
            else:
                grouped_counts[key] = 1

#Print grouped counts
for key, count in grouped_counts.items():
    print(f"{key}: {count}")


###########################################################
from collections import Counter

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()[1:]  # header skip

    pairs = []
    for line in lines:
        columns = line.strip().split('|')
        if len(columns) > 8:
            symbol_col = columns[3].strip().replace('XX','FE')
            opt_type = columns[8].strip()
            if symbol_col != "" and opt_type != "":
                pairs.append((symbol_col, opt_type))   # tuple bana diya

grouped_counts = Counter(pairs)

# Print result
for key, count in grouped_counts.items():
    print(f"{key}: {count}", end="")
