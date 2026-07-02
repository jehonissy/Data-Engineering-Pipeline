import sqlite3
import pandas as pd


def load_data():
    # Read cleaned CSV
    df = pd.read_csv("data/cleaned_data.csv")

    # Connect to SQLite database
    conn = sqlite3.connect("database/covid_data.db")

    # Store data in table
    df.to_sql("covid_stats", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Data loaded into SQLite database successfully!")


if __name__ == "__main__":
    load_data()