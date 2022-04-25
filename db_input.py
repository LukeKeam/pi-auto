from db_connect import db_create_connection


def db_send_to_local_db_obd(utc, speed, rpm, fuel_level, fuel_rate, absolute_load, engine_load, run_time, intake_temp,
    oil_temp, coolant_temp, ambiant_air_temp, barometric_pressure):
    """
    store only 6min intervals while moving
    if vehicle move stop then store that
        and wait till move start to start again
    """
    def create_task(conn, task):
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
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid
    database = r"data.db"
    # create a database connection
    conn = db_create_connection(database)
    with conn:
        """
        id integer PRIMARY KEY,
        datetime text NOT NULL,
        longitude integer NOT NULL,
        latitude integer NOT NULL,
        speed integer,
        vehicle_move_stop integer,
        vehicle_move_start integer,
        alert integer
        """
        # task_1 = ('20200827091548.000', '-27.701941', '153.215176', '25', '1', '1', '1',)
        # create_task(conn, task_1)
        # create tasks
        task_2 = (utc, speed, rpm, fuel_level, fuel_rate, absolute_load, engine_load, run_time, intake_temp,
    oil_temp, coolant_temp, ambiant_air_temp, barometric_pressure)
        create_task(conn, task_2)



def db_send_to_local_db(utc, latitude, longitude, speed, vehicle_move_stop, vehicle_move_start, alert  ):
    """
    store only 6min intervals while moving
    if vehicle move stop then store that
        and wait till move start to start again
    """
    def create_task(conn, task):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """
        sql = ''' INSERT INTO gps(datetime,longitude,latitude,speed,vehicle_move_stop,vehicle_move_start,alert)
                  VALUES(?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid
    database = r"data.db"
    # create a database connection
    conn = db_create_connection(database)
    with conn:
        """
        id integer PRIMARY KEY,
        datetime text NOT NULL,
        longitude integer NOT NULL,
        latitude integer NOT NULL,
        speed integer,
        vehicle_move_stop integer,
        vehicle_move_start integer,
        alert integer
        """
        # task_1 = ('20200827091548.000', '-27.701941', '153.215176', '25', '1', '1', '1',)
        # create_task(conn, task_1)
        # create tasks
        task_2 = (utc, latitude, longitude, speed, vehicle_move_stop, vehicle_move_start, alert,)
        create_task(conn, task_2)
