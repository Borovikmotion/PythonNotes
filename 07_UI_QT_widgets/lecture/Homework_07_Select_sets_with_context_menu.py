import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui


# rename window 
class MyChildDialog(QtWidgets.QDialog):

    buttonSignal = QtCore.Signal(str)

    def __init__(self, parent = None):
        super(MyChildDialog, self).__init__()
        self.setFixedSize(300,100)
        self.setObjectName("myCustomSignalExampleChildWindow_Pointer")
        self.setWindowTitle("Rename Selection Set")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.label_top = QtWidgets.QLabel("Enter new name:")

        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.textField = QtWidgets.QLineEdit()

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.button_Apply = QtWidgets.QPushButton("Apply") 
        self.button_Apply.clicked.connect(self.buttonPressed)
        self.button_Cancel = QtWidgets.QPushButton("Cancel") 
        self.button_Cancel.clicked.connect(self.buttonCancelPressed)

        self.mainLayout.addWidget(self.label_top)
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addLayout(self.buttons_layout)
        self.buttons_layout.addWidget(self.button_Apply)
        self.buttons_layout.addWidget(self.button_Cancel)

    def buttonPressed(self):
        text = self.textField.text()
        if text:
            self.buttonSignal.emit(text)
        self.close()
    
    def buttonCancelPressed(self):
        self.close()


# selection set widget 
class SelectionSetWidget(QtWidgets.QWidget):
    
    setClicked = QtCore.Signal(list)
    removeSetClicked = QtCore.Signal(int)

    def __init__(self, objects, number):
        super(SelectionSetWidget, self).__init__()

        self.objects = objects
        self.text = "Selection Set " + str(number)
        self.state = True
        self.number = number
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(270, 44)
        self.setMaximumHeight(60)
        self.set_background()

        # layout
        self.main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.main_layout)

        self.label_ = QtWidgets.QLabel(self.text)
        self.main_layout.addWidget(self.label_)
        self.label_.setAlignment(QtCore.Qt.AlignCenter)

        # CUSTOM MENU
        self.popMenu = QtWidgets.QMenu(self)

        self.popMenuRenameSelectionSet = QtWidgets.QAction('Rename selection set', self)
        self.popMenu.addAction(self.popMenuRenameSelectionSet)
        self.popMenuRenameSelectionSet.triggered.connect(self.renameSelectionSet)

        self.popMenuAddObjects = QtWidgets.QAction('Add objects to set', self)
        self.popMenu.addAction(self.popMenuAddObjects)
        self.popMenuAddObjects.triggered.connect(self.addObjectsToSet)

        self.popMenuDeleteObjects = QtWidgets.QAction('Remove objects from set', self)
        self.popMenu.addAction(self.popMenuDeleteObjects)
        self.popMenuDeleteObjects.triggered.connect(self.deleteObjectsFromSet)

        self.popMenuSelectObjects = QtWidgets.QAction('Select objects', self)
        self.popMenu.addAction(self.popMenuSelectObjects)
        self.popMenuSelectObjects.triggered.connect(self.selectObjects)

        self.popMenuRemoveSet = QtWidgets.QAction('Delete selection set', self)
        self.popMenu.addAction(self.popMenuRemoveSet)
        self.popMenuRemoveSet.triggered.connect(self.removeSet)

        self.setMouseTracking(True)  
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)

    def set_background(self, r=50, g=50, b=50):
        self.setAutoFillBackground(True)
        self.p = QtGui.QPalette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(r,g,b))
        self.setPalette(self.p)

    # EVENTS
    def enterEvent(self, event):
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.set_background(75, 75, 75)
    
    def leaveEvent(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.set_background(50, 50, 50)
    
    def mousePressEvent(self, event):
        self.set_background(85, 85, 85)
        if event.buttons() == QtCore.Qt.LeftButton:
            self.state = True
        elif event.buttons() == QtCore.Qt.RightButton:
            self.state = False

    def mouseReleaseEvent(self, event):
        self.set_background(75, 75, 75)
        if self.state == True:
            self.setClicked.emit(self.objects)

    # CONTEXT MENU
    def onContextMenu(self, point):
        self.popMenu.exec_(self.mapToGlobal(point))
    
    def renameSelectionSet(self):
        print ("Enter new name")
        self.chld = MyChildDialog(parent = self)
        self.chld.show()
        self.chld.buttonSignal.connect(self.receiveRenameSignal)

    def receiveRenameSignal(self, text = None):
        # self.textField.setText(text)
        self.text = text
        self.label_.setText(self.text)


    def addObjectsToSet(self):
        selectedObjects = cmds.ls(sl=1, l=1)
        for obj in selectedObjects:
            if obj not in self.objects:
                self.objects.append(obj)
        print ("Objects have been to selection set")

    def deleteObjectsFromSet(self):
        selectedObjects = cmds.ls(sl=1, l=1)
        for obj in selectedObjects:
            if obj in self.objects:
                self.objects.remove(obj)
        print ("Objects have been removed from set")

    def selectObjects(self):
        cmds.select(self.objects)
        print ("Objects have been selected")

    def removeSet(self):
        print ("Selection set have been removed")
        self.removeSetClicked.emit(self.number)


# Main window
class MyCustomWidget(QtWidgets.QDialog):
    def __init__(self):
        super(MyCustomWidget, self).__init__()

        self.selection = []
        self.get_selection()
        self.createdSets = {}
        self.i = 0
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Selection Sets")
        self.setObjectName("MyCustomWidgetUIId")
        self.setMinimumSize(300, 500)
        self.resize(300, 500)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(5,5,5,5)
        self.main_layout.setSpacing(5)
        self.setLayout(self.main_layout)

        # scroll area -------------------------------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(290)
        # self.scrollArea.setMaximumWidth(390)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,5,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.main_layout.addWidget(self.scrollArea) #add to main layout
        #--------------------------------------------------

        # add button
        self.button_add = QtWidgets.QPushButton("Add Set")
        self.button_add.setMinimumHeight(44)
        self.button_add.clicked.connect(self.on_button_add_clicked)
        self.main_layout.addWidget(self.button_add)

    def on_button_add_clicked(self):
        self.get_selection()
        self.add_widget_for_selection()
        # print ("add")

    def get_selection(self):
        self.selection = cmds.ls(sl=1, l=1)

    def add_widget_for_selection(self):
        self.selection_set_wgt = SelectionSetWidget(self.selection, self.i)
        self.createdSets[self.i] = self.selection_set_wgt
        self.i = self.i + 1

        self.scroll_layout.addWidget(self.selection_set_wgt)
        self.selection_set_wgt.setClicked.connect(self.select_objects)
        self.selection_set_wgt.removeSetClicked.connect(self.remove_set)
    
    def select_objects(self, objects):
        cmds.select(objects)

    def remove_set(self, number):
        widget = self.createdSets[number]
        if widget:
            widget.deleteLater()
        print (number)

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

