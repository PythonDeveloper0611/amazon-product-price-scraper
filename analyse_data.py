import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
connection = sqlite3.connect('amazon_scraper.db')

# Load the data into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM products", connection)

# Close the database connection
connection.close()

# Display the first few rows of the DataFrame
print(df.head())

# Data Analysis and Visualization

# Convert price to numeric (remove commas and convert to float, handle missing values)
df['price'] = df['price'].str.replace(',', '', regex=True).astype(float, errors='ignore')

# Histogram of product prices
plt.figure(figsize=(10, 6))
sns.histplot(df['price'].dropna(), bins=20, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Bar chart of product availability
availability_counts = df['availability'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=availability_counts.index, y=availability_counts.values)
plt.title('Product Availability')
plt.xlabel('Availability')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Convert reviews column to numeric (extract digits, handle missing values)
df['reviews'] = df['reviews'].str.replace(',', '', regex=True).str.extract(r'(\d+)')  # FIXED: Used raw string
df['reviews'] = pd.to_numeric(df['reviews'], errors='coerce')

# Scatter plot of price vs. reviews
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['reviews'], y=df['price'])
plt.title('Price vs. Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.show()
