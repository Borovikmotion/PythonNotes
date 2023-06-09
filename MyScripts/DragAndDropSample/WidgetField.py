"""
This is a field widget that accepts drops
"""

# style="""
#     QScrollBar:vertical {
#         background: rgb(120, 120, 120);
#         width: 5px;
#         margin: 0px 0 0px 0;
#         }
#     QScrollBar::handle:vertical {
#         border: 1px rgb(120, 120, 120);
#         background: rgb( 120, 120,  120 );
#         }

# }
# """

# style="""
#     QScrollBar:vertical {
#         background: rgb(40, 40, 40);
#         width: 5px;
#         margin: 0px 0 0px 0;
#         }
#     QScrollBar::handle:vertical {
#         border: 1px rgb(120, 120, 120);
#         background: rgb( 40, 40,  40 );
#         }
# """

from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds

from DragAndDropSample.WidgetButton import WidgetButton

class WidgetField(QtWidgets.QWidget):
    def __init__(self):
        super(WidgetField, self).__init__()
        self.setFixedSize(240, 490)
        self.setAcceptDrops(True)

        #bg color
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(40,40,40))
        self.setPalette(self.p)

        #add layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(3,3,2,2)

        #scroll
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setMinimumHeight(200)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll_area.setStyleSheet(style)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)

        self.scroll_layout = QtWidgets.QGridLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,3,0)
        self.scroll_layout.setSpacing(5)
        self.scroll_area_widget.setLayout(self.scroll_layout)

        self.main_layout.addWidget(self.scroll_area)

    def add_test_buttons(self):
        for i in range(4):
            button = WidgetButton(label = "Button_" + str(i))
            self.scroll_layout.addWidget(button)

    def dragEnterEvent(self, event):
        # print ("entered")
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        # print ("move")
        event.acceptProposedAction()

    def dropEvent(self, event):
        # print ("droped")
        
        mimeData = event.mimeData()
        text = mimeData.get_text()
        # widget = mimeData.from_widget

        event.source().deleteLater()

        button = WidgetButton()
        button.set_label(text)

        self.scroll_layout.addWidget(button)