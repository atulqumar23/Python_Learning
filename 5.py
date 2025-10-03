'''5. Count the number of unique symbols and the number of unique `undrlygFinInstrmId` 
values: 
• Use pandas `nunique()` method or convert the columns into sets to count unique 
values. 
• Helps understand the breadth of instruments and identifiers in the dataset.'''

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"

symbols_set = set()
underlyg_ids_set = set()

with open(file_path, 'r', encoding='utf-8') as file:
    # lines = file.readline()
    # next(file)
    for line in file:
        # print(line)
        parts = line.strip().split('|')
        if len(parts) > 3:
            underlygFinInstrmId = parts[1].strip()
            # if underlygFinInstrmId == "0":
            #     continue
            # print(underlygFinInstrmId)
            symbol = parts[3].strip()
            if symbol == "":
                continue
            symbols_set.add(symbol)
            underlyg_ids_set.add(underlygFinInstrmId)

print(f"Unique symbols count: {len(symbols_set)}")
print(f"Unique underlygFinInstrmId count: {len(underlyg_ids_set)}")



##########################################################################


import pandas as pd

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
df = pd.read_csv(file_path, sep='|', header=None, skiprows=1, encoding='utf-8')
df = df[[1, 3]]  
# df = df[df[3] != ""]  

# Count unique values using nunique()
unique_symbols_count = df[3].nunique()
unique_underlygFinInstrmId_count = df[1].nunique()

print(f"Unique symbols count: {unique_symbols_count}")
print(f"Unique underlygFinInstrmId count: {unique_underlygFinInstrmId_count}")

