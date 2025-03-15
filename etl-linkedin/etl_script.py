import pandas as pd
from helpers import days_published, date_published, extract_num_from_str
from store import store_jobs

# Load CSV data
df = pd.read_csv("jobs-webdeveloper.csv")

# df.head(5)
# Data Cleaning
df = df.drop_duplicates(subset=["url"])

# Published date
# df["published"] = df["published"].apply(days_published)
# df["published"] = df["published"].apply(date_published)
# Aplicar las funciones encadenadas en una sola línea
df["published"] = df["published"].apply(lambda x: date_published(days_published(x)))
df["applicants"] = df["applicants"].apply(extract_num_from_str)

# print(df.columns)
# print(df.iloc[ :5 , 4])

store_jobs(df)