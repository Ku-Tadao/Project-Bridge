# server/database.py

import sqlite3

# Define the name of our database file.
DATABASE_NAME = 'our_project.db'

def init_db():
    """
    Initializes the database and creates the 'notes' table if it doesn't exist.
    This function should be run once to set up the database.
    """
    # Connect to the SQLite database.
    # If the file doesn't exist, it will be created in the 'server' directory.
    conn = sqlite3.connect(DATABASE_NAME)

    # A 'cursor' is used to execute SQL commands.
    cursor = conn.cursor()

    print("Creating 'notes' table...")
    # SQL command to create a table.
    # "IF NOT EXISTS" prevents an error if we run this function again.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- A unique ID for each note
            content TEXT NOT NULL,                -- The text of the note
            author TEXT NOT NULL,                 -- Who wrote it ("me" or "gf")
            is_shared INTEGER NOT NULL DEFAULT 0, -- 0 for private, 1 for shared
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- The time it was created
        );
    ''')

    # Save (commit) the changes.
    conn.commit()

    # Close the connection.
    conn.close()
    print("Table 'notes' created successfully.")
    print(f"Database '{DATABASE_NAME}' is ready.")

# This allows us to run this script directly from the command line
# to initialize the database.
if __name__ == '__main__':
    init_db()