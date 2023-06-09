import sys
import getpass
user_name = getpass.getuser()
sys.path.append('C:/Users/{}/Documents/maya/scripts/examples/09_built_in_generators_decorators_regEx_logs'.format(user_name))

packages = ['MayaLogs'] # project list, that we would like to reload
for i in sys.modules.keys()[:]:
    for package in packages:
        if i.startswith(package):
            del(sys.modules[i])

import MayaLogs.maya_logs_fixed
MayaLogs.maya_logs_fixed.main()
