#!/usr/bin/python3

""" displays all values in the states table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    curr = conn.cursor()
    msg = "SELECT * FROM states WHERE name LIKE BINARY
