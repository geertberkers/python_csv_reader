# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 00:46:24 2025

@author: geert
"""

import pandas as pd
from pymongo import MongoClient

# 1. Connect to MongoDB (localhost or remote)
client = MongoClient('mongodb+srv://user:password@cluster0.iv2js6b.mongodb.net')  # Default URI, change if needed

# 2. Select your database
db = client['databases']

# 3. Choose your collection (MongoDB's version of a table)
collection = db['people']
#collection = db['netflix']

# 4. Load the CSV data into a DataFrame
csv_file = 'people.csv'
#csv_file = 'netflix.csv'
df = pd.read_csv(csv_file)

# 5. Convert the DataFrame to a dictionary list (to insert into MongoDB)
data_dict = df.to_dict(orient='records')

# 6. Insert data into MongoDB
collection.insert_many(data_dict)

print("CSV data has been loaded into MongoDB!")

# 7. Optional: Verify by reading back the data
for person in collection.find():
    print(person)

# 8. Close connection (optional, Mongo handles it well)
client.close()
