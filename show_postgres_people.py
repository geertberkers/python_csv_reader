# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:33:14 2025

@author: geert
"""

import psycopg2

# 1. Docker compose up

conn = psycopg2.connect(
    dbname='people_database',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)

# 1. Connect to the database
#conn = psycopg2.connect(
#    dbname='postgres',
#    user='postgres',
#    password='password',
#    host='localhost',
#    port='5432'
#)

cur = conn.cursor()

# 2. Query the table
cur.execute('SELECT * FROM people;')

# 3. Fetch all rows
rows = cur.fetchall()

# 4. Print the rows
for row in rows:
    print(row)

# 5. Clean up
cur.close()
conn.close()
