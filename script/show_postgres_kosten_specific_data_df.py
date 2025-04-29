# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:15:19 2025

@author: geert
"""

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env", override=True)
load_dotenv(dotenv_path="../prod.env", override=True)

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


# 3. Create the engine
# Format: 'postgresql://username:password@host:port/database'
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string)


# Read the table into a DataFrame
sql_statement = '''
SELECT *
FROM (
    SELECT 
        afschrijving, beschrijving, bedrag, 1 AS sort_order
    FROM public.afschrijvingen
    WHERE datum = '1e'

    UNION ALL

    SELECT 
        'AFSCHRIJVINGEN' AS afschrijving,
        'TOTAAL' AS beschrijving,
        SUM(bedrag) AS bedrag,
        0 AS sort_order
    FROM public.afschrijvingen
    WHERE datum = '1e'
) AS combined
ORDER BY sort_order, bedrag DESC;
'''
df = pd.read_sql(sql_statement, con=engine)

# Display
print(df)
