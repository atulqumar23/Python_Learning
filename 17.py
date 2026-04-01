'''17. Filter contracts where the strike price falls within ±5% of a given spot price: 
• Accept a spot price input. 
• Compute lower and upper bounds as 95% and 105% of the spot price. 
• Filter rows where `StrkPx` falls in this range and display the output. '''

file = R"E:\SEPTEMBER\contract_file\contract -3.txt"
spot_bound = []

# Read strike prices from txt (column 7, zero-based index)
with open(file, 'r') as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) < 8:
            continue
        strike = parts[7]  # column 8
        try:
            spot_bound.append(float(strike))
        except ValueError:
            continue
# print(spot_bound)
spot_price = float(input("enter a spot price "))
lower_bound = 0.95 * spot_price
upper_bound = 1.05 * spot_price
# print(f"{lower_bound} and {upper_bound}")

# Filter results
filtered = []
for s in spot_bound:
    if lower_bound <= s <= upper_bound:
        filtered.append(s)
# print(filtered)
print("Filtered Strike Prices:")
for s in filtered:
    print(s)


