        # radiobuttons
        self.radio_buttons_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.radio_buttons_layout)

        self.buttonGroup1 = QtWidgets.QButtonGroup()
        self.rbutton_Sphere = QtWidgets.QRadioButton("Sphere")
        self.rbutton_Cube = QtWidgets.QRadioButton("Cube")
        self.rbutton_Cone = QtWidgets.QRadioButton("Cone")

        self.radio_buttons_layout.addWidget(self.rbutton_Sphere)
        self.radio_buttons_layout.addWidget(self.rbutton_Cube)
        self.radio_buttons_layout.addWidget(self.rbutton_Cone)

        self.buttonGroup1.addButton(self.rbutton_Sphere)
        self.buttonGroup1.addButton(self.rbutton_Cube)
        self.buttonGroup1.addButton(self.rbutton_Cone)
        
        self.rbutton_Sphere.setChecked(True)
