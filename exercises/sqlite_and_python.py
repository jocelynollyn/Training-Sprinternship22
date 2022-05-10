import sqlite3
from sqlite3 import Error
DATABASE_NAME = 'BitcoinDB-demo.db'
TABLE_NAME = 'Bitcoin'

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, DATABASE_NAME)

# TODO: Connect to database
try: # always use a try-catch statement to prevent your programs from crashing in case of a failure
    db = sqlite3.connect(db_path)

except Error as e:
    print(e)

# TODO: get cursor
cursor = db.cursor()

# TODO: define SQL query
sql = "SELECT * FROM '{}';".format(TABLE_NAME)

# TODO: execute sql query
cursor.execute(sql)

# TODO: fetch all results obtained
results = cursor.fetchall()

# TODO: close
cursor.close()

# TODO: print the results
print(results)

