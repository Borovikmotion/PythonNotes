        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.buttons_layout)
        self.button_OK = QtWidgets.QPushButton("Create")
        self.buttons_layout.addWidget(self.button_OK)

        def on_button_ok_clicked(self):
            print("OK")
            self.close()