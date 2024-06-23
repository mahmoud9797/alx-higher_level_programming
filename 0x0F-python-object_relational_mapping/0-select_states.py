#!/usr/bin/python3

"""  python & database connection & script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    curr = conn.cursor()
    curr.execute("SELECT * FROM states ORDER BY id ASC")
    tabel_rows = curr.fetchall()
    for row in tabel_rows:
        print(row)
    curr.close()
    conn.close()
