import sys
import getpass
user_name = getpass.getuser()
sys.path.append('C:/Users/{}/Documents/maya/scripts/examples/08_QT_Graphics_Drag&Drop'.format(user_name))

packages = ['ToolSet'] # project list, that we would like to reload
for i in sys.modules.keys()[:]:
    for package in packages:
        if i.startswith(package):
            del(sys.modules[i])

import ToolSet.mainUI
ToolSet.mainUI.main()
