import psycopg

# Connect to an existing database
conn = psycopg.connect("dbname='test' user='dashl' host='localhost'")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (171, "nothing to see here"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
cur.fetchone()
# (2, 171, "nothing to see")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
