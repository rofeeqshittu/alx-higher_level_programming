#!/usr/bin/python3
"""
    List all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

   # Connect to MySQL
   try:
       db = MySQLdb.connect(
               host="localhost", port=3306, user=username,
               passwd=password, db=database
               )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    try:
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        sys.exit(1)

    # Disconnect from server
    db.close()
