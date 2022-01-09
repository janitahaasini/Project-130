import pandas as pd
import csv
df=pd.read_csv("merged_data.csv")

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Luminosity"]
print(df.shape)
df.to_csv("final_output.csv")