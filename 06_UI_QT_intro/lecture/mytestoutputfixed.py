# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myTest.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets

class MyUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyUI, self).__init__()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_CreateSphere = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_CreateSphere.setObjectName("btn_CreateSphere")
        self.verticalLayout.addWidget(self.btn_CreateSphere)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 360, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 283, 22))
        self.menubar.setObjectName("menubar")
        self.menuHello = QtWidgets.QMenu(self.menubar)
        self.menuHello.setObjectName("menuHello")
        self.menuHaha = QtWidgets.QMenu(self.menubar)
        self.menuHaha.setObjectName("menuHaha")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShere = QtWidgets.QAction(MainWindow)
        self.actionShere.setObjectName("actionShere")
        self.menuHello.addAction(self.actionShere)
        self.menubar.addAction(self.menuHello.menuAction())
        self.menubar.addAction(self.menuHaha.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_CreateSphere.setText(_translate("MainWindow", "CreateSphere"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuHello.setTitle(_translate("MainWindow", "Hello"))
        self.menuHaha.setTitle(_translate("MainWindow", "Haha"))
        self.actionShere.setText(_translate("MainWindow", "Shere"))

MyUI_instance = MyUI()
UI_generated = Ui_MainWindow()
UI_generated.setupUi(MyUI_instance)
MyUI_instance.show()