import logging
import os


dir_ = os.path.dirname(__file__)
log_file = os.path.join(dir_, "logs", "maya.log")

logging.basicConfig(filename=log_file,
                    filemode='w',
                    level = logging.ERROR,
                    format='[%(module)s.%(funcName)s.%(lineno)d] %(levelname)s:%(message)s'
                    )


def foo_A():
    logging.error("Hello")

def main():
    logging.debug("HEHEHE")
    logging.error("HOHOHO")
    logging.warning("CCCCCC")

    foo_A()


    


if __name__ == "__main__":
    main()