from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds 
import os
import json


ROOT  = str(os.path.dirname(__file__))


class MyMIME(QtCore.QMimeData):

    def __init__(self):
        super(MyMIME,  self).__init__()
        
        self.toolName = None



class ButtonWidget(QtWidgets.QWidget):
    """
    The button that we gonna Click | Drag | Drop
    When we click - our cursor carries MimeData that we need to feed with some custom info
    """

    def __init__(self, parent = None, label = "TEST"):

        super(ButtonWidget, self).__init__()

        self.setFixedSize(200, 40)

        # Background Color
        self.setAutoFillBackground(True)
        color = 80
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)

        # main layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainLayout)

        # label
        self.label = QtWidgets.QLabel(label)
        self.mainLayout.addWidget(self.label)

    def addLabel(self, t = ""):
        self.label.setText(t) # for Drag and Drop


    def mousePressEvent(self, event):


        if event.buttons() != QtCore.Qt.LeftButton:
            return


        mimeData = MyMIME() 

        # Feed mimeData
        mimeData.toolName = self.label.text()


        # Ghost Widget
        self.pixmap = self.grab()
        painter = QtGui.QPainter(self.pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(self.pixmap.rect(), QtGui.QColor(80, 80, 80, 127))
        painter.end()

        # Start Drag and Drop
        drag = QtGui.QDrag(self) 
        drag.setMimeData(mimeData) 
        drag.setPixmap(self.pixmap) 
        drag.setHotSpot(event.pos()) 
        drag.exec_(QtCore.Qt.LinkAction | QtCore.Qt.MoveAction) 



class FieldWidget(QtWidgets.QWidget):

    def __init__(self, parent = None):

        super(FieldWidget, self).__init__()

        self.buttonsList = []

        # Some settings
        # self.setFixedSize(240, 490)
        self.setMinimumWidth(240)
        self.setMinimumHeight(490)
        self.setAcceptDrops(True) # this is important - we can now drop widgets here

        # Add background color
        self.setAutoFillBackground(True)
        color = 40
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)

        # Let's add main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        #* scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        #   self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        self.scroll_layout = QtWidgets.QGridLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,2,0)
        self.scroll_layout.setSpacing(5)
        self.scroll_area_widget.setLayout(self.scroll_layout) #* -> scroll_layout
        self.mainLayout.addWidget(self.scrollArea)


    def dropEvent(self, e):


        mimeData = e.mimeData() #get mime data from the cursor
        
        label = mimeData.toolName


        self.label = ButtonWidget(label = label)

        self.scroll_layout.addWidget(self.label)


        e.source().deleteLater()


    def dragMoveEvent(self, e):
        e.acceptProposedAction()


    def dragEnterEvent(self, e):
        e.acceptProposedAction()


    def createWidget(self, label):

        btn = ButtonWidget(label = label)
        self.scroll_layout.addWidget(btn)



class OptionsUI(QtWidgets.QDialog):


    MySignal = QtCore.Signal(bool)
    
    def __init__(self, classList = []):

        super(OptionsUI, self).__init__() 


        self.classList = classList

        
        self.setObjectName('myOptionsUI')
        
        self.setWindowTitle('My Options UI')
        
        # self.setMinimumSize(400, 600) # Width , Height in pixels

        self.createUI()

        self.readJSON()



    def createUI(self):



        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout( self.mainLayout )


        # fields
        self.fieldLayout = QtWidgets.QHBoxLayout()


        self.leftField = FieldWidget()


        self.rightField = FieldWidget()


        self.fieldLayout.addWidget(self.leftField)
        self.fieldLayout.addWidget(self.rightField)

        self.mainLayout.addLayout(self.fieldLayout)


        # button save
        self.btnSave = QtWidgets.QPushButton("Save")
        self.btnSave.clicked.connect(self.saveToJson)
        self.mainLayout.addWidget(self.btnSave)


    def readJSON(self):

        json_file_path = os.path.join(ROOT, "save.json")


        json_data = []
        if os.path.isfile(json_file_path):
            with open(json_file_path, 'r') as f:
                json_data = json.load(f)


        for i in self.classList:

            if i in json_data:
                self.rightField.createWidget(label = i)
            else:
                self.leftField.createWidget(label = i)




    def saveToJson(self):


        output = []

        if self.rightField.scroll_layout.count():

            for i in range(self.rightField.scroll_layout.count()):

                item = self.rightField.scroll_layout.itemAt(i)
                widget = item.widget()

                label = widget.label.text()

                output.append(label)


        json_file_path = os.path.join(ROOT, "save.json")


        with open(json_file_path, 'w') as outfile:
            outfile.write(json.dumps(output, indent = 4, sort_keys=True))


        self.MySignal.emit(True)


        self.close()


