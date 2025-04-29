# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:33:14 2025

@author: geert
"""

import pandas as pd
from sqlalchemy import create_engine

# 1. Load the CSV
csv_file = 'people.csv'
csv_file = 'afschrijvingen.csv'
df = pd.read_csv(csv_file)

# 2. Define the PostgreSQL connection string
user = 'postgres'
password = 'password'
host = 'localhost'
port = '5432'
database = 'afschrijvingen_database'

#user = 'postgres'
#password = 'password'
#host = 'localhost'
#port = '5432'
#database = 'postgres'



# Format: 'postgresql://username:password@host:port/database'
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# 3. Create the engine
engine = create_engine(connection_string)

# 4. Write the DataFrame into a PostgreSQL table
#df.to_sql('people', con=engine, if_exists='replace', index=False)
df.to_sql('afschrijvingen', con=engine, if_exists='replace', index=False)

print("CSV data has been loaded into PostgreSQL!")


