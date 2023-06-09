
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        # #checkbox
        self.checkbox = QtWidgets.QCheckBox("MyCheckbox")
        self.checkbox.toggled.connect(self.on_checkbox_toggled)
        self.mainLayout.addWidget(self.checkbox)
    
    def on_checkbox_toggled(self, state):
        checkbox_state = self.checkbox.isChecked()
        print("haha", checkbox_state)