from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds

class WidgetButtonMimeData(QtCore.QMimeData):
    def __init__(self):
        super(WidgetButtonMimeData, self).__init__()

        self.some_text = ""
        # self.from_widget = None
    
    def set_text(self, text):
        self.some_text = text
    
    def get_text(self):
        return self.some_text


class WidgetButton(QtWidgets.QWidget):
    def __init__(self, label = "test"):
        super(WidgetButton, self).__init__()

        self.setMinimumHeight(40)

        #bg color
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(80,80,80))
        self.setPalette(self.p)

        #add layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(2,2,2,2)

        #label
        self.label = QtWidgets.QLabel(label)
        self.main_layout.addWidget(self.label)
    
    def set_label(self, text):
        self.label.setText(text)
    
    def mouseMoveEvent(self, event):
        if event.buttons() != QtCore.Qt.LeftButton:
            return
        
        mimeData = WidgetButtonMimeData()
        mimeData.set_text(self.label.text())
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
        # QtCore.Qt.LinkAction - move the data from the source to target
        # QtCore.Qt.MoveAction - create a link from the source to the target