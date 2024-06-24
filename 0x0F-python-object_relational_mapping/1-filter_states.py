#!/usr/bin/python3

""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    curr = conn.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    table_rows = curr.fetchall()
    for rows in table_rows:
        print(rows)
    curr.close()
    conn.close()

