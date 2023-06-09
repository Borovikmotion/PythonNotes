import sys
packages = ['MayaLogs'] # project list, that we would like to reload
for i in sys.modules.keys()[:]:
    for package in packages:
        if i.startswith(package):
            del(sys.modules[i])

import MayaLogs.maya_logs_fixed
MayaLogs.maya_logs_fixed.main()