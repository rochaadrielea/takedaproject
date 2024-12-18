import pandas as pd
import sqlite3

# Load the data
def process_and_store_data():
    # Load CSV
    df = pd.read_csv("manufacturing_data.csv")

    # Add recommendations based on conditions
    def recommendation(row):
        if row["Defect_Rate"] > 0.1:
            return "Reduce Defects"
        elif row["Production_Yield"] < 90:
            return "Improve Yield"
        else:
            return "Process Optimized"

    df["Recommendation"] = df.apply(recommendation, axis=1)

    # Insert into SQLite database
    conn = sqlite3.connect("manufacturing.db")
    df.to_sql("manufacturing_data", conn, if_exists="replace", index=False)
    conn.close()
    print("Data processed and stored successfully!")

if __name__ == "__main__":
    process_and_store_data()
