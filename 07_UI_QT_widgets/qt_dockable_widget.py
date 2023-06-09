import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

class MyCustomWidget(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):
    def __init__(self):
        super(MyCustomWidget, self).__init__()

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("My Custom UI")
        self.setObjectName("MyCustomWidgetUIId")
        self.setMinimumSize(300, 500)
        self.resize(300, 500)

        self.mainWidget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(5,5,1,5)
        self.main_layout.setSpacing(5)
        self.mainWidget.setLayout(self.main_layout)

def main():
    #dockable thing
    if cmds.workspaceControl('MyCustomWidgetUIIdWorkspaceControl', exists=True):
        cmds.deleteUI('MyCustomWidgetUIIdWorkspaceControl', control = True)
        
    if cmds.workspaceControlState('MyCustomWidgetUIIdWorkspaceControl', exists=True):
        cmds.workspaceControlState('MyCustomWidgetUIIdWorkspaceControl', remove=1)
        
    myUI = MyCustomWidget()
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl('MyCustomWidgetUIIdWorkspaceControl',
                            label = 'MyCustomWidget',
                            edit = 1,
                            tabToControl = ['AttributeEditor', -1],
                            widthProperty = 'fixed',
                            initialWidth = 300)

if __name__ == "__main__":
    main()
