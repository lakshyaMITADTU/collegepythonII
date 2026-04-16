import pandas as pd
df = pd.read_json("employees.json")
df.to_csv("employees.csv", index=False)
print("Conversion done successfully!")
