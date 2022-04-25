import os
import datetime


def log_write_to_text_file(log_message):
    datetime_log = datetime.datetime.now()
    datetime_log_date = datetime_log.strftime("%Y-%m-%d")
    path_test = os.path.exists('./Log')
    if path_test == False:
        os.mkdir('./Log')
    log_write = open("./Log/Log {0}.txt".format(datetime_log_date), "a")
    datetime_log_message = datetime_log.strftime("%Y-%m-%d %H:%M:%S")
    log_write.write(datetime_log_message)
    log_write.write(': ')
    log_write.write(log_message)
    log_write.write("\n")
    # doesnt write until closed end
    log_write.close()

