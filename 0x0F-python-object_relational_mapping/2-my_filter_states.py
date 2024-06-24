#!/usr/bin/python3
"""
 Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, usrInput = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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
        cursor.execute("SELECT * FROM states WHERE name LIKE {usrInput} ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        sys.exit(1)

    # Disconnect from server
    db.close()
