# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 16:18:18 2025

@author: geert
"""

from flask import Flask, request, render_template, jsonify
import psycopg2
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
# Format: 'postgresql://username:password@host:port/database'
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'


app = Flask(__name__)

#DB_PARAMS = {
#    'dbname': 'development_database',
#    'user': 'postgres',
#    'password': 'password',
#    'host': 'localhost',
#    'port': 5432
#}


@app.route('/aggrid')
def indexGrid():
    return render_template('index_aggrid.html')


@app.route('/data')
def get_data():
    query = "SELECT * FROM public.development"
    try:
        #conn = psycopg2.connect(**DB_PARAMS)
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        cur.execute(query)
        headers = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Convert to list of dicts
        result = [dict(zip(headers, row)) for row in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    headers = []
    query = "SELECT * FROM public.development"
    error = None
    if request.method == 'POST':
        query = request.form['query']
        try:
            #conn = psycopg2.connect(**DB_PARAMS)
            conn = psycopg2.connect(connection_string)
            print("✅ Connected to PostgreSQL successfully")
            cur = conn.cursor()
            cur.execute(query)
            if query.strip().lower().startswith('select'):
                results = cur.fetchall()
                headers = [desc[0] for desc in cur.description]
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            error = str(e)
            print("❌ PostgreSQL connection failed:", e)


    return render_template('index.html', query=query, results=results, headers=headers, error=error)

if __name__ == '__main__':
    app.run(debug=True)