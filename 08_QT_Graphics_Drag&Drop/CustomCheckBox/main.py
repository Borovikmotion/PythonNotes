from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from checkBox import MyCheckBox


class MyDialog(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()

        self.setFixedSize(400, 400)
        self.setObjectName("MySuperDialogID")
        self.setWindowTitle("Custom Widget Example")

        # main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        #checkbox
        self.btn = MyCheckBox()
        self.btn.toggled.connect(self.debug)
        self.main_layout.addWidget(self.btn)

    def debug(self, state):
        print(state)


def main():

    if cmds.window("MySuperDialogID", exists=1):
        cmds.deleteUI("MySuperDialogID")
    
    if cmds.windowPref("MySuperDialogID", exists=1):
        cmds.windowPref("MySuperDialogID", remove=1)
    
    # global mydlg

    mydlg = MyDialog()
    mydlg.show()



# if __name__ == "__main__":
#     main()