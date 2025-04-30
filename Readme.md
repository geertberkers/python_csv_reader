# Python Project for ETL
- Read JSON
- Read CSV
- Import into MongoDB
- Import into PostgreSQL

# Plan reading CSV
Here's the plan:
1. Pick a database (lets use SQLite first as it's super easy, no server setup needed).
2. Pick a CSV file (you can use any CSV as if you don't have one, I'll suggest a sample).
3. Write a Python script to:
- Read the CSV
- Create a database table
- Insert the data.

# TODO:
- Make sure a way is added to add PRIMARY KEY to tables.ALPN
- Probably need another script for this.
- Than colums can be refernced so that tables can be linked. 

# ENV Files
- For security reasons, production environment variables are not shared in this project.
- An `.env` file is created to read values from.
- Add `prod.env` to add production values.
- This file is added in gitignore so not commited

```
user=user
password=secretproductionpassword
host=localhost/ip/domainname
port=5432
database=mydatabasename
```


# Connect pgAdmin
In pgAdmin, Connect to Your Postgres Server

After logging in: Click "Add New Server".

In the General tab a Give it any name (e.g., MyDatabase).

In the Connection tab:

```
Host: postgres (because the containers share a network in Docker Compose)
Port: 5432
Username: postgres
Password: password
```


# Docker compose Folder Structure
- Create extra databases
- Add automatic connection to pgAdmin
```
postgres-docker/
├── docker-compose.yml
└── init/
    └── create_second_db.sql
└── json/
    └── servers.json
```

Run Docker:

`docker-compose down -v`

`docker-compose up -d`


# Run PSQL from docker:
`docker run -it --rm postgres psql -h <host> -U <user> -d <database>`
Example to check if data is loaded

```
PS C:\Users\geert\python_csv_reader> docker run -it --rm postgres psql -h 91.99.8.239 -U user -d database
Password for user user:
psql (17.4 (Debian 17.4-1.pgdg120+2), server 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off, ALPN: none)
Type "help" for help.

database=> \c database
psql (17.4 (Debian 17.4-1.pgdg120+2), server 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off, ALPN: none)
You are now connected to database "kosten" as user "geert".
database=> \dt
            List of relations
 Schema |      Name      | Type  | Owner
--------+----------------+-------+-------
 public | afschrijvingen | table | geert
(1 row)

database=> SELECT * FROM afschrijvingen;
database=>


```

# Note: Failing Netflix data because , is in the Title:
```
"Squid Game: The Challenge: Seizoen 1: Red Light, Green Light","4/26/25"
"Cheat: Seizoen 1: Scumbags, The Lot Of 'Em","4/26/25"
"Inside: Seizoen 2: Fresh Meat, Fresh Money","4/26/25"
This , in the name are seen as divider,,,

Solved by changing code!
```
