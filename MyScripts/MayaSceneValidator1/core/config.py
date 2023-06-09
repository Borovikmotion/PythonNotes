#this module doesnt exist in python 3.8
from ConfigParser import ConfigParser
import os 

root_ = os.path.dirname(__file__)

class Configurator(object):
    """
    Class works with config.ini
    """
    def __init__(self):
        print("config importeddfgdfgdf")