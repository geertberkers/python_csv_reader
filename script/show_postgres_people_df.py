# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:15:19 2025

@author: geert
"""

import pandas as pd
from sqlalchemy import create_engine

# Create the engine
engine = create_engine('postgresql://postgres:password@localhost:5432/people_database')

# Read the table into a DataFrame
sql_statement = 'SELECT * FROM people;'
df = pd.read_sql(sql_statement, con=engine)

# Display
print(df)
