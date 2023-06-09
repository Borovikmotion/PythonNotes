import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_UI()
        self.xOffset = 0
        self.objectName = "Object_Name"
        self.obj = None

    def setup_UI(self):
        self.setWindowTitle("Create Poly Objects")
        self.setMinimumSize(500, 130)
        self.setMaximumSize(1000, 130)
        self.resize(500, 130)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)

        # line edit text
        self.ledit_object_name = QtWidgets.QLineEdit("Object_Name")
        self.main_layout.addWidget(self.ledit_object_name)
        self.ledit_object_name.textChanged.connect(self.on_object_name_changed)

        # radiobuttons
        self.radio_buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.radio_buttons_layout)
        self.buttonGroup1 = QtWidgets.QButtonGroup()
        self.rbutton_Sphere = QtWidgets.QRadioButton("Sphere")
        self.rbutton_Cube = QtWidgets.QRadioButton("Cube")
        self.rbutton_Cone = QtWidgets.QRadioButton("Cone")
        self.radio_buttons_layout.addWidget(self.rbutton_Sphere)
        self.radio_buttons_layout.addWidget(self.rbutton_Cube)
        self.radio_buttons_layout.addWidget(self.rbutton_Cone)
        self.buttonGroup1.addButton(self.rbutton_Sphere)
        self.buttonGroup1.addButton(self.rbutton_Cube)
        self.buttonGroup1.addButton(self.rbutton_Cone)
        self.rbutton_Sphere.setChecked(True)

        # slider
        self.slider_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.slider_layout)
        self.slider_xOffset = QtWidgets.QSlider()
        self.slider_xOffset.setOrientation(QtCore.Qt.Horizontal)
        self.slider_layout.addWidget(self.slider_xOffset)
        self.slider_xOffset.setMinimum(0)
        self.slider_xOffset.setMaximum(10)
        self.slider_xOffset.setMinimumWidth((self.width()/3)*2)
        self.slider_xOffset.valueChanged.connect(self.on_slider_value_changed)

        # slider value text
        self.ledit_slider_value = QtWidgets.QLineEdit("0")
        self.slider_layout.addWidget(self.ledit_slider_value)

        # buttons
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.buttons_layout)
        self.button_OK = QtWidgets.QPushButton("Create")
        self.button_OK.clicked.connect(self.on_button_ok_clicked)
        self.button_Apply = QtWidgets.QPushButton("Apply")
        self.button_Apply.clicked.connect(self.on_button_apply_clicked)
        self.button_Cancel = QtWidgets.QPushButton("Close")
        self.button_Cancel.clicked.connect(self.close)
        self.buttons_layout.addWidget(self.button_OK)
        self.buttons_layout.addWidget(self.button_Apply)
        self.buttons_layout.addWidget(self.button_Cancel)

    def on_slider_value_changed(self):
        self.xOffset = self.slider_xOffset.value()
        self.ledit_slider_value.setText(str(self.xOffset))
        # print(self.xOffset)
    
    def on_object_name_changed(self):
        self.objectName = self.ledit_object_name.displayText()
        # print(self.ObjectName)

    def on_button_ok_clicked(self):
        self.on_button_apply_clicked()
        self.close()

    def create_object(self):
        if self.rbutton_Sphere.isChecked():
            self.obj = cmds.polySphere(n = self.objectName)[0]
        elif self.rbutton_Cube.isChecked():
            self.obj = cmds.polyCube(n = self.objectName)[0]
        elif self.rbutton_Cone.isChecked():
            self.obj = cmds.polyCone(n = self.objectName)[0]

    def move_object(self):
        cmds.setAttr(self.obj + ".translateX", self.xOffset)

    def on_button_apply_clicked(self):
        if not self.objectName:
            self.objectName = "Object"
        elif self.objectName[0] == "0" or self.objectName[0] == "1" or self.objectName[0] == "2" or self.objectName[0] == "3" or self.objectName[0] == "4" or self.objectName[0] == "5" or self.objectName[0] == "6" or self.objectName[0] == "7" or self.objectName[0] == "8" or self.objectName[0] == "9":
            self.objectName = "Object"
        self.create_object()
        self.move_object()
    
    def resizeEvent(self, event):
        # print("resize")
        super(MyWindow, self).resizeEvent(event)
        self.slider_xOffset.setMinimumWidth((self.width()/3)*2)


if cmds.window("MyTestUI", q=1, exists=True):
    cmds.deleteUI("MyTestUI")

if cmds.windowPref("MyTestUI", exists=True):
    cmds.windowPref("MyTestUI", remove=1)

window = MyWindow()
window.show()
