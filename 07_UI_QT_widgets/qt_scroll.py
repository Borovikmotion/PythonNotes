    def setup_ui(self):
        self.setWindowTitle("My Custom UI")
        self.setObjectName("MyCustomWidgetUIId")
        self.setMinimumSize(300, 500)
        self.resize(300, 500)

        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(5,5,1,5)
        self.main_layout.setSpacing(5)
        # self.setLayout(self.main_layout)
        self.mainWidget.setLayout(self.main_layout)

        # scroll area -------------------------------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(290)
        # self.scrollArea.setMaximumWidth(390)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)

        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,5,0)
        self.scroll_layout.setSpacing(5) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)

        self.main_layout.addWidget(self.scrollArea) #add to main layout