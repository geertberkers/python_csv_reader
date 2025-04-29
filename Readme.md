# Python Project for ETL
- Read JSON
- Read CSV
- Import into MongoDB
- Import into PostgreSQL

# Plan reading CSV
Here's the plan:
Pick a database (letâ€™s use SQLite first â€” it's super easy, no server setup needed).
Pick a CSV file (you can use any CSV â€” if you don't have one, I'll suggest a sample).
Write a Python script to:
Read the CSV
Create a database table
Insert the data.


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


# Note: Failing Netflix data:
```
"Squid Game: The Challenge: Seizoen 1: Red Light, Green Light","4/26/25"
"Cheat: Seizoen 1: Scumbags, The Lot Of 'Em","4/26/25"
"Inside: Seizoen 2: Fresh Meat, Fresh Money","4/26/25"
This , in the name are seen as divider,,,

Solved by changing code!
```
