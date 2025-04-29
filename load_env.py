# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:33:14 2025

@author: geert
"""
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env", override=True)
#load_dotenv(dotenv_path="prod.env", override=True)

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