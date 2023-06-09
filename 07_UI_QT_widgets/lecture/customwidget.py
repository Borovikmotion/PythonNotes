from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds 
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin



class CustomUserWidget(QtWidgets.QWidget):

    mySignal = QtCore.Signal(str)

    def __init__(self, objectPath = None):

        super(CustomUserWidget, self).__init__()

        self.objectPath = objectPath
        self.objectName = self.objectPath.split("|")[-1]

        self.setObjectName(self.objectName)


        # Context menu

        self.popMenu = QtWidgets.QMenu(self)

        self.popMenuAdd = QtWidgets.QAction('Add object', self)
        self.popMenu.addAction(self.popMenuAdd)
        self.popMenuAdd.triggered.connect(self.testA)

        self.popMenuDel = QtWidgets.QAction('Delete object', self)
        self.popMenu.addAction(self.popMenuDel)
        self.popMenuDel.triggered.connect(self.testB)    

        # attributes
        self.setMouseTracking(True)  
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)


        #---------------

        self.setupUI()


    def onContextMenu(self, point):

        self.popMenu.exec_(self.mapToGlobal(point))


    def testA(self):
        print "TEST A"

    def testB(self):
        print "TEST B"

    def setupUI(self):

        self.setFixedSize(375, 40)

        # Background Color
        self.setAutoFillBackground(1)

        color = 85
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color)) # 0 - 255
        self.setPalette(self.p)

        # main layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.mainLayout.setSpacing(20)
        self.setLayout(self.mainLayout)

        # checkbox
        self.checkbox = QtWidgets.QCheckBox()
        self.mainLayout.addWidget(self.checkbox)

        # label
        self.label = QtWidgets.QLabel(self.objectName)
        self.label.setFixedSize(285, 30)
        self.mainLayout.addWidget(self.label)

        # button

        self.btn = QtWidgets.QPushButton("Fix")
        self.btn.setObjectName("MySuperButton")
        self.button2Style = """
            QPushButton#MySuperButton{
                background-color: rgb(109,113,168);
                border-radius: 10px;
                min-width: 30px;
                min-height: 30px;
                font-weight: 900;

 
            }
            QPushButton#MySuperButton:hover {
                background-color: rgb(255,133,198);
                min-width: 30px;
                min-height: 30px;  
            }
            """
        self.btn.setStyleSheet(self.button2Style)
        self.btn.clicked.connect(self.sendSignal)
        self.mainLayout.addWidget(self.btn)


    def sendSignal(self):
            
        self.mySignal.emit(self.objectName)

        cmds.xform(self.objectPath, t=[0,0,0], ro=[0,0,0])

        self.deleteLater()





    def enterEvent(self, e):
        color = 95

        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        
        super(CustomUserWidget, self).enterEvent(e)
        
        
    def leaveEvent(self, e):
        color = 85

        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        self.setCursor(QtCore.Qt.ArrowCursor)
        
        super(CustomUserWidget, self).leaveEvent(e)


    def mousePressEvent(self, e):

        color = 125

        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        self.setCursor(QtCore.Qt.PointingHandCursor)


        super(CustomUserWidget, self).mousePressEvent(e)



    def mouseReleaseEvent(self, event):

        color = 95

        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        self.setCursor(QtCore.Qt.PointingHandCursor)



        if event.button() == QtCore.Qt.LeftButton:
            cmds.select(self.objectPath)

        # elif event.button() == QtCore.Qt.RightButton:

        #     print("Right Button Clicked")



        super(CustomUserWidget, self).mouseReleaseEvent(event)







class SceneChecker(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):

    def __init__(self):

        super(SceneChecker,self).__init__()

        self.setObjectName("mySceneChecker")

        self.setupUI()

    def setupUI(self):

        #properties
        self.setMinimumWidth(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(500)
        self.setWindowTitle("My Scene Check")
        self.setDockableParameters(widht = 400)
        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainWidget.setLayout(self.mainLayout)
        self.setLayout( self.mainLayout)


        # scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(390)
        self.scrollArea.setMaximumWidth(390)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,0,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)

        self.mainLayout.addWidget(self.scrollArea) #add to main layout


        # selection = cmds.listRelatives(cmds.ls(type = "mesh", l=1), p=1, f=1)

        # for i in selection:

        #     btn = CustomUserWidget(objectPath = i)
        #     self.scroll_layout.addWidget(btn)


        # Separator
        self.separatorLine1 = QtWidgets.QFrame()
        self.separatorLine1.setFrameShape( QtWidgets.QFrame.HLine )
        self.mainLayout.addWidget(self.separatorLine1)

        # Info
        self.info = QtWidgets.QLabel("Info:")

        self.mainLayout.addWidget(self.info)

        # buttons
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnFix = QtWidgets.QPushButton("Fix")
        self.btnFix.clicked.connect(self.btnFixClicked)
        self.btnCheck = QtWidgets.QPushButton("Check")
        self.btnCheck.clicked.connect(self.btnCkeckClicked)
        self.btnLayout.addWidget(self.btnFix)
        self.btnLayout.addWidget(self.btnCheck)


        self.mainLayout.addLayout( self.btnLayout)


    def fixObject(self, i = None):

        cmds.xform(i, t= [0,0,0], ro=[0,0,0])


    def btnFixClicked(self):
        

        widgetlist = []
        widgetListFull = []

        if self.scroll_layout.count(): # if layout has any children

          for i in range(self.scroll_layout.count()): #[0,1,2,3,4]

            item = self.scroll_layout.itemAt(i)
            widget = item.widget()

            widgetListFull.append(widget)

            if widget.checkbox.isChecked():
                widgetlist.append(widget)


        if widgetlist:
            for i in widgetlist:

                obj = i.objectPath
                self.fixObject(obj)
                i.deleteLater()

        else:
            for i in widgetListFull:
                obj = i.objectPath
                self.fixObject(obj)
                i.deleteLater()


    def changeInfo(self, text):

        self.info.setText( "Info: {} has been fixed".format(text))








    def checkNonZeroObjects(self):

        objects = cmds.listRelatives(cmds.ls(type = "mesh", l=1), p=1, f=1)

        result = []

        for i in objects:

            rotation = cmds.xform(i, q=1, ws=1, ro=1) 

            translation = cmds.xform(i, q=1, ws=1, t=1) 

            if any(rotation) or any(translation):

                result.append(i)


        return result




    def btnCkeckClicked(self):
        
        # DELETE ALL
        if self.scroll_layout.count(): # if layout has any children

          for i in range(self.scroll_layout.count()): #[0,1,2,3,4]

            item = self.scroll_layout.itemAt(i)
            widget = item.widget()

            if widget:
              widget.deleteLater()


        badObjects = self.checkNonZeroObjects()

        # Add Bad objects
        for i in badObjects:

            btn = CustomUserWidget(objectPath = i)
            btn.mySignal.connect(self.changeInfo)
            self.scroll_layout.addWidget(btn)














def main():
    
    if cmds.workspaceControl('mySceneCheckerWorkspaceControl', exists=True):
        cmds.deleteUI('mySceneCheckerWorkspaceControl', control = True)
        cmds.workspaceControlState('mySceneCheckerWorkspaceControl', remove=1)
        
    myUI = SceneChecker()
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl('mySceneCheckerWorkspaceControl',
                            label = 'SceneChecker',
                            edit = 1,
                            tabToControl = ['AttributeEditor', -1],
                            widthProperty = 'fixed',
                            initialWidth = 400)



    
    
main()
