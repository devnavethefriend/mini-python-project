import sqlite3
from setup import hth_result  # Import the result object from setup.py

# Connect to the SQLite database
conn = sqlite3.connect('astcry_data.db')
cursor = conn.cursor()

# Create the match_results table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hth_results (
        match_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_number INTEGER,
        total_goals_scored INTEGER
    );
''')

# Commit the changes and close the connection
conn.commit()

# Iterate through the data and insert into the SQL table
for match_number, total_goals in enumerate(hth_result, start=1):
    cursor.execute('''
        INSERT INTO hth_results (match_number, total_goals_scored)
        VALUES (?, ?)
    ''', (int(match_number), int(total_goals)))

# Commit the changes and close the connection
conn.commit()
conn.close()