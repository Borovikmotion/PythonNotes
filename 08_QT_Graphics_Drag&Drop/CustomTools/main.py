import maya.cmds as cmds
import json
import os
from PySide2 import QtWidgets, QtCore, QtGui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from tools_choose_window import MyToolsChooseWindow
from tool_widget import ToolWidget



json_path = "C:/Tools"
json_name = "Tools_list.json"



# DOCK WINDOW
class MyCustomToolsWidget(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):
    def __init__(self, json_path, json_name):
        super(MyCustomToolsWidget, self).__init__()
        self.setDockableParameters(width = 300)

        self.child = None
        self.json_data = {}
        self.json_path = json_path
        self.json_name = json_name

        # create json folder
        if not os.path.exists(self.json_path):
            os.mkdir(self.json_path)

        self.active_tools = []
        self.get_active_tools()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("My Custom UI")
        self.setObjectName("MyCustomToolsWidgetUIId")
        self.setMinimumSize(300, 500)
        self.resize(300, 500)

        # an invisible widget
        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)

        #main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(5,5,1,5)
        self.main_layout.setSpacing(5)
        self.mainWidget.setLayout(self.main_layout)

        # scroll area -------------------------------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(290)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,5,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.main_layout.addWidget(self.scrollArea) #add to main layout
        #--------------------------------------------------

        #Options button
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.btn_layout)
        self.button_options = QtWidgets.QPushButton("Options")
        self.button_options.setMinimumHeight(40)
        self.button_options.setMinimumWidth(120)
        self.button_options.clicked.connect(self.on_button_options_clicked)
        self.btn_layout.addWidget(self.button_options)

        if os.path.exists(self.json_path + "/" + self.json_name):
            self.json_data = self.read_json(path = self.json_path, name = self.json_name)
            for i in self.json_data["CurrentTools"]:
                wgt = ToolWidget(i)
                self.scroll_layout.addWidget(wgt)

    def get_active_tools(self):
        if os.path.exists(json_path + "/" + json_name):
            print("reading tools list from json file")
            # self.json_data = self.read_json(path = self.json_path, name = self.json_name)
        else:
            print("there is no json tools list")
            # self.json_data = self.read_json(path = self.json_path, name = self.json_name)
    
    # read json
    def read_json(self, path, name):
        with open (path + "/" + name, "r") as f:
            jsonData  = json.load(f)
        return jsonData

    def on_button_options_clicked(self):
            # delete current widgets
        if self.scroll_layout.count():
            for i in range (self.scroll_layout.count()):
                item = self.scroll_layout.itemAt(i)
                widget = item.widget()
                if widget:
                    widget.deleteLater()


        # call a new window
        if os.path.exists(self.json_path + "/" + self.json_name):
            self.json_data = self.read_json(path = self.json_path, name = self.json_name)
        self.child = MyToolsChooseWindow(json_data = self.json_data, json_path = self.json_path, json_name = self.json_name, parent = self)
        self.child.toolsChooseSignal.connect(self.reload_tools)
        self.child.show()


    def reload_tools(self):
        self.json_data = self.read_json(path = self.json_path, name = self.json_name)
        self.child.close()
        for i in self.json_data["CurrentTools"]:
            wgt = ToolWidget(i)
            self.scroll_layout.addWidget(wgt)
        


def main():

    #dockable thing
    if cmds.workspaceControl('MyCustomToolsWidgetUIIdWorkspaceControl', exists=True):
        cmds.deleteUI('MyCustomToolsWidgetUIIdWorkspaceControl', control = True)
        
    if cmds.workspaceControlState('MyCustomToolsWidgetUIIdWorkspaceControl', exists=True):
        cmds.workspaceControlState('MyCustomToolsWidgetUIIdWorkspaceControl', remove=1)
        
    myUI = MyCustomToolsWidget(json_path = json_path, json_name = json_name)
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl('MyCustomToolsWidgetUIIdWorkspaceControl',
                            label = 'MyCustomToolsWidget',
                            edit = 1,
                            tabToControl = ['AttributeEditor', -1],
                            widthProperty = 'fixed',
                            initialWidth = 300)


if __name__ == "__main__":
    main()


