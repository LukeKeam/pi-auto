# https://www.sqlitetutorial.net/sqlite-python/

"""
actual data
1,1,20200825092347.000,-27.701941,153.215176,2.055,,,1,,500.0,500.0,500.0,,2,,1059.9,192.0\r\n\r\nOK\r\n
"""

import time
from db_connect import db_create_connection

database = r"data.db"
db_file = database
conn = db_create_connection(db_file)
cur = conn.cursor()


# check db
def db_select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """


print('gps')
date_time_from_server = "20200827091549.000"
cur.execute("SELECT * FROM gps ORDER BY id DESC LIMIT 500")  # " WHERE datetime > {0} ".format(date_time_from_server))
rows = cur.fetchall()
for row in rows:
    time.sleep(.02)
    print(row)

print('')
print('users')
cur.execute("SELECT * FROM user")
rows = cur.fetchall()
for row in rows:
    time.sleep(.1)
    print(row)


print('')
print('obd')
cur.execute("SELECT * FROM obd ORDER BY id DESC LIMIT 500")
rows = cur.fetchall()
for row in rows:
    time.sleep(.02)
    print(row)

