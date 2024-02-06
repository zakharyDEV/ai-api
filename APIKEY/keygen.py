import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import sqlite3

# Function to generate random API key
def generate_key():
    key = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for _ in range(4):
        for _ in range(4):
            key += random.choice(characters)
        key += '-'
    key += random.choice(characters)
    return key

# Function to save API key to SQLite database
def save_to_database(key):
    conn = sqlite3.connect('api_keys.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS api_keys (key TEXT)")
    cursor.execute("INSERT INTO api_keys VALUES (?)", (key,))
    conn.commit()
    conn.close()

# Function to handle button click event
def button_click():
    key = generate_key()
    save_to_database(key)
    messagebox.showinfo('API Key', f'Generated API Key: {key}')
    button.config(text='Copy API Key', command=lambda: copy_key(key))

# Function to copy API key to clipboard
def copy_key(key):
    window.clipboard_clear()
    window.clipboard_append(key)
    window.update()
    messagebox.showinfo('API Key', 'API Key copied to clipboard!')

# Create main window
window = tk.Tk()
window.title('API Key Generator')

# Create button
button = tk.Button(window, text='Generate API Key', command=button_click)
button.pack(pady=20)

# Run the main window
window.mainloop()