import sqlite3

def init_db():
    # This creates the connection to the database file
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    # Use SQL commands to create structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized and table created.")

if __name__ == "__main__":
    init_db()