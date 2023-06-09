# a little bit wrong way to import packages 
# from core import config

import os
# from MayaSceneValidator.core.config import Configurator #tests with config
# from MayaSceneValidator.core.resources import Resources
from MayaSceneValidator.gui.main_gui import ValidatorGUI, create_gui
from MayaSceneValidator.core.batch_mode import BatchValidator

root_ = os.path.dirname(__file__)

class Validator(object):
    #variables for the whole class
    GUI_MODE = 0
    BATCH_MODE = 1

    def __init__(self, mode, preset, auto_fix=False):
        # tests with config file 
        # self.config = Configurator(config_path=os.path.join(root_, "config.ini"))
        # # self.config.set_variable("test", "age", "28")
        # print(self.config.get_current_preset())
        # self.config.set_current_preset("trololo")
        # self.resources = Resources()

        if mode == Validator.GUI_MODE:
            create_gui()

        elif mode == Validator.BATCH_MODE:
            batch = BatchValidator()
            batch.start(preset=preset, auto_fix=auto_fix)






def main(preset="modeling", auto_fix=False, mode=Validator.GUI_MODE):
    v = Validator(mode=mode, preset=preset, auto_fix=auto_fix)




# how to launch this in pycharm without maya 
# if __name__ = "__main__"
#     main()
