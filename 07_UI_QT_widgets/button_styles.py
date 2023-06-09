# styles
button1Style = """
    QPushButton#MyCustomButtonWidgetId{
        background-color: rgb(246,93,205);
        border-radius: 8px;
        min-width: 30px;
        min-height: 25px;
        font-weight: 900;

    }
    QPushButton#MMyCustomButtonWidgetId:hover {
        background-color: rgb(255,255,255);
        min-width: 30px;
        min-height: 25px;  
    }
    """

# styles
button2Style = """
    QPushButton#MyCustomButtonWidgetId{
        background-color: rgb(109,113,168);
        border-radius: 8px;
        min-width: 30px;
        min-height: 25px;
        font-weight: 900;

    }
    QPushButton#MMyCustomButtonWidgetId:hover {
        background-color: rgb(255,133,198);
        min-width: 30px;
        min-height: 25px;  
    }
    """


# button
        self.button_ = QtWidgets.QPushButton("MyButton")
        self.button_.setObjectName("MyCustomButtonWidgetId")
        # self.button_.clicked.connect(self.on_button_clicked)
        self.button_.setStyleSheet(button1Style)
        self.main_layout.addWidget(self.button_)
