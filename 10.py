'''10. Replace all occurrences of 'XX' with 'FF' in the `Srs` column: 
• This can be done using pandas `str.replace('XX', 'FF')` function to clean the series 
column.'''

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
with open(file_path, 'r') as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) < 5 :
            continue
        series = file_data[4]
        if series == 'XX':
            series = 'FF'
        print(series)



####################################################
import pandas as pd
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
df = pd.read_csv(file_path,sep= "|", header=None, skiprows= 1)
# df[4] = df[4].astype(str).str.strip()
df[4] = df[4].str.strip().replace('XX', 'FF' , regex= False)
print(df[4])