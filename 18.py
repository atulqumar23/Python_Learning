'''18. Identify the top 3 expiry dates that have the highest number of contracts: 
• Group the dataset by expiry date. 
• Count the number of rows for each expiry. 
• Sort and display the top 3 based on count. '''

from datetime import datetime
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
expiry_dates = {}

# Read the file skipping the first line and extract expiry dates
with open(file_path, 'r') as file:
    next(file)  # skip header or first line
    for line in file:
        parts = line.strip().split('|')
        if len(parts) > 55:
            xpriy_date = int(parts[48])
            xpriy_datetime  = datetime.fromtimestamp(xpriy_date).strftime("%Y-%m-%d %H:%M:%S")
            # expiry_dates.append(xpriy_datetime)
            if xpriy_datetime in expiry_dates:
                expiry_dates[xpriy_datetime] += 1
            else:
                expiry_dates[xpriy_datetime] = 1
print(expiry_dates)

# Create a DataFrame from expiry dates
# df_expiry = pd.DataFrame(expiry_dates, columns=['expiry_date'])

# # Count the number of contracts per expiry date
# expiry_counts = df_expiry['expiry_date'].value_counts()

# # Get top 3 expiry dates
# top_3_expiry = expiry_counts.head(3)

# print(top_3_expiry)
import pandas as pd

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
df = pd.read_csv(file_path, sep="|", header=None, skiprows=1)

# Column 48 ko datetime me convert karo, errors waise hi skip ho jaye
df[48] = pd.to_datetime(df[48], errors="coerce")

# NaT (missing dates) ko drop karo
valid_dates = df[48].dropna()

# Frequency ke hisaab se top 3 expiry dates
top_3_by_count = valid_dates.value_counts().head(3)
print("Top 3 frequent expiry dates:\n", top_3_by_count)

# Chronologically nearest 3 expiry dates
nearest_3_dates = valid_dates.sort_values().head(3)
nearest_3_counts = nearest_3_dates.value_counts()
print("\nNearest 3 expiry dates with count:\n", nearest_3_counts)

