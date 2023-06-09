        # slider
        self.slider_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.slider_layout)
        self.slider_xOffset = QtWidgets.QSlider()
        self.slider_xOffset.setOrientation(QtCore.Qt.Horizontal)
        self.slider_layout.addWidget(self.slider_xOffset)
        
        self.slider_xOffset.setMinimum(0)
        self.slider_xOffset.setMaximum(10)
        self.slider_xOffset.setMinimumWidth((self.width()/3)*2)
        self.slider_xOffset.valueChanged.connect(self.on_slider_value_changed)

        # slider value text
        self.ledit_slider_value = QtWidgets.QLineEdit("0")
        self.slider_layout.addWidget(self.ledit_slider_value)


        def on_slider_value_changed(self):
            self.xOffset = self.slider_xOffset.value()
            self.ledit_slider_value.setText(str(self.xOffset))
            # print(self.xOffset)