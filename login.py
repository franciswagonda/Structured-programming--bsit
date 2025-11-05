import sqlite3
import hashlib

# --- Database setup ---
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')
conn.commit()

# --- Helper to hash passwords ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Register function ---
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                       (username, hash_password(password)))
        conn.commit()
        print("✅ Registration successful!")
    except sqlite3.IntegrityError:
        print("⚠️ Username already exists!")

# --- Login function ---
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    if result and result[0] == hash_password(password):
        print(f"✅ Welcome back, {username}!")
    else:
        print("❌ Invalid username or password")

# --- Menu ---
while True:
    print("\n=== Login System ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")