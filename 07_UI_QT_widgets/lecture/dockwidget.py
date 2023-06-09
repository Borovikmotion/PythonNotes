from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds 
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin




class SceneChecker(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):

    def __init__(self):

        super(SceneChecker,self).__init__()

        self.setObjectName("mySceneChecker")

        self.setupUI()

    def setupUI(self):

        #properties
        self.setMinimumWidth(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(500)
        self.setWindowTitle("My Scene Check")
        self.setDockableParameters(widht = 400)


        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

        self.mainWidget.setLayout(self.mainLayout)

        self.setLayout( self.mainLayout)

        # custom UI

        for i in range(6):

            btn = QtWidgets.QPushButton("TEST {}".format(i))
            self.mainLayout.addWidget(btn)










def main():
    
    if cmds.workspaceControl('mySceneCheckerWorkspaceControl', exists=True):
        cmds.deleteUI('mySceneCheckerWorkspaceControl', control = True)
        
    if cmds.workspaceControlState('mySceneCheckerWorkspaceControl', exists=True):
        cmds.workspaceControlState('mySceneCheckerWorkspaceControl', remove=1)
        
    myUI = SceneChecker()
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl('mySceneCheckerWorkspaceControl',
                            label = 'SceneChecker',
                            edit = 1,
                            tabToControl = ['AttributeEditor', -1],
                            widthProperty = 'fixed',
                            initialWidth = 400)



    
    
main()
