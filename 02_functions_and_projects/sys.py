
# a list of maya paths
import sys

pathList = sys.path
for path in pathList:
    print(path)


# custom path
import sys
sys.path.append('/Users/adrian/Documents/MayaScripting/examples')