# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:33:14 2025

@author: geert
"""

import pandas as pd
from sqlalchemy import create_engine

# 1. Load the CSV into a DataFrame
csv_file = 'people.csv'
df = pd.read_csv(csv_file)

# 2. Create a SQLite database (or connect if exists)
engine = create_engine('sqlite:///people.db')

# 3. Write the DataFrame into a database table
df.to_sql('people', con=engine, if_exists='replace', index=False)

print("CSV data has been loaded into the database!")
