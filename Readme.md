Here's the plan:
Pick a database (let’s use SQLite first — it's super easy, no server setup needed).

Pick a CSV file (you can use any CSV — if you don't have one, I'll suggest a sample).

Write a Python script to:

Read the CSV

Create a database table

Insert the data.



3. In pgAdmin, Connect to Your Postgres Server
After logging in:

Click "Add New Server".

In the General tab → Give it any name (e.g., MyDatabase).

In the Connection tab:

Host: postgres (because the containers share a network in Docker Compose)

Port: 5432

Username: postgres

Password: password