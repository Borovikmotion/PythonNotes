"""

"C:\Program Files\Autodesk\Maya2019\bin\mayapy.exe" C:\Users\borov\Documents\maya\scripts\MayaSceneValidator\main_batch.py -p "C:\Users\borov\Downloads\testMayaScenes" -pr "modeling" -af True

"""

import maya.standalone
import sys
import os
import maya.cmds as cmds
from argparse import ArgumentParser
import sys

# FILEPATH = 'C:/Users/volod/Desktop/testBatch'

def main():

    # create arguments
    # action - means argument comes without value, we just add it >> hello.py --sui
    parser = ArgumentParser(description="Maya Scene Validator")
    parser.add_argument('-pr', '--preset', type=str, required=True, help='Defines which preset you want to use to check maya scenes')
    parser.add_argument('-af', '--auto_fix', type=bool, default=False, help='Should it fix all wrong objects? ')
    parser.add_argument('-p', '--path', type=str, required=True, help='Folder path with maya files ')
    args = parser.parse_args()

    # -----------------------------------------------------

    FILEPATH = args.path
    AUTO_FIX = args.auto_fix
    PRESET = args.preset

    print(FILEPATH, AUTO_FIX, PRESET)

    if not os.path.isdir(FILEPATH):
        print "ERROR"
        return

    if not os.listdir(FILEPATH): 
        print "ERROR"
        return


    mayaFiles = []
    for i in os.listdir(FILEPATH):
        filename, file_extension = os.path.splitext(i)
        if file_extension == '.mb' or file_extension == '.ma':
            full_path  = os.path.join(FILEPATH, i)
            mayaFiles.append(full_path)

    if not mayaFiles:
        print "ERROR"
        return
    
    # -------------------------------------------

    maya.standalone.initialize()

    result = {}

    for i in mayaFiles:
        print("Checking: ", i)

        cmds.file(i, open=True, force=True)
        
        packages = ['MayaSceneValidator'] # project list, that we would like to reload

        for i in sys.modules.keys()[:]:
            for package in packages:
                if i.startswith(package):
                    del(sys.modules[i])

        import MayaSceneValidator.main
        from MayaSceneValidator.main import Validator
        MayaSceneValidator.main.main(auto_fix=AUTO_FIX, mode=Validator.BATCH_MODE)

        if AUTO_FIX:
            print("trying autofix and saving file")
            cmds.file(save=1)
        
        # cmds.file(new=1, force=True)

    maya.standalone.uninitialize()


if __name__ == "__main__":
    main()
