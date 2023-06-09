import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class ToolWidgetMimeData(QtCore.QMimeData):
    def __init__(self):
        super(ToolWidgetMimeData, self).__init__()

        self.some_text = ""
    
    def set_text(self, text):
        self.some_text = text
    
    def get_text(self):
        return self.some_text

class ToolWidget(QtWidgets.QWidget):
    def __init__(self, label):
        super(ToolWidget, self).__init__()
        self.tool_name = label
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(270, 60)
        self.setMaximumHeight(60)
        self.set_background()

        # layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        #label
        self.label_ = QtWidgets.QLabel(self.tool_name)
        self.main_layout.addWidget(self.label_)
        self.label_.setAlignment(QtCore.Qt.AlignCenter)

    def set_background(self, r=50, g=50, b=50):
        #set background
        self.setAutoFillBackground(True)
        self.p = QtGui.QPalette()

        # RGB
        self.p.setColor(self.backgroundRole(), QtGui.QColor(r,g,b))
        self.setPalette(self.p)

    def set_label(self, text):
        self.label_.setText(text)

    # EVENTS
    # def enterEvent(self, event):
    #     # print("entered")
    #     self.setCursor(QtCore.Qt.PointingHandCursor)
    #     self.set_background(75, 75, 75)
    
    # def leaveEvent(self, event):
    #     # print("left")
    #     self.setCursor(QtCore.Qt.ArrowCursor)
    #     self.set_background(50, 50, 50)
    
    def mousePressEvent(self, event):
        self.set_background(85, 85, 85)

    def mouseReleaseEvent(self, event):
        self.set_background(75, 75, 75)

    # DRAG AND DROP
    def mouseMoveEvent(self, event):
        if event.buttons() != QtCore.Qt.LeftButton:
            return
        
        mimeData = ToolWidgetMimeData()
        mimeData.set_text(self.label_.text())
        # mimeData.from_widget = self

        # create transparent image behind the moving mouse cursor
        self.pixmap = self.grab()
        painter = QtGui.QPainter(self.pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(self.pixmap.rect(), QtGui.QColor(80,80, 80, 127))
        painter.end()

        # put MIME DTATA
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(self.pixmap)
        drag.setHotSpot(event.pos())

        # drag MAIN THING
        drag.exec_(QtCore.Qt.LinkAction | QtCore.Qt.MoveAction)

