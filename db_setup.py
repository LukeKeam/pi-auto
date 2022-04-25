# https://www.sqlitetutorial.net/sqlite-python/
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables():
    database = r"data.db"
    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user  (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        token text,
                                        ip_address text
                                    ); """
    sql_create_gps_table = """CREATE TABLE IF NOT EXISTS gps (
                                    id integer PRIMARY KEY,
                                    datetime text NOT NULL,
                                    longitude integer NOT NULL,
                                    latitude integer NOT NULL,
                                    speed integer,
                                    vehicle_move_stop integer,
                                    vehicle_move_start integer,
                                    alert integer
                                ); """
    sql_create_obd_table = """CREATE TABLE IF NOT EXISTS obd (
                                    id integer PRIMARY KEY,
                                    utc text,
                                    speed text,
                                    rpm text,
                                    fuel_level text,
                                    fuel_rate text,
                                    absolute_load text,
                                    engine_load text,
                                    run_time text,
                                    intake_temp text,
                                    oil_temp text, 
                                    coolant_temp text,
                                    ambiant_air_temp text,
                                    barometric_pressure text
                                ); """
    """
    'SPEED', 'RPM', 'ABSOLUTE_LOAD', 'ENGINE_LOAD', 'RUN_TIME', 'FUEL_LEVEL', 'INTAKE_TEMP', 'AMBIANT_AIR_TEMP',
        'BAROMETRIC_PRESSURE', 'FUEL_RATE', 'OIL_TEMP', 'COOLANT_TEMP'
    """
    """
    user integer NOT NULL,,
    FOREIGN KEY (user) REFERENCES user (id)
    """
    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create table
        create_table(conn, sql_create_user_table)
        # create gps table
        create_table(conn, sql_create_gps_table)
        # create obd table
        create_table(conn, sql_create_obd_table)
    else:
        print("Error! cannot create the database connection.")


###################################################################
# insert data into user
###################################################################
def create_username(conn, data):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO user(username,token,ip_address)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid


###################################################################
# insert data into gps
###################################################################
def create_gps(conn, gps_data):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO gps(datetime,longitude,latitude,speed,vehicle_move_stop,vehicle_move_start,alert)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, gps_data)
    conn.commit()
    return cur.lastrowid


###################################################################
# insert data into obd
###################################################################
def create_obd(conn, obd_data):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO obd(utc, speed, rpm, fuel_level, fuel_rate, absolute_load, engine_load, run_time, 
    intake_temp, oil_temp, coolant_temp, ambiant_air_temp, barometric_pressure)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, obd_data)
    conn.commit()
    return cur.lastrowid



###################################################################
# insert data into all
###################################################################
def add_data():
    database = r"data.db"
    # create a database connection
    conn = create_connection(database)
    i = 1
    while i != 2:
        with conn:
            # insert user data
            user_data = ('username', 'token', 'ip_address')
            create_username(conn, user_data)
            # insert database
            gps_data = ('20200825092347.000', '-27.701941', '153.215176', '25', '1', '1', '1')
            create_gps(conn, gps_data)
            obd_data = ('20200825092347.000', '5', '500', '50', '6', '51', '52', '3500000', '53', '54', '55', '30', '20')
            create_obd(conn, obd_data)
            #
            print('i', i)
            if i >= 2:
                break
            i = i + 1

if __name__ == '__main__':
    create_tables()
    add_data()

