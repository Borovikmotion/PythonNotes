from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds 
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from optionsUI import OptionsUI

import os
import json


class BasicTool(QtWidgets.QWidget):
    """
    The button that we gonna Click | Drag | Drop
    When we click - our cursor carries MimeData that we need to feed with some custom info
    """

    def __init__(self, parent = None, label = "TEST"):

        super(BasicTool, self).__init__()

        self.setFixedSize(200, 40)

        # Background Color
        self.setAutoFillBackground(True)
        color = 100
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)

        # main layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainLayout)

        # label
        self.label = QtWidgets.QLabel(label)
        self.mainLayout.addWidget(self.label)


    def mousePressEvent(self, event):
        pass
        # print self.label.text()


class ToolA(BasicTool):

    def __init__(self, label = "TEST"):

        super(ToolA, self).__init__(label = label)

    def mousePressEvent(self, event):
        print "ToolA"
        super(ToolA, self).mousePressEvent(event)


class ToolB(BasicTool):

    def __init__(self, label = "TEST"):

        super(ToolB, self).__init__(label = label)

    def mousePressEvent(self, event):
        print "ToolB"
        super(ToolB, self).mousePressEvent(event)


class ToolC(BasicTool):

    def __init__(self, label = "TEST"):

        super(ToolC, self).__init__(label = label)

    def mousePressEvent(self, event):
        print "ToolC"
        super(ToolC, self).mousePressEvent(event)


class ToolD(BasicTool):

    def __init__(self, label = "TEST"):

        super(ToolD, self).__init__(label = label)

    def mousePressEvent(self, event):
        print "ToolD"
        super(ToolD, self).mousePressEvent(event)



GLOBAL_LIST = ["ToolA", "ToolB", "ToolC", "ToolD"]

ROOT  = str(os.path.dirname(__file__))

class ToolSet(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):

    def __init__(self):

        super(ToolSet,self).__init__()

        self.setObjectName("myToolSet")

        self.setupUI()

        self.readJSON()

    def setupUI(self):

        #properties
        self.setMinimumWidth(200)
        self.setMaximumWidth(200)
        self.setMinimumHeight(500)
        self.setWindowTitle("My ToolSet")
        self.setDockableParameters(widht = 200)

        # MainWidget and MainLayout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget) # set main widget
        self.mainWidget.setLayout(self.mainLayout) # set main layout

        # Scroll Layout
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(200)
        self.scrollArea.setMaximumWidth(200)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,0,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.mainLayout.addWidget(self.scrollArea) #add to main layout

        # options button
        self.optionsBtn = QtWidgets.QPushButton("Options")
        self.optionsBtn.clicked.connect(self.openOptionsUI)
        self.mainLayout.addWidget(self.optionsBtn)


    def readJSON(self):


        # clean up
        if self.scroll_layout.count():
            for i in range(self.scroll_layout.count()):
                item = self.scroll_layout.itemAt(i)
                widget = item.widget()
                widget.deleteLater()




        json_file_path = os.path.join(ROOT, "save.json")

        json_data = []
        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)


        for i in json_data:

            exec("btn = {0}(label = '{0}')".format(i))

            self.scroll_layout.addWidget(btn)



    def openOptionsUI(self):
        
        if cmds.window('myOptionsUI', q=1, exists=1):
            cmds.deleteUI('myOptionsUI')
            
        if cmds.windowPref('myOptionsUI', exists = 1):
            cmds.windowPref('myOptionsUI', remove = 1)
                         
        self.myUI = OptionsUI(classList = GLOBAL_LIST)

        self.myUI.MySignal.connect(self.readJSON)
        self.myUI.show()




def main():
    
    if cmds.workspaceControl('myToolSetWorkspaceControl', exists=True):
        cmds.deleteUI('myToolSetWorkspaceControl', control = True)
        cmds.workspaceControlState('myToolSetWorkspaceControl', remove=1)
        
    myUI = ToolSet()
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl('myToolSetWorkspaceControl',
                            label = 'ToolSet',
                            edit = 1,
                            tabToControl = ['AttributeEditor', -1],
                            widthProperty = 'fixed',
                            initialWidth = 400)



    
main()
