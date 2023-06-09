import maya.cmds as cmds
import json
import os
from PySide2 import QtWidgets, QtCore, QtGui
from tools_field_widget import ToolsFieldWidget

# Main window
class MyToolsChooseWindow(QtWidgets.QDialog):

    toolsChooseSignal = QtCore.Signal()

    def __init__(self, json_data, json_path, json_name, parent = None):
        super(MyToolsChooseWindow, self).__init__()

        self.json_data = json_data
        self.json_path = json_path
        self.json_name = json_name
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Choose Tools")
        self.setObjectName("MyToolsChooseWindowUIId")
        self.setMinimumSize(600, 550)
        self.setMaximumSize(600, 550)
        self.resize(600, 550)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # main layout 
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        #field layout
        self.fields_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.fields_layout)

        # ------- add two fields for tools --------------
        #Full list
        self.full_list = ToolsFieldWidget()
        self.full_list.toolsFiledSignal.connect(self.receive_signal_from_full_list)

        if not os.path.exists(self.json_path + "/" + self.json_name):
            print("as there is no json file yet, generating a list of tools in the left column")
            self.full_list.add_test_buttons()
        else:
            # print(self.json_data)
            # print(self.json_data["NotUsedTools"])
            self.full_list.add_tools_from_list(self.json_data["NotUsedTools"])
        
        self.fields_layout.addWidget(self.full_list)

        #current list 
        self.current_list = ToolsFieldWidget()
        self.current_list.toolsFiledSignal.connect(self.receive_signal_from_current_list)

        if os.path.exists(self.json_path + "/" + self.json_name):
            self.current_list.add_tools_from_list(self.json_data["CurrentTools"])
            pass
        
        self.fields_layout.addWidget(self.current_list)
        # --------------------------------------------

        # Save Button
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.btn_layout)

        self.button_save = QtWidgets.QPushButton("Save")
        self.button_save.setMinimumHeight(40)
        self.button_save.setMinimumWidth(120)
        self.button_save.clicked.connect(self.on_button_save_clicked)
        self.btn_layout.addWidget(self.button_save)
        self.btn_layout.setAlignment(QtCore.Qt.AlignCenter)

    def on_button_save_clicked(self):
        self.json_data["NotUsedTools"] = self.full_list.tools_list
        self.json_data["CurrentTools"] = self.current_list.tools_list
        print(self.json_data)
        self.write_json(path = self.json_path, name = self.json_name)
        self.toolsChooseSignal.emit()

    def write_json(self, path, name):
        with open (path + "/" + name, "w") as f:
            f.write(json.dumps(self.json_data, indent = 4, sort_keys = True))

    def receive_signal_from_full_list(self, tool_name = None):
        self.full_list.tools_list.append(tool_name)
        self.current_list.tools_list.remove(tool_name)
    
    def receive_signal_from_current_list(self, tool_name = None):
        self.full_list.tools_list.remove(tool_name)
        self.current_list.tools_list.append(tool_name)

def main():
    # A regular way to do window thing
    if cmds.window("MyToolsChooseWindowUIId", exists=1):
        cmds.deleteUI("MyToolsChooseWindowUIId")
    
    if cmds.windowPref("MyToolsChooseWindowUIId", exists=1):
        cmds.windowPref("MyToolsChooseWindowUIId", remove=1)

    global myUI
    myUI = MyToolsChooseWindow()
    myUI.show()

if __name__ == "__main__":
    main()









