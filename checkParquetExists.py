import pandas as pd


df_check = pd.read_parquet("street_names.parquet")
print("--- VERIFYING PARQUET CONTENT ---")
print(df_check)