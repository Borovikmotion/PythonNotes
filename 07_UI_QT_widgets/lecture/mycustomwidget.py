import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


button2Style = """
    QPushButton#MyCustomButtonWidgetID{
        background-color: rgb(109,113,168);
        border-radius: 10px;
        min-width: 30px;
        min-height: 30px;
        font-weight: 900;


    }
    QPushButton#MyCustomButtonWidgetID:hover {
        background-color: rgb(255,133,198);
        min-width: 30px;
        min-height: 30px;  
    }
    """


class ObjectWidget(QtWidgets.QWidget):
    def __init__(self, object_path):
        super(ObjectWidget, self).__init__()

        self.object_path = object_path
        self.display_name = self.object_path.split("|")[-1]

        self.setup_ui()


    def setup_ui(self):

        self.setMinimumSize(260, 40)
        self.setMaximumHeight(40)

        self.setAutoFillBackground(True)

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

        # button delete
        self.btn_delete = QtWidgets.QPushButton("Del")
        self.btn_delete.setObjectName("MyCustomButtonWidgetID")
        self.btn_delete.setMaximumWidth(30)
        # self.btn_delete.setStyleSheet(button2Style)
        self.btn_delete.clicked.connect(self.on_button_del_clicked)
        self.main_layout.addWidget(self.btn_delete)


    def set_background(self, r=60, g=60, b=60):
        # set background
        self.p = QtGui.QPalette()
        self.color = QtGui.QColor(r,g,b)
        self.p.setColor(self.backgroundRole(), self.color) 
        self.setPalette(self.p)


    def on_checkbox_toggled(self, state):
        cmds.setAttr(self.object_path + ".visibility", state)

    def on_button_del_clicked(self):
        cmds.delete(self.object_path)
        self.deleteLater()

    def enterEvent(self, event):
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.set_background(75,75,75)

    def leaveEvent(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.set_background()

    def mousePressEvent(self, event):
        self.set_background(85,85,85)
    
    def mouseReleaseEvent(self, event):
        self.set_background(75,75,75)
        state = self.checkbox.isChecked()
        self.checkbox.setChecked(not state)
    


scroll_style = """
    QScrollBar:vertical {
        background: rgb(10,10,10);
        width: 5px;
        margin: 0px 0 0px 0;
        }

    QScrollBar::handle:vertical {
        border: 1px rgb(0, 0, 0);
        background: rgb(255, 85, 85);
        }
"""



class MyCustomWidget(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):
    def __init__(self):
        super(MyCustomWidget, self).__init__()

        # self.setDockableParameters(widht = 300)
        self.setFloating(False)
        self.selection = []

        self.get_selection()
        self.setup_ui()


    def setup_ui(self):

        self.setWindowTitle("My Custom UI")
        self.setObjectName("MyCustomWidgetUIId")
        self.setMinimumSize(300, 500)
        self.resize(300,500)

        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop) 
        self.main_layout.setContentsMargins(5,5,0,5)
        self.main_layout.setSpacing(3)
        self.mainWidget.setLayout(self.main_layout)


        #* scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(290)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scrollbar = QtWidgets.QScrollBar()
        self.scrollbar.setStyleSheet(scroll_style)
        self.scrollArea.setVerticalScrollBar(self.scrollbar)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)

        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,5,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.main_layout.addWidget(self.scrollArea) #add to main layout
        #* --------------------------------

        self.populate_selection()


        # update button
        self.button_udpate = QtWidgets.QPushButton("Update")
        self.button_udpate.clicked.connect(self.on_button_update_clicked)
        self.main_layout.addWidget(self.button_udpate)

    def on_button_update_clicked(self):
        if self.scroll_layout.count(): # if layout has any children
            for i in range(self.scroll_layout.count()): #[0,1,2,3,4]
                item = self.scroll_layout.itemAt(i)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        self.get_selection()

        # create custom widgets in a cycle
        self.populate_selection()


    def get_selection(self):
        self.selection = cmds.ls(sl=1,l=1)
        # [u'|group4|group3|group2|group1|pSphere2', u'|pSphere4', u'|pSphere3', u'|pSphere1']


    def populate_selection(self):
        # create custom widgets in a cycle
        for i in self.selection:
            self.object_wgt = ObjectWidget(i)
            self.scroll_layout.addWidget(self.object_wgt)







def main():

    # if cmds.window("MyCustomWidgetUIId", exists=1):
    #     cmds.deleteUI("MyCustomWidgetUIId")

    # if cmds.windowPref("MyCustomWidgetUIId", exists=1):
    #     cmds.windowPref("MyCustomWidgetUIId", remove=1)

    # global myUI
    # myUI = MyCustomWidget()
    # myUI.show()

    if cmds.workspaceControl('MyCustomWidgetUIIdWorkspaceControl', exists=True):
        cmds.deleteUI('MyCustomWidgetUIIdWorkspaceControl', control = True)
        cmds.workspaceControlState('MyCustomWidgetUIIdWorkspaceControl', remove=1)

    global myUI
    myUI = MyCustomWidget()
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl(  "MyCustomWidgetUIIdWorkspaceControl",
                                edit=1,
                                r=1, # raise to the top and make it active
                                tabToControl=["AttributeEditor", -1],
                                floating=False,
                                initialWidth=300,
                                minimumWidth=300,
                                widthProperty="preferred",
                                label="MyCustomWidget")


if __name__ == "__main__":
    main()