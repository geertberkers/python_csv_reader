# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 19:28:28 2025

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


# List of filenames (lines) from input
lines = [
    "ZCONTRAINDICATION.csv",
    "ZGNAMERELATIONSHIP.csv",
    "ZINTAKEMOMENT.csv",
    "ZWCIATABLE25TTIMEUNIT.csv",
    "ZDISPENSEEVENT.csv",
    "ZGPRESCRIPTIONPRODUCT.csv",
    "ZMEDICATION.csv",
    "Z_19ADMINISTRATIONREQUESTS.csv",
    "ZGADDRESS.csv",
    "ZGPRODUCT.csv",
    "ZMEDICATIONADMINISTRATIONREQUEST.csv",
    "Z_25CATEGORIES.csv",
    "ZGCONTRAINDICATED.csv",
    "ZGSUPPLIERPRODUCT.csv",
    "ZMEDICATIONCHANGE.csv",
    "Z_METADATA.csv",
    "ZGGENERICPRODUCT.csv",
    "ZGTEXTBLOCK.csv",
    "ZPHARMACY.csv",
    "Z_MODELCACHE.csv",
    "ZGINFORMATORIUMGROUP.csv",
    "ZGTEXTBLOCKHTML.csv",
    "ZWCIATABLE25AUNIT.csv",
    "Z_PRIMARYKEY.csv",
    "ZGLOGISTICALINFO.csv",
    "ZGTHESAURUSENTRY.csv",
    "ZWCIATABLE25BTEXT.csv",
    "ZGMONITORINGINFO.csv",
    "ZGTRADEPRODUCT.csv",
    "ZWCIATABLE25BTEXTCATEGORY.csv",
    "ZGNAME.csv",

]

# Define the function
def printname(filename):
    #print('Handling file:', filename)
    save_csv_db(filename)    
    #print('Finished handling file:', filename)
    print('')
          
         
            
         
def save_csv_db(csv_file):
    # Remove .csv extension for use as table name
    db_name = os.path.splitext(os.path.basename(csv_file))[0]
    #print(db_name)
    
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading '{csv_file}':", e)
        return

    df = pd.read_csv(csv_file)
    print(df) # Show DataFrame in Terminal output
    
    
    # 2. Define the PostgreSQL connection string
    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

    # 3. Create the engine
    engine = create_engine(connection_string)

    # 4. Write the DataFrame into a PostgreSQL table
    df.to_sql(db_name, con=engine, if_exists='replace', index=False)

    print(f"CSV data - '{db_name}' -  has been loaded into PostgreSQL!")
    
    
    
    
# Apply function to each item in the list
for line in lines:
    printname('../csv/gstandaard/' + line)