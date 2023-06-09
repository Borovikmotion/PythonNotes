import re
import os
import logging
import datetime

ROOT = "C:/p_tests"

def getDateTime():
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    second = '{:02d}'.format(now.second)

    return[now.year, now.month, now.day, now.hour, now.minute, now.second]

def createLogger():
        #check dir
        log_dir = os.path.join(ROOT, "logs")
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)

        # create our own logger, to google - logging handlers
        log_file = os.path.join(log_dir, "{0}_{1}_{2}_{3}_{4}_{5}_maya.log".format(*getDateTime()))
        logger = logging.getLogger("MayaLogs")
        logger.setLevel(logging.DEBUG)

        # cleanup old data
        for hnd in logger.handlers:
            print "Removing {} handler".format(hnd)
            logger.removeHandler(hnd)

        file_handler = logging.FileHandler(log_file, mode='w', encoding = 'utf8')
        file_handler_format = logging.Formatter('[%(module)s.%(funcName)s.%(lineno)d] %(levelname)s:%(message)s')
        file_handler.setFormatter(file_handler_format)
        logger.addHandler(file_handler)
        # logger.debug("hehehe")

        return logger, file_handler

def read_file(full_path_to_file):
    def decorator(function):
        def wrapper(*args, **kwargs):

            logger_.info("Reading {}".format(full_path_to_file))
            #check if file exists
            if not os.path.isfile(full_path_to_file):
                logger_.info("File {} does not exist".format(full_path_to_file))
                raise ValueError('File "{}" does not exist'.format(full_path_to_file))

            #read file
            source_text = []
            with open (full_path_to_file, "r") as f:
                source_text = f.read().splitlines()

            #check if file is empty
            if not source_text:
                logger_.info("File {} is empty".format(full_path_to_file))
                raise ValueError('File "{}" is empty'.format(full_path_to_file))

            #call the main function
            result = function(textData = source_text)

            #write rew file
            source_path, source_file = os.path.split(full_path_to_file)
            new_file = source_file.split(".")[0] + "_filtered_" + ".txt"
            new_path = os.path.join(source_path, new_file)
            with open (new_path, "w") as f:
                f.write("\n".join(result))

            return result
        return wrapper 
    return decorator

def check_numbers(list_of_objects):
    for i in list_of_objects:
        pattern = re.compile("([+-]?([0-9]+|[1-9]+[0-9]*|[1-9]+[0-9]*[.]?[0-9]*[1-9]+|[0-9]?[.]?[0-9]*[1-9]+))$")
        result = pattern.match(i)
        if result:
            if  -1000000 <= float(i) <= 1000000:
                if not (float(i) == 0 and len(i) > 1):
                    logger_.info("+:\t\t{}".format(i))
                    yield i
        else:
            logger_.info("-:\t\t{}".format(i))

@read_file("C:/p_tests/numbers_data.txt")
def main(textData=None):

    #delete spaces in lines
    source_numbers = map(lambda i: i.strip(), textData)
    #do stuff through a generator 
    final_numbers = [i for i in check_numbers(source_numbers)]

    print("\n".join(final_numbers))

    return final_numbers


logger_, f_handler_ = createLogger()

if __name__ == "__main__":
    main()

logger_.removeHandler(f_handler_)
f_handler_.close()



# # launch this in maya or just copy script
# import sys
# packages = ['MayaLogs'] # project list, that we would like to reload
# for i in sys.modules.keys()[:]:
#     for package in packages:
#         if i.startswith(package):
#             del(sys.modules[i])

# import MayaLogs.lesson_09_Hm_5 as mlog
# mlog.main()



