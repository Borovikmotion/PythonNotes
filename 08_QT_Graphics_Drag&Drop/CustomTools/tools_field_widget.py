import maya.cmds as cmds
import json
import os
from PySide2 import QtWidgets, QtGui, QtCore

from tool_widget import ToolWidget

class ToolsFieldWidget(QtWidgets.QWidget):
    
    toolsFiledSignal = QtCore.Signal(str)

    def __init__(self):
        super(ToolsFieldWidget, self).__init__()
        self.setFixedSize(300, 490)
        self.setAcceptDrops(True)
        self.tools_list = []
        self.setup_UI()

    def setup_UI(self):
        #bg color
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(40,40,40))
        self.setPalette(self.p)

        #add layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(3,3,2,2)

        # scroll area -------------------------------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(290)
        # self.scrollArea.setMaximumWidth(390)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,5,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.main_layout.addWidget(self.scrollArea) #add to main layout
        #--------------------------------------------------

    def add_tools_from_list(self, list):
        for i in list:
            tool = ToolWidget(label = str(i))
            self.scroll_layout.addWidget(tool)
            self.tools_list.append(i)

    def add_test_buttons(self):
        for i in "ABCDEFGHIJK":
            button = ToolWidget(label = "Tool_" + str(i))
            self.scroll_layout.addWidget(button)
            self.tools_list.append("Tool_" + str(i))

    # def add_tool(self, tool_name):
    #     tool = ToolWidget(label = tool_name)
    #     self.scroll_layout.addWidget(tool)

    def dragEnterEvent(self, event):
        # print ("entered")
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        # print ("move")
        event.acceptProposedAction()

    def dropEvent(self, event):
        # print ("droped")
        
        mimeData = event.mimeData()
        tool_name = mimeData.get_text()
        # widget = mimeData.from_widget

        #push a signal saying we should delete widget which is no longer in use 
        self.toolsFiledSignal.emit(tool_name)

        #delete old widget
        event.source().deleteLater()

        new_tool = ToolWidget(tool_name)
        self.scroll_layout.addWidget(new_tool)