import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect('amazon_scraper.db')

# Load the data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM products", connection)

# Close the database connection
connection.close()

# Export the data to a CSV file
df.to_csv('amazon_products.csv', index=False)
print("✅ Data exported to amazon_products.csv")