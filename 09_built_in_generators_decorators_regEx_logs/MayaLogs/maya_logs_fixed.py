import logging
import os
import datetime

now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
day = '{:02d}'.format(now.day)
hour = '{:02d}'.format(now.hour)
minute = '{:02d}'.format(now.minute)
second = '{:02d}'.format(now.second)

dir_ = os.path.dirname(__file__)
log_file = os.path.join(dir_, "logs", "{0}_{1}_{2}_{3}_{4}_{5}_maya.log".format(year, month, day, hour, minute, second))

logger = logging.getLogger("MayaLogs")
logger.setLevel(logging.DEBUG)

# clean logger from trash
for hnd in logger.handlers:
    print "Removing {} handler".format(hnd)
    logger.removeHandler(hnd)

file_handler = logging.FileHandler(log_file, mode='w')
file_handler_format = logging.Formatter('[%(module)s.%(funcName)s.%(lineno)d] %(levelname)s:%(message)s')
file_handler.setFormatter(file_handler_format)

logger.addHandler(file_handler)



def main():
    
    logger.debug("hello world")
    logger.info("hello world")
    logger.warning("hello world")
    logger.error("hello world")
    logger.critical("hello world")

    file_handler.close()
    logger.removeHandler(file_handler)

