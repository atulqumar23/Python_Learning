import pandas as pd
company_dict = {"hcl": [1500, 3000, 2500, 4000],
                "tcs": [1300,1200,1100,1000],
                "chetu": [500,800,900,700]
                }
df = pd.DataFrame(company_dict)
# df.to_csv("new.csv", index=False)
df.to_csv("new.csv", index= False, header=["a","b","c"])
print(df)



