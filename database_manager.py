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

def add_item(name, qty):
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()
    # This command inserts new row of data into the table
    cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", (name, qty))
    conn.commit()
    conn.close()
    print(f"Added {qty} of {name} to the pantry.")

def get_inventory():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()
    # This selects everything from the table
    cursor.execute("SELECT item_name FROM inventory")
    # Use list comprehension to get the names
    items = [row[0] for row in cursor.fetchall()]
    conn.close()
    return items

if __name__ == "__main__":
    init_db()