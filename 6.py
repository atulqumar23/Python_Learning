'''6. Convert the `XpryDt` column from Unix timestamp (seconds since epoch) to human
readable date: 
• Use `datetime.fromtimestamp()` to convert each value into proper date format 
like YYYY-MM-DD.'''

import pandas as pd
from datetime import datetime
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
with open(file_path, 'r') as file:
    for line in file:
        file_data = line.strip().split("|")
        if len(file_data) < 40 :
            continue
        expriy_time = int(file_data[26])
        readable_td = datetime.fromtimestamp(expriy_time).strftime("%Y-%m-%d %H:%M:%S")
        print(readable_td)

################################################################

df = pd.read_csv(file_path, sep="|", header= None, skiprows=1)
df[26] = pd.to_datetime(df[26])
print(df[26])