
# ________________CUSTTOM WIDGETS___________________
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# QDialog 
# QMainWindow

# styles
button2Style = """
    QPushButton#MyCustomButtonWidgetId{
        background-color: rgb(109,113,168);
        border-radius: 8px;
        min-width: 30px;
        min-height: 25px;
        font-weight: 900;

    }
    QPushButton#MMyCustomButtonWidgetId:hover {
        background-color: rgb(255,133,198);
        min-width: 30px;
        min-height: 25px;  
    }
    """

button1Style = """
    QPushButton#MyCustomButtonWidgetId{
        background-color: rgb(246,93,205);
        border-radius: 8px;
        min-width: 30px;
        min-height: 25px;
        font-weight: 900;

    }
    QPushButton#MMyCustomButtonWidgetId:hover {
        background-color: rgb(255,255,255);
        min-width: 30px;
        min-height: 25px;  
    }
    """


class ObjectWidget(QtWidgets.QWidget):
    def __init__(self, object_path):
        super(ObjectWidget, self).__init__()

        self.object_path = object_path
        self.display_name = self.object_path.split("|")[-1]

        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(270, 44)
        self.setMaximumHeight(60)

        self.set_background()

        # layout
        self.main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.main_layout)

        # checkbox
        self.checkbox = QtWidgets.QCheckBox(self.display_name)
        visibility_state = cmds.getAttr(self.object_path + ".visibility")
        self.checkbox.setChecked(visibility_state)
        self.checkbox.toggled.connect(self.on_checkbox_toggled)
        self.main_layout.addWidget(self.checkbox)

        #button
        self.btn_delete = QtWidgets.QPushButton("Delele")
        self.btn_delete.setObjectName("MyCustomButtonWidgetId")
        self.btn_delete.setMaximumWidth(60)
        self.btn_delete.setStyleSheet(button2Style)
        self.btn_delete.clicked.connect(self.on_button_del_clicked)
        self.main_layout.addWidget(self.btn_delete)

    def set_background(self, r=50, g=50, b=50):
        #set background
        self.setAutoFillBackground(True)
        self.p = QtGui.QPalette()

        # RGB
        self.p.setColor(self.backgroundRole(), QtGui.QColor(r,g,b))
        self.setPalette(self.p)

        # HSV
        # self.color = QtGui.QColor()
        # self.color.setHsv(146, 60, 100)
        # self.p.setColor(self.backgroundRole(), self.color)
        # self.setPalette(self.p)

    def on_button_del_clicked(self):
        # print ("clicked")
        cmds.delete(self.object_path)
        self.deleteLater()

    def on_checkbox_toggled(self, state):
        # print(state)
        cmds.setAttr(self.object_path + ".visibility", state)

    # def mousePressEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton:
    #         print("clicked with event")

    def enterEvent(self, event):
        # print("entered")
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.set_background(75, 75, 75)
    
    def leaveEvent(self, event):
        # print("left")
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.set_background(50, 50, 50)
    
    def mousePressEvent(self, event):
        self.set_background(85, 85, 85)

    def mouseReleaseEvent(self, event):
        self.set_background(75, 75, 75)

        state = self.checkbox.isChecked()
        self.checkbox.setChecked(not state)

#dock thing for putting to the right panel, regular widget would inherit only q widget q dialog class like this:
# class MyCustomWidget(QtWidgets.QDialog):

class MyCustomWidget(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):
    def __init__(self):
        super(MyCustomWidget, self).__init__()

        self.setDockableParameters(width = 300)

        self.selection = []
        self.get_selection()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("My Custom UI")
        self.setObjectName("MyCustomWidgetUIId")
        self.setMinimumSize(300, 500)
        self.resize(300, 500)

        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(5,5,1,5)
        self.main_layout.setSpacing(5)
        # self.setLayout(self.main_layout)
        self.mainWidget.setLayout(self.main_layout)

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

        #test buttons
        # self.btn1 = QtWidgets.QPushButton("test1")
        # self.main_layout.addWidget(self.btn1)
        # self.btn2 = QtWidgets.QPushButton("test1")
        # self.main_layout.addWidget(self.btn2)

        # #test custom widgets
        # self.owgt1 = ObjectWidget()
        # self.main_layout.addWidget(self.owgt1)
        # self.owgt2 = ObjectWidget()
        # self.main_layout.addWidget(self.owgt2)
        # self.owgt3 = ObjectWidget()
        # self.main_layout.addWidget(self.owgt3)

        # custom widgets
        self.populate_selection()

        # update button
        self.button_update = QtWidgets.QPushButton("Update")
        self.button_update.setObjectName("MyCustomButtonWidgetId")
        self.button_update.clicked.connect(self.on_button_update_clicked)
        self.button_update.setStyleSheet(button1Style)
        self.main_layout.addWidget(self.button_update)

    def on_button_update_clicked(self):
        # delete current widgets
        if self.scroll_layout.count():
            for i in range (self.scroll_layout.count()):
                item = self.scroll_layout.itemAt(i)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        self.get_selection()
        self.populate_selection()

    def get_selection(self):
        self.selection = cmds.ls(sl=1, l=1)
    
    def populate_selection(self):
        for i in self.selection:
            self.object_wgt = ObjectWidget(i)
            self.scroll_layout.addWidget(self.object_wgt)

def main():

    # A regular way to do window thing
    # if cmds.window("MyCustomWidgetUIId", exists=1):
    #     cmds.deleteUI("MyCustomWidgetUIId")
    
    # if cmds.windowPref("MyCustomWidgetUIId", exists=1):
    #     cmds.windowPref("MyCustomWidgetUIId", remove=1)

    # global myUI
    # myUI = MyCustomWidget()
    # myUI.show()

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

# global - python garbage collection 
