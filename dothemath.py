import sqlite3
import pandas as pd
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('astcry_data.db')  # Replace with your database file
cursor = conn.cursor()

# Retrieve the data into a DataFrame
query = "SELECT * FROM hth_results;"
df = pd.read_sql_query(query, conn)

# Iterate through the DataFrame and insert data into the SQL table
for index, row in df.iterrows():
    try:
        match_number = row['match_number']
        total_goals_scored = row['total_goals_scored']
        # Label Generation: Determine if a match has 3 goals or more
        df['label'] = np.where(int(total_goals_scored) >= int(3))
    except ValueError:
        pass
    
    # Insert data into the 'match_results' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS df_results (
            label_id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_number INTEGER,
            total_goals_scored INTEGER 
        );
    ''')

    cursor.execute('''
        INSERT INTO df_results (match_number, total_goals_scored)
        VALUES (?, ?)
        ''', (match_number, total_goals_scored)
    )

# Print the updated DataFrame
print(df)

# Close the database connection
conn.commit()
conn.close()
