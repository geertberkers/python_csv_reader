# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:18:18 2025

@author: geert
"""

import psycopg2

# Connection settings
conn = psycopg2.connect(
    dbname='netflix_database',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)

# Open a cursor to perform database operations
cur = conn.cursor()

# 1. Create the table (only once)
cur.execute("""
    CREATE TABLE IF NOT EXISTS Netflix (
        id SERIAL PRIMARY KEY,
        title TEXT,
        date DATE
    );
""")
conn.commit()

# 2. Load the CSV
# 2. Load the CSV properly with COPY ... CSV HEADER
with open('Netflix.csv', 'r', encoding='utf-8') as f:
    cur.copy_expert("""
        COPY netflix(title, date)
        FROM STDIN
        WITH CSV HEADER
    """, f)

conn.commit()

print("CSV data has been loaded super fast using COPY!")

# 3. Close communication
cur.close()
conn.close()
