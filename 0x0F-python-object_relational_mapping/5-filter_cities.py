#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    """lists all cities of a given state from the database hbtn_0e_4_usa"""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = conn.cursor()
    command = """SELECT cities.name FROM cities
                 JOIN states ON cities.state_id = states.id
                 WHERE states.name = %s"""
    cur.execute(command, (sys.argv[4],))
    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append(row[0])
    print(', '.join(str(x) for x in cities))
    cur.close()
    conn.close()
