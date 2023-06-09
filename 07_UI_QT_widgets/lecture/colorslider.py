import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui


class ColorBar(QtWidgets.QWidget):

    def __init__(self):
        super(ColorBar, self).__init__()

        self.setFixedSize(10,20)

        # Set Background Color = Green
        self.setAutoFillBackground(True)

        # fill the background
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(0,255,0))
        self.setPalette(self.p)

    def setColor(self, rgb = [0,0,0]):
        R = rgb[0]
        G = rgb[1]
        B = rgb[2]
        self.p.setColor(self.backgroundRole(), QtGui.QColor(R,G,B))
        self.setPalette(self.p)


class ColorSlider(QtWidgets.QWidget):

    mySignal = QtCore.Signal(int)

    def __init__(self):
        super(ColorSlider, self).__init__()

        self.setMinimumSize(200,20)

        # set background color 
        # self.setAutoFillBackground(True) # We need this parameter set True to be able to change background

        # fill the background
        # self.p = self.palette()
        # self.p.setColor(self.backgroundRole(), QtGui.QColor(30,30,30)) # RGB(30,30,30)
        # self.setPalette(self.p)

        self.createUI()

    def createUI(self):

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout( self.mainLayout )

        # add color widget
        self.colorWidget = ColorBar()
        self.mainLayout.addWidget( self.colorWidget )

        # add horizontal slider
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(self.changeTextField)
        self.mainLayout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.setColorBar)

        # add text field
        self.textField = QtWidgets.QSpinBox()
        self.textField.setFixedSize(50,20)
        self.textField.setRange( self.slider.minimum(), self.slider.maximum() )
        self.textField.valueChanged.connect(self.changeSlider)
        self.mainLayout.addWidget(self.textField)

    def setColorBar(self, value):

        colorMinMax = 255

        colorMinMaxPercent = colorMinMax/100.0 # 1% of our color

        sliderMinMax = self.slider.maximum() - self.slider.minimum() # 15 - 5 = 10
        sliderMin = self.slider.minimum()

        sliderMinMaxPercent = sliderMinMax/100.0

        # as slider min can be any number (not only 0)
        # What percentage slider has been moved ?

        sliderValue = value # int

        # this is how far we moved slider in percentage
        sliderPercent = (sliderValue - sliderMin) / sliderMinMaxPercent

        # calculate color

        colorR = 0 + colorMinMaxPercent * sliderPercent
        colorG = colorMinMax - colorMinMaxPercent * sliderPercent

        self.colorWidget.setColor(rgb = [colorR, colorG, 0] )

        # send signal to the outer code
        self.mySignal.emit(value)




    def changeTextField(self, value):

        self.textField.setValue( value )

    def changeSlider(self, value):

        self.slider.setValue(value)
        


class MyDialog(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super(MyDialog, self).__init__() 
        
        self.setObjectName('myTestWindow')
        
        self.setWindowTitle('My Test UI')
        
        self.setMinimumSize(300, 100) # Width , Height in pixels

        self.createUI()

    def createUI(self):

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout( self.mainLayout )


        sldr1 = ColorSlider()
        sldr1.mySignal.connect(self.printSliderValue)
        self.mainLayout.addWidget( sldr1 )

        sldr2 = ColorSlider()
        self.mainLayout.addWidget( sldr2 )

    def printSliderValue(self, value):

        print value

        


if cmds.window('myTestWindow', q=1, exists=1):
    cmds.deleteUI('myTestWindow')
    
if cmds.windowPref('myTestWindow', exists = 1):
    cmds.windowPref('myTestWindow', remove = 1)
        
        
myUI = MyDialog()
myUI.show()