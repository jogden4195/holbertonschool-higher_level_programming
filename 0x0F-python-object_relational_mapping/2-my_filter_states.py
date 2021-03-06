#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    """lists all states with a N name from the database hbtn_0e_0_usa"""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute(
        """SELECT id, name FROM states WHERE name
        LIKE BINARY '{}' ORDER BY id""".format(
            sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print('{}'.format(row))
    cur.close()
    conn.close()
