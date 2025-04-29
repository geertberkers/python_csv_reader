# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 01:17:02 2025

@author: geert
"""

import json
import pandas as pd
from sqlalchemy import create_engine

# 1. Load the raw JSON data
with open('../json/raw_patient.json') as f:
    data = json.load(f)
# Normally you load from a file or API, here we simulate it:
#raw_json = '''
#[
#    {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
#    {"id": 2, "name": "Bob", "city": "Los Angeles"},
#    {"id": 3, "name": "Charlie", "age": "35", "city": "Chicago"},
#    {"id": 4, "name": null, "age": 28, "city": "Miami"}
#]
#'''
#data = json.loads(raw_json)

# 2. Normalize/clean the JSON data
df = pd.json_normalize(data)

# Fill missing 'age' with 0, convert to integer
df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)

# Fill missing 'name' with 'Unknown'
df['name'] = df['name'].fillna('Unknown')

# Optional: clean strings (like strip spaces, lowercase)
df['city'] = df['city'].str.strip()

print("Cleaned Data:")
print(df)



# 2. Define the PostgreSQL connection string
user = 'postgres'
password = 'password'
host = 'localhost'
port = '5432'
database = 'people_database'


# Format: 'postgresql://username:password@host:port/database'
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# 3. Create the engine
engine = create_engine(connection_string)

# 4. Create table and insert
df.to_sql('people', con=engine, if_exists='replace', index=False)

print("JSON data has been cleaned and loaded into PostgreSQL!")
