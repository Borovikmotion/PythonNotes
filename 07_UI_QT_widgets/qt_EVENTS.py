

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.set_background(85, 85, 85)
            print("clicked with event")

    def enterEvent(self, event):
        # print("entered")
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.set_background(75, 75, 75)
    
    def leaveEvent(self, event):
        # print("left")
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.set_background(50, 50, 50)

    # !!! 
    def mouseReleaseEvent(self, event):
        self.set_background(75, 75, 75)
        # state = self.checkbox.isChecked()
        # self.checkbox.setChecked(not state)