#!/usr/bin/env python

import psycopg2

instructor = raw_input('Enter instructor: ')
session = raw_input('Enter session: ')
time = raw_input('Enter time: ')

try:
    conn = psycopg2.connect("dbname='bcc' user='bcc'")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO bcc_sessions (title, presenter, start_time) VALUES ('{}', '{}', '{}')".format(session, instructor, time))
    conn.commit()

    cursor.execute("""SELECT * from bcc_sessions""")

    rows = cursor.fetchall()

    print "Table contents:"
    for row in rows:
        print row
except:
    print "DB connection error"
