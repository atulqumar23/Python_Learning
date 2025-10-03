'''7. Adjust the converted expiry dates by adding a base date “01-01-1980”: 
• Convert the base date to `datetime` and add it to the timestamp-derived date. 
• Useful if the date was meant to be an offset from a different origin. '''

from datetime import datetime, timedelta

# Step 1: Define the base date
base_date = datetime(1980, 1, 1)

# Step 2: Read the file and extract expiry dates (XpryDt at index 6)
file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
expiry_dates = []

with open(file_path, "r") as f:
    for line in f:
        row = line.strip().split('|')
        if len(row) > 6 and row[6] != "":
            # Convert Unix timestamp to datetime
            dt = datetime.fromtimestamp(int(row[6]))
            expiry_dates.append(dt)

# Step 3: Adjust each expiry date by adding the base date offset
# We calculate the offset from 1970-01-01 (Unix epoch) to base_date
epoch = datetime(1970, 1, 1)
offset = base_date - epoch

adjusted_dates = [dt + offset for dt in expiry_dates]

# Step 4: Print sample adjusted dates
for dt in adjusted_dates[:5]:
    print(dt.strftime("%Y-%m-%d"))
