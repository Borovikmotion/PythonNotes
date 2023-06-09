# Python 3 (начиная с Maya 2022 и далее)
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



# old Python 2.7
import sys
packages = ['webinar']
for i in sys.modules.keys()[:]:
    for package in packages:
        if i.startswith(package):
            del(sys.modules[i])

import webinar.poseLibImport
webinar.poseLibImport.main()