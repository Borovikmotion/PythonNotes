import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore



class MyDialog(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super(MyDialog, self).__init__() # Инициализация всех свойств и настроек класса QDialog
        
        # задать уникальный идентификатор окна
        self.setObjectName('myTestWindow')
        
        # установить видимое название окна
        self.setWindowTitle('My Test UI')
        
        # указать минимальный размер окна (меньше окно сделать нельзя)
        self.setMinimumSize(300, 100) # Width , Height in pixels
        
        # create main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout) # установить в наш QDialog главный layout
        
        # Создадим отдельный горизонтальный layout для кнопок
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSpacing(2)
        self.buttonsLayout.setContentsMargins(0,0,0,0) # Left Top Right Bottom
                
        # Создадим сами кнопки
        self.button_Create = QtWidgets.QPushButton('Create')
        self.button_Apply = QtWidgets.QPushButton('Apply')
        self.button_Close = QtWidgets.QPushButton('Close')
        
        self.button_Create.clicked.connect( self.create )
        self.button_Apply.clicked.connect( self.apply )
        self.button_Close.clicked.connect( self.close )
        
        # Поместим кнопки в соответствующий layout
        self.buttonsLayout.addWidget( self.button_Create )
        self.buttonsLayout.addWidget( self.button_Apply )
        self.buttonsLayout.addWidget( self.button_Close )
        
        # Не забываем поместить наш доп layout в основной layout
        self.mainLayout.addLayout(self.buttonsLayout)
        
        #Создаем виджет - группу для радио-кнопок
        self.radio_group = QtWidgets.QGroupBox()
        self.radio_group.setMaximumHeight(50) # установим группе высоту - 50px

        # Поскольку мы поместим внутрь виджета - другие виджеты 
        # то мы должны создать и поместить в него сначала layout ( скатерть !)
        self.radio_groupLayout = QtWidgets.QHBoxLayout()
        
        # Создаем радио-кнопки
        self.radio_Sphere = QtWidgets.QRadioButton('Sphere')
        self.radio_Cube = QtWidgets.QRadioButton('Cube')
        self.radio_Cone = QtWidgets.QRadioButton('Cone')
        
        # Помещаем их в соответсвующий layout
        self.radio_groupLayout.addWidget(self.radio_Sphere)
        self.radio_Sphere.setChecked( True ) 
        self.radio_groupLayout.addWidget(self.radio_Cube)
        self.radio_groupLayout.addWidget(self.radio_Cone)
        
        # Устанавливаем в группу - layout
        self.radio_group.setLayout( self.radio_groupLayout)
        
        # Саму же группу добавляем в главный layout
        self.mainLayout.addWidget( self.radio_group )
        
        # старье
        self.mainLayout.addLayout(self.buttonsLayout)
        
    def create(self):
        # Creates a polygonal object and closes UI
        
        # check which radio button is selected
        if self.radio_Sphere.isChecked():
            cmds.polySphere()
        elif self.radio_Cube.isChecked():
            cmds.polyCube()
        else:
            cmds.polyCone()
        
        # close our UI
        self.close()
        
    def apply(self):
        # Creates an object and keeps UI opened
        
        # check which radio button is selected
        if self.radio_Sphere.isChecked():
            cmds.polySphere()
        elif self.radio_Cube.isChecked():
            cmds.polyCube()
        else:
            cmds.polyCone()
        

# проверить если наш UI уже создан

if cmds.window('myTestWindow', q=1, exists=1):
    cmds.deleteUI('myTestWindow')
    
# проверить если Maya хранит в себе настройки отображения нашего UI
if cmds.windowPref('myTestWindow', exists = 1):
    cmds.windowPref('myTestWindow', remove = 1)
        
        
myUI = MyDialog()
myUI.show()