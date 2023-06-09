from importlib import reload
import sys
packages = ['webinar']
for module in sys.modules.keys():
  for pkg_name in packages:
      if module.startswith(pkg_name):
          print("Reloading {}".format(module))
          reload(sys.modules[module])

import webinar.poseLibImport
webinar.poseLibImport.main()