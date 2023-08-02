import sqlite3

# Connect to the database (will create a new file if it doesn't exist)
conn = sqlite3.connect('python_project3/quiz_app.db')
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create a table to store quiz attempts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz_attempts (
        attempt_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

conn.commit()
