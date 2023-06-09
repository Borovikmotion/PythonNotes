import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class MyCustomWidget(QtWidgets.QDialog):
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
    # A regular way to do window thing
    if cmds.window("MyCustomWidgetUIId", exists=1):
        cmds.deleteUI("MyCustomWidgetUIId")
    
    if cmds.windowPref("MyCustomWidgetUIId", exists=1):
        cmds.windowPref("MyCustomWidgetUIId", remove=1)

    global myUI
    myUI = MyCustomWidget()
    myUI.show()

if __name__ == "__main__":
    main()
