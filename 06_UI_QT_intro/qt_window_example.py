# SIMPLE WINDOW  WITH BUTTONS
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
# from PySide2.QtWidgets import QHBoxLayout

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Create Poly Objects")
        self.setMinimumSize(500, 100)
        self.setMaximumSize(700, 300)
        self.resize(500, 100)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # layouts
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)
        # self.radio_buttons_layout = QHBoxLayout()
        self.radio_buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.radio_buttons_layout)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.buttons_layout)

        # radiobuttons
        self.rbutton_Sphere = QtWidgets.QRadioButton("Sphere")
        self.rbutton_Sphere.setChecked(True)
        self.rbutton_Cube = QtWidgets.QRadioButton("Cube")
        self.rbutton_Cone = QtWidgets.QRadioButton("Cone")
        self.radio_buttons_layout.addWidget(self.rbutton_Sphere)
        self.radio_buttons_layout.addWidget(self.rbutton_Cube)
        self.radio_buttons_layout.addWidget(self.rbutton_Cone)

        # buttons
        self.button_OK = QtWidgets.QPushButton("OK")
        self.button_OK.clicked.connect(self.on_button_ok_clicked)

        self.button_Apply = QtWidgets.QPushButton("Apply")
        self.button_Apply.clicked.connect(self.on_button_apply_clicked)

        self.button_Cancel = QtWidgets.QPushButton("Cancel")
        self.button_Cancel.clicked.connect(self.close)

        self.buttons_layout.addWidget(self.button_OK)
        self.buttons_layout.addWidget(self.button_Apply)
        self.buttons_layout.addWidget(self.button_Cancel)

    def on_button_ok_clicked(self):
        self.on_button_apply_clicked()
        self.close()

    def on_button_apply_clicked(self):
        if self.rbutton_Sphere.isChecked():
            cmds.polySphere()
        elif self.rbutton_Cube.isChecked():
            cmds.polyCube()
        elif self.rbutton_Cone.isChecked():
            cmds.polyCone()


if cmds.window("MyTestUI", q=1, exists=True):
    cmds.deleteUI("MyTestUI")

if cmds.windowPref("MyTestUI", exists=True):
    cmds.windowPref("MyTestUI", remove=1)

a = MyWindow()
a.show()





# SIMPLE WINDOW, but MORE
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
# from PySide2.QtWidgets import QHBoxLayout

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_UI()
        self.create_radio_buttons()
        self.create_buttons()

    def setup_UI(self):
        self.setWindowTitle("Create Poly Objects")
        self.setMinimumSize(500, 100)
        self.setMaximumSize(700, 300)
        self.resize(500, 100)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # layouts
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)

        # self.radio_buttons_layout = QHBoxLayout()
        self.radio_buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.radio_buttons_layout)
        self.radio_test_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.radio_test_layout)

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.buttons_layout)

        # radiobuttons
    def create_radio_buttons(self):
        self.bg1 = QtWidgets.QButtonGroup()
        self.rbutton_Sphere = QtWidgets.QRadioButton("Sphere")
        self.rbutton_Sphere.setChecked(True)
        self.rbutton_Cube = QtWidgets.QRadioButton("Cube")
        self.rbutton_Cone = QtWidgets.QRadioButton("Cone")
        self.radio_buttons_layout.addWidget(self.rbutton_Sphere)
        self.radio_buttons_layout.addWidget(self.rbutton_Cube)
        self.radio_buttons_layout.addWidget(self.rbutton_Cone)
        self.bg1.addButton(self.rbutton_Sphere)
        self.bg1.addButton(self.rbutton_Cube)
        self.bg1.addButton(self.rbutton_Cone)

        self.bg2 = QtWidgets.QButtonGroup()
        self.r1 = QtWidgets.QRadioButton("r1")
        self.r2 = QtWidgets.QRadioButton("r2")
        self.r3 = QtWidgets.QRadioButton("r3")
        self.radio_test_layout.addWidget(self.r1)
        self.radio_test_layout.addWidget(self.r2)
        self.radio_test_layout.addWidget(self.r3)
        self.bg2.addButton(self.r1)
        self.bg2.addButton(self.r2)
        self.bg2.addButton(self.r3)

        # buttons & signals
    def create_buttons(self):
        self.button_OK = QtWidgets.QPushButton("OK")
        self.button_OK.clicked.connect(self.on_button_ok_clicked)

        self.button_Apply = QtWidgets.QPushButton("Apply")
        self.button_Apply.clicked.connect(self.on_button_apply_clicked)

        self.button_Cancel = QtWidgets.QPushButton("Cancel")
        self.button_Cancel.clicked.connect(self.close)

        self.buttons_layout.addWidget(self.button_OK)
        self.buttons_layout.addWidget(self.button_Apply)
        self.buttons_layout.addWidget(self.button_Cancel)

    def on_button_ok_clicked(self):
        self.on_button_apply_clicked()
        self.close()

    def on_button_apply_clicked(self):
        if self.rbutton_Sphere.isChecked():
            cmds.polySphere()
        elif self.rbutton_Cube.isChecked():
            cmds.polyCube()
        elif self.rbutton_Cone.isChecked():
            cmds.polyCone()

    # EVENTS
    def enterEvent(self, event):
        print("enter")
        super(MyWindow, self).enterEvent(event)

    def leaveEvent(self, event):
        print("leave")
        super(MyWindow, self).leaveEvent(event)

    def mousePressEvent(self, event):
        print("press")
        super(MyWindow, self).mousePressEvent(event)

if cmds.window("MyTestUI", q=1, exists=True):
    cmds.deleteUI("MyTestUI")

if cmds.windowPref("MyTestUI", exists=True):
    cmds.windowPref("MyTestUI", remove=1)

a = MyWindow()
a.show()