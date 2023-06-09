# a little bit wrong way to import packages 
# from core import config

from MayaSceneValidator.core.config import Configurator

print("importted config")

class Validator(object):
    def __init__(self):
        print("hahaha")
        self.config = Configurator()
        pass



def main():
    v = Validator()


# how to launch this in pycharm without maya 
# if __name__ = "__main__"
#     main()
