'''2. Find all the unique ticker symbols in the file: 
• Extract the 'TckrSymb' column from the data. 
• Use Python’s built-in `set()` function to get distinct values. 
• Alternatively, convert the column to a list and remove duplicates manually using a 
loop. 
• This helps identify all different symbols available in the contracts.'''
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
with open(file_path, "r") as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) > 10:
            
            ticker_symbol = file_data[3].strip()
            if ticker_symbol == "" or ticker_symbol == 0:
                continue
            print(ticker_symbol)



###########################################################
unique_symbol = set()
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
with open(file_path, "r") as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) > 10:
            
            ticker_symbol = file_data[3].strip()
            if ticker_symbol == "" or ticker_symbol == 0:
                continue
            unique_symbol.add(ticker_symbol)
print(unique_symbol)


##############################################

unique_list = []
with open(file_path, "r") as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) > 10:
            ticker_symbol = file_data[3].strip()
            if ticker_symbol != "" and ticker_symbol not in unique_list:
                unique_list.append(ticker_symbol)

print(unique_list)

