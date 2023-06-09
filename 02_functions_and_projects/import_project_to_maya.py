import sys
packages = ['MayaSceneValidator'] # project list, that we would like to reload

for i in sys.modules.keys()[:]:
    for package in packages:
        if i.startswith(package):
            del(sys.modules[i])

import MayaSceneValidator.main
MayaSceneValidator.main.main() 
