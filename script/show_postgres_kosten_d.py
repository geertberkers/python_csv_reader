# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:15:19 2025

@author: geert
"""

import pandas as pd
from sqlalchemy import create_engine

# Create the engine
engine = create_engine('postgresql://postgres:password@localhost:5432/afschrijvingen_database')

# Read the table into a DataFrame
sql_statement = '''
SELECT *
FROM (
    SELECT 
        afschrijving, beschrijving, datum, rekening, bedrag, 1 AS sort_order
    FROM public.afschrijvingen

    UNION ALL

    SELECT 
        'AFSCHRIJVINGEN' AS afschrijving,
        'TOTAAL' AS beschrijving,
        NULL AS datum,
        'REKENINGEN' AS rekening,
        SUM(bedrag) AS bedrag,
        0 AS sort_order
    FROM public.afschrijvingen
) AS combined
ORDER BY sort_order, bedrag DESC, datum;
'''
df = pd.read_sql(sql_statement, con=engine)

# Display
print(df)
