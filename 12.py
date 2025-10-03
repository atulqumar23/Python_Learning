'''12. Given an `undrlygFinInstrmId`, retrieve and display all related contract details: 
• Accept input from user. 
• Filter the DataFrame to rows where `undrlygFinInstrmId` matches the input. 
• Show relevant columns like symbol, expiry, strike, option type, etc. '''

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
random_InstrmId = input("enter a strike price : ")
match_contract = []
with open(file_path, 'r') as file:
    next(file)
    for line in file :
        parts = line.strip().split("|")
        if len(parts) < 10:
            continue
        undrlygFinInstrmId = parts[1].strip()
        if undrlygFinInstrmId == random_InstrmId:
            match_contract.append(line.strip())
print(match_contract)


################################################################
# import pandas as pd

# file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
# random_strike = input("Enter a strike price: ") 

# # Read file
# df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)

# # Filter rows where column 1 matches input
# filtered = df[df[1].astype(str) == random_strike]

# # Convert to list of rows (optional)
# new = filtered.values.tolist()

# print(new)



