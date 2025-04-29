# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:33:14 2025

@author: geert
"""

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env", override=True)
#load_dotenv(dotenv_path="../prod.env", override=True)

# Access them using os.environ
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")

print("Reading env file:")
print("User:", user)
print("Password:", password)
print("Host:", host)
print("port:", port)
print("database:", database)

# 1. Load the CSV
csv_file = '../csv/people.csv'
#csv_file = '../csv/afschrijvingen.csv'
df = pd.read_csv(csv_file)

# 2. Define the PostgreSQL connection string

# Format: 'postgresql://username:password@host:port/database'
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# 3. Create the engine
engine = create_engine(connection_string)

# 4. Write the DataFrame into a PostgreSQL table
df.to_sql('people', con=engine, if_exists='replace', index=False)
#df.to_sql('afschrijvingen', con=engine, if_exists='replace', index=False)

print("CSV data has been loaded into PostgreSQL!")


