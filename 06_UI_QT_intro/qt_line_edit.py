
        # line edit text
        self.ledit_object_name = QtWidgets.QLineEdit("Object_Name")
        self.main_layout.addWidget(self.ledit_object_name)
        self.ledit_object_name.textChanged.connect(self.on_object_name_changed)


        def on_object_name_changed(self):
            self.objectName = self.ledit_object_name.displayText()
            # print(self.ObjectName)