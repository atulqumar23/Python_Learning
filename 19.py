'''19. Add a new column that flags each contract as 'ITM' (In The Money) or 'OTM' (Out of 
The Money): 
• Requires input spot prices. 
• For CE: if strike < spot → ITM; else → OTM 
• For PE: if strike > spot → ITM; else → OTM 
• Use these rules to generate a new column 'Moneyness'.'''

spot_price_m = float(input("Enter spot price for moneyness: "))
moneyness_list = []
with open(R"E:\SEPTEMBER\contract_file\contract -3.txt") as data:
    for row in data:
        if len(row) > 8 and row[3] != "" and row[7] != "" and row[8] != "":
            strike = float(row[7])
            opt_type = row[8]
            if opt_type == "CE":
                if strike < spot_price_m:
                    print("ITM")
                else:
                    print("OTM")
                status = "ITM" if strike < spot_price_m else "OTM"
            elif opt_type == "PE":
                status = "ITM" if strike > spot_price_m else "OTM"
        else:
            status = ""
        moneyness_list.append((row[3], strike, opt_type, status))
print(moneyness_list)