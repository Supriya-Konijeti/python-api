from flask import Flask, render_template, request, jsonify
import db
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Priyak@33",
    port="5432"
)
print(conn)
table_customer_query = '''
        CREATE TABLE Todo(
            ID INT PRIMARY KEY NOT NULL,
            NAME Varchar NOT NULL,
            COMPANY varchar
        )
'''
cur = conn.cursor()

cur.execute(table_customer_query)
conn.commit()
print("Table created")
