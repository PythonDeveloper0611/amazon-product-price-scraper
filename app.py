from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

# Function to load data from SQLite database
def load_data():
    connection = sqlite3.connect('amazon_scraper.db')
    df = pd.read_sql_query("SELECT * FROM products", connection)
    connection.close()
    return df

@app.route('/')
def index():
    df = load_data()
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)