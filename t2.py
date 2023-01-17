# Small script to show PostgreSQL and Pyscopg together

import psycopg

try:
    conn = psycopg.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")
