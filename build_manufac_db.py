import sqlite3

def create_database():
    # Connect to the database (it creates a new file if it doesn't exist)
    conn = sqlite3.connect("manufacturing.db")
    cursor = conn.cursor()

    # Define table schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS manufacturing_data (
            Process_ID TEXT PRIMARY KEY,
            Step TEXT,
            Duration REAL,
            Defect_Rate REAL,
            Production_Yield REAL,
            Recommendation TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database and table created successfully!")

if __name__ == "__main__":
    create_database()
