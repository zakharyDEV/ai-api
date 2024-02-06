import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import sqlite3

def generate_key():
    key = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for _ in range(4):
        for _ in range(4):
            key += random.choice(characters)
        key += '-'
    key += random.choice(characters)
    return key

def save_to_database(key):
    conn = sqlite3.connect('api_keys.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS api_keys (key TEXT)")
    cursor.execute("INSERT INTO api_keys VALUES (?)", (key,))
    conn.commit()
    conn.close()

def button_click():
    key = generate_key()
    save_to_database(key)
    messagebox.showinfo('API Key', f'Generated API Key: {key}')
    button.config(text='Copy API Key', command=lambda: copy_key(key))
    print(f"Generated API Key: {key}")

def copy_key(key):
    window.clipboard_clear()
    window.clipboard_append(key)
    window.update()
    messagebox.showinfo('API Key', 'API Key copied to clipboard!')
    print("API Key copied to clipboard!")

window = tk.Tk()
window.title('API Key Generator')

button = tk.Button(window, text='Generate API Key', command=button_click)
button.pack(pady=20)

window.mainloop()