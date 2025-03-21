import pandas as pd
import os

# ✅ Load the extracted data into a DataFrame
df = pd.read_csv("naukri_job_listings.csv")

# ✅ Display the job listings in a table format
from tabulate import tabulate
print("\n📄 Extracted Job Listings:\n")
print(tabulate(df, headers="keys", tablefmt="grid"))

# ✅ Open the CSV file in Excel (Windows)
os.startfile("naukri_job_listings.csv")
