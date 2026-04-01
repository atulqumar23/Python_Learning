'''11. Determine the lot size for each unique ticker symbol and save the results in a CSV file: 
• Extract unique combinations of ticker symbol and lot size. 
• Save the output in the format: Symbol, LotSize using `to_csv()` or file write 
methods. '''

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
symbol_lots = {}
ff = set()

with open(file_path, "r") as f:
    for line in f:
        row = line.strip().split('|')
        if len(row) > 31:  # Lot size is at index 24
            symbol = row[3]   # Ticker symbol
            lot_size = row[30]
            gg = (symbol, lot_size)
            if gg not in ff:
                ff.add(gg)
            # if symbol and lot_size:
            #     symbol_lots[symbol] = lot_size  # Keep unique pair

for k,l in ff:
    print(l)
# print(ff)

# with open("lot_sizes.csv", "w") as out:
#     out.write("Symbol,LotSize\n")
#     for sym, lot in symbol_lots.items():
#         out.write(f"{sym},{lot}\n")

        
##################################################


# import pandas as pd
# df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)
# unique_lot = df[df[3], df[30]].drop_duplicates().dropna()
# unique_lot.columns = ['Symbol', 'Lotsize']
# unique_lot.to_csv("Lot_size.csv", index=False)







