import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Initialize database
def init_db():
    conn = sqlite3.connect("login_info.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to check login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect("login_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password!")

# Function to register user
def register():
    username = username_entry.get()
    password = password_entry.get()
    
    if username and password:
        try:
            conn = sqlite3.connect("login_info.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User registered successfully!")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            update_datagrid()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
    else:
        messagebox.showwarning("Warning", "Please enter both username and password")

# Function to update the DataGridView
def update_datagrid():
    conn = sqlite3.connect("login_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    # Clear existing data in DataGridView
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert new data into DataGridView
    for user in users:
        tree.insert("", tk.END, values=user)

# Initialize database
init_db()

# GUI setup
root = tk.Tk()
root.title("Login Page")
root.geometry("1000x600")
root.config(bg="green")

# Create main frame
main_frame = tk.Frame(root, bg="green")
main_frame.pack(fill="both", expand=True)

# Left Section - Image Display
left_frame = tk.Frame(main_frame, bg="orange", width=400, height=600)
left_frame.grid(row=0, column=0, sticky="nsew")

# Load and display an image
image_path = "login_image.png"  # Ensure this image exists in the project folder
try:
    image = Image.open(image_path)
    image = image.resize((350, 350), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(left_frame, image=image, bg="white")
    image_label.pack(pady=20)
except Exception:
    error_label = tk.Label(left_frame, text="Image not found", bg="white", fg="red", font=("Arial", 14))
    error_label.pack(pady=20)

# Right Section - Login Form
right_frame = tk.Frame(main_frame, bg="white", width=600, height=600)
right_frame.grid(row=0, column=1, sticky="nsew")

# Main Heading - LOGIN PAGE
heading_label = tk.Label(right_frame, text="LOGIN PAGE", font=("Arial", 20, "bold"), bg="white", fg="blue")
heading_label.grid(row=0, column=0, columnspan=2, pady=20)

# Labels and Entry Fields
tk.Label(right_frame, text="Username", bg="white", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(right_frame, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(right_frame, text="Password", bg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(right_frame, font=("Arial", 12), show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons - Now Side by Side in a Single Row
button_frame = tk.Frame(right_frame, bg="white")
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Login", command=login, font=("Arial", 12), bg="lightblue", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Register", command=register, font=("Arial", 12), bg="lightgreen", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Exit", command=root.quit, font=("Arial", 12), bg="lightcoral", width=10).pack(side=tk.LEFT, padx=5)

# DataGridView (Treeview) to display registered users
tree = ttk.Treeview(right_frame, columns=("ID", "Username", "Password"), show="headings", height=5)
tree.heading("ID", text="ID")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")
tree.grid(row=5, column=0, columnspan=2, pady=20)

# Update the DataGridView on startup
update_datagrid()

# Run the application
root.mainloop()
