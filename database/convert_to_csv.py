import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')  # replace with your database name

# Execute the SQL script to populate the tables
cursor = conn.cursor()

# with open('schema.sql', 'r') as f:
#     cursor.executescript(f.read())
# conn.commit()


with open('moakup.sql', 'r') as f:
    cursor.executescript(f.read())
conn.commit()

# List of table names
tables = ['Race', 'Character', 'Doctor', 'Planet', 'Time', 'Journey', 'Enemy', 'Companion', 'Users', 'Message', 'Character_In_Journey']

# Write each table to a CSV file
for table in tables:
    if table == 'Character':
        df = pd.read_sql_query(f"SELECT * from {table}", conn, dtype={'age': 'Int64'})
    else:
        df = pd.read_sql_query(f"SELECT * from {table}", conn)
    df.to_csv(f"csvs/{table}.csv", index=False)

# Close the connection
conn.close()