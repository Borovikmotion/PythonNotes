import os 
import json
from MayaSceneValidator.core.config import Configurator
from MayaSceneValidator.core.common import read_json, log


root_ = os.path.dirname(__file__)
project_root = os.path.dirname(root_)

#single tone - make all iuunstances of class connected together
class Resources(object):
    __instance__ = None

    @staticmethod
    def get_instance():
        if not Resources.__instance__:
            Resources()
        return Resources.__instance__

    def __init__(self):
        if Resources.__instance__ is None:
            Resources.__instance__ = self
        else:
            raise Exception("Error Singleton")

        # paths to project files
        self.config_path = os.path.join(project_root, "config.ini") 
        self.preset_root = os.path.join(project_root, "presets")
        self.preset_current = None
        self.preset_current_path = None
        self.preset_paths = []
        self.rules_root = os.path.join(project_root, "rules")
        self.rules_paths = []
        self.config = None

        self.get_rules()
        self.get_presets()
        self.get_config()
        self.get_info()

    def get_config(self):
        #creates configurator class instance
        # returns None
        self.config = Configurator(config_path=self.config_path)
        self.config.init_config()
        self.get_current_preset_name()
        self.get_current_preset_path()
    
    def get_current_preset_name(self):
        self.preset_current = self.config.get_current_preset()
    
    def get_current_preset_path(self):
        self.preset_current_path = self.config.get_current_preset_path()

    def get_rules(self):
        self.rules_paths = []
        # os.walk allows to go through the files and folders inside directory 
        for path, folders, files in os.walk(self.rules_root):
            if path != self.rules_root:
                # print(path, folders, files)
                self.rules_paths.append(path)
        return self.rules_paths

    def get_presets(self):
        self.preset_paths = []
        for path, folders, files in os.walk(self.preset_root):
            for i in files:
                preset = os.path.join(path, i)
                # print(path, folders, files)
                self.preset_paths.append(preset)
        return self.preset_paths

    def get_current_preset_rules(self):
        json_data = read_json(self.preset_current_path)
        return json_data

    def get_preset_rules(self, preset_name=None):
        if not preset_name:
            return []
        for i in self.preset_paths:
            file_full_name = os.path.split(i)[1]
            file_name = os.path.splitext(file_full_name)[0]
            if preset_name == file_name:
                return read_json(i)


    def save_current_preset(self, preset=None):
        assert preset is not None, "preset is None"
        self.config.set_current_preset(preset=preset)

        for preset_path in self.preset_paths:
            if preset+".json" in preset_path:
                self.config.set_current_preset_path(preset_path=preset_path)
                break

        self.get_current_preset_name()
        self.get_current_preset_path()

    def get_info(self):
        if self.rules_paths:
            for i in self.rules_paths:
                log(message=i, category="rule path")
        
        if self.preset_paths:
            for i in self.preset_paths:
                log(message=i, category="preset path")
        
        #print config.ini
        log(message="current preset = {0}".format(self.preset_current), category="config.ini")
        log(message="current preset path = {0}".format(self.preset_current_path), category="config.ini")