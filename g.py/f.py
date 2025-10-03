import pandas as pd
spot_bound = []
file = R"E:\SEPTEMBER\contract_file\contract -3.txt"
with open(file,'r') as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) < 10 :
            continue
        strike = parts[7]
        # print(strike)
        spot_bound.append(float(spot_bound))
# print(spot_bound)
spot_price = float(input("enter a spot price "))
lower_bound = 0.95 * spot_price
upper_bound = 1.05 * spot_price
print(f"{lower_bound} and {upper_bound}")
count = pd.DataFrame(spot_bound, columns=["StrxPx"])
print(count)
fillered = count[(count["StrxPx"] >= lower_bound) & (count["StrxPx"]<= upper_bound)]
print(fillered)


