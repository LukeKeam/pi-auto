import datetime
import time
import requests
from dateutil import parser
from db_connect import db_create_connection


# https://requests.readthedocs.io/en/master/
# https://2.python-requests.org/en/latest/user/quickstart/

def post_to_server(auth_user_id, token, conn):
    print('starting post_to_server')
    try:
        # setup var start
        global data_to_send
        data_to_send = ''''['''
        # get latest record from remote server and save utc
        url = 'https://api.fleet-track.org/gps/'
        headers = {'content-type': 'application/json', 'Authorization': 'Token {0}'.format(token)}
        print('start')
        r = ''
        requests.session().close()
        r = requests.get(url, headers=headers).json()[0]
        requests.session().close()
        print('get r', r)
        utc_server = r['utc']
        u = parser.parse(utc_server)
        u = u + datetime.timedelta(0,1)
        utc_server_formatted = u.strftime("%Y%m%d%H%M%S")
        # print(utc_server_formatted)
        # get utc to latest record from local db
        now = datetime.datetime.now().utcnow().strftime("%Y%m%d%H%M%S")
        print('now', now)
        # database connection
        cur = conn.cursor()
        def send(row, auth_user_id):
            # print('Send record start')
            user_id = "Polo"
            auth_user = "1"
            utc = row[1]
            u = int(float(utc))
            latitude = str(row[2])
            longitude = str(row[3])
            speed = int(row[4])
            vehicle_move_stop = str(row[5])
            vehicle_move_start = str(row[6])
            alert = str(row[7])
            # post to server
            url = 'https://api.fleet-track.org/gps/'
            payload = '{{"user_id":"{0}", "auth_user":"{1}", "utc":"{2}" , "latitude":"{3}", "longitude":"{4}", ' \
                   '"speed":"{5}", "vehicle_move_stop":"{6}", "vehicle_move_start":"{7}", ' \
                   '"alert":"{8}"}}, '.format(user_id, auth_user, u, latitude, longitude, speed, vehicle_move_stop,
                                             vehicle_move_start, alert)
            # print('payload', payload)
            # put into var
            # print('data', data)
            global data_to_send
            data_to_send = data_to_send + payload
            #print('data_to_send', data_to_send)
            #print(' ')
            #print(' ')
        # send data
        print('Start session with server')
        ssn = requests.Session()
        i = 0
        print("get records from db assuming newest id is newest") # ID%3600
        rows = ''
        print('before query')
        # old query
        # cur.execute("SELECT * FROM gps WHERE datetime BETWEEN {0} AND {1} ORDER BY id ASC ".format(utc_server_formatted, now))
        # Grabs all the alerts
        # cur.execute("SELECT * FROM gps WHERE Alert = 1 ORDER BY id ASC".format(utc_server_formatted, now))
        # grab all records between dates and every 6mins AND alert = 1
        cur.execute("SELECT * FROM gps WHERE (datetime BETWEEN {0} AND {1}) AND (ROWID % 360 = 0) OR (datetime "
                    "BETWEEN {0} AND {1}) AND (Alert = 1) ORDER "
                    "BY id "
                    "ASC".format(utc_server_formatted, now))  # 3600 = 6 seconds
        rows = cur.fetchall()[:3500]  # max size 3501?
        print(rows[:1])
        # print(rows)
        if not rows:
            print('No data to send in rows')
        if rows:
            # just run through once. server caches response for newest record
            print("Starting row and changing structure for json")
            for row in rows:
                # print('row in rows', data_to_send)
                send(row, auth_user_id)
            # once finished then send
            print('Start sending data')
            # remove comma from end
            data_to_send = data_to_send[:-2]
            # remove parts of string
            data_to_send = data_to_send[1:]
            data_to_send = data_to_send + "]"
            # print('data_to_send', data_to_send)
            headers = {'content-type': 'application/json', 'Authorization': 'Token {0}'.format(token)}
            r = ssn.post(url, data=data_to_send, headers=headers)
            # print(r.json())
            # print("data", data_to_send)
            print("Status code", r.status_code)  # 200 is ok, 524 timeout, 400 bad request, 413 payload too large
            print('Posted and completed')
            print('')
            ssn.close()
    except Exception as e:
        print('post_to_server except', e)

