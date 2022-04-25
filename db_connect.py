import sqlite3
from sqlite3 import Error


def db_create_connection(db_file):
    """ create or make db then connect to a
    a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
