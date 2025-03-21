import sqlite3

#Function to fetch and display stored product data
def display_stored_data():
    connection = sqlite3.connect('amazon_scraper.db')
    cursor = connection.cursor()

   #cursor.execute("SELECT title, price, reviews, availability, created_at FROM products")
    rows = cursor.fetchall()

    if not rows:
        print("⚠️ No data found in the database.")
    else:
        print("\n📦 **Stored Product Data:**\n" + "-" * 80)
        for row in rows:
            title, price, reviews, availability, created_at = row
            print(f"🔹 **Title:** {title}")
            print(f"   💰 **Price:** {price}")
            print(f"   ⭐ **Reviews:** {reviews}")
            print(f"   🛒 **Availability:** {availability}")
            print(f"   ⏳ **Added On:** {created_at}")
            print("-" * 80)

    cursor.close()
    connection.close()


# Call the function to clean up the database
#remove_duplicates()

# Call the function to display data
display_stored_data()
