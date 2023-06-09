def __init__(self, objectPath = None):

    # Context menu

    self.popMenu = QtWidgets.QMenu(self)

    self.popMenuAdd = QtWidgets.QAction('Add object', self)
    self.popMenu.addAction(self.popMenuAdd)
    self.popMenuAdd.triggered.connect(self.testA)

    self.popMenuDel = QtWidgets.QAction('Delete object', self)
    self.popMenu.addAction(self.popMenuDel)
    self.popMenuDel.triggered.connect(self.testB)    

    # attributes
    self.setMouseTracking(True)  
    self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.customContextMenuRequested.connect(self.onContextMenu)


def onContextMenu(self, point):

    self.popMenu.exec_(self.mapToGlobal(point))


def testA(self):
    print "TEST A"

def testB(self):
    print "TEST B"