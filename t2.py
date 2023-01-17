# Small script to show PostgreSQL and Pyscopg together

import psycopg

try:
    conn = psycopg.connect("dbname='test' user='dashl' host='localhost' password='cr2kbsi'")
except:
    print("I am unable to connect to the database")
