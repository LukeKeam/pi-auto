import time, datetime, subprocess
# curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -
# curl -s http://whatismyip.akamai.com/


def ping_me():
    i = 0
    while i <= 5:
        print('')
        print('')
        print('int', i)
        print(datetime.datetime.now())
        subprocess.run(['ping', '-I', 'ppp0', '-c', '2', 'google.com'])
        print('')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        i = i + 1
        time.sleep(5)
