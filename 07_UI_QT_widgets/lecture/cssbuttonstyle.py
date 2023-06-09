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