# this script try to fix jobs.csv files containing row with missing or erroneous data  

from scripts.csv_handler import csv_to_df
from scripts.job import job_search

filename = 'jobs-nest.js.csv'

df = csv_to_df(filename)

def update_dataframe(df):
    """Iterate over the DataFrame and update rows where 'title' is empty or invalid."""
    
    for index, row in df.iterrows():
        if not isinstance(row["title"], str) or not row["title"].strip():  # Check if 'title' is empty or invalid
            new_values = job_search(row["url"])  # Scrape data

            if new_values is None or len(new_values) != len(df.columns):  # Validate result
                print(f"Warning: Skipping row {index} due to invalid job_search() result.")
                continue  # Skip if invalid

            df.loc[index] = new_values  # Replace the entire row with new data

    return df


df = update_dataframe(df)

df.to_csv(filename)