# _______MORE________
class MyCheckbox(QtWidgets.QCheckBox):
    def __init__(self, *args, **kwargs):
        super(MyCheckbox, self).__init__(*args, **kwargs)

    # when u replace events - checkbox is no longer working:
    # def mouseReleaseEvent(self, event):
    #     print("pressed")
    
    # def mousePressEvent(self, event):
    #     print("pressed")

    # and how to fix that:
    def mouseReleaseEvent(self, event):
        print("pressed")

        super(MyCheckBox, self).mouseReleaseEvent(event)
    
    def mousePressEvent(self, event):
        print("pressed")
        
        super(MyCheckBox, self).mousePressEvent(event)

