import sqlite3
import subprocess
import time
import re

def check_api_key():
    conn = None
    try:
        conn = sqlite3.connect('api_keys.db')
        cursor = conn.cursor()
        cursor.execute("SELECT key FROM api_keys")
        keys = cursor.fetchall()
        
        # Manually set values to check
        api_key = "YOUR_API_KEY" # Replace with your API key
        
        # Convert keys to a list of strings
        keys = [key[0] for key in keys]
        
        # Check if api_key exists in keys list
        if api_key in keys:
            run_main()
        else:
            print("Error: 1001 api key does not exist.")
    except sqlite3.Error as e:
        print("Error: An error occurred while accessing the database:", e)
    finally:
        if conn:
            conn.close()

def run_main(): # if true run the server for communication
    try:
        subprocess.call(["python", "path/to/main.py"]) # Replace with the path to your main.py file
    except subprocess.CalledProcessError as e:
        print("Error: An error occurred while running main.py:", e)

while True:
    check_api_key()
    time.sleep(360) # time in second before re verification of the api key