from PySide2 import QtWidgets, QtGui, QtCore

class MyCheckBox(QtWidgets.QCheckBox):
    def __init__(self):
        super(MyCheckBox, self).__init__()
    
        self.background_color = "#777"
        self.circle_color = "#eee"
        self.active_color = "#6db9ff"

        width = 40
        height = 20

        self.setFixedSize(width, height)

        # self.update()

    #makes logic work if we click at any place at our widget
    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def paintEvent(self, event):
        
        # DRAWING 
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing)

        #PEN EXAMPLES

        # # dot line 
        # brush = QtGui.QColor(255, 255, 255, 255)
        # pen = QtGui.QPen(brush, 5, QtCore.Qt.DashDotLine)
        # p.setPen(pen)

        # # how to draw a circle without stroke
        # p.setPen(QtCore.Qt.NoPen)

        # brush = QtGui.QBrush(QtGui.QColor(102, 212, 242, 255))
        # p.setBrush(brush)
        # p.drawEllipse(5,5,80,80)

        # -------------- CHECKBOX ---------------------

        if not self.isChecked():
            #gray background
            p.setPen(QtCore.Qt.NoPen)
            p.setBrush(QtGui.QColor(self.background_color))
            p.drawRoundedRect(0,0, self.width(), self.height(), self.height()/2, self.height()/2)

            #circle
            p.setBrush(QtGui.QColor(self.circle_color))
            p.drawEllipse(2,2, self.height()-4, self.height()-4)

        else:
            #blue background
            p.setPen(QtCore.Qt.NoPen)
            p.setBrush(QtGui.QColor(self.background_color))
            p.drawRoundedRect(0,0, self.width(), self.height(), self.height()/2, self.height()/2)

            #circle
            p.setBrush(QtGui.QColor(self.active_color))
            p.drawEllipse(self.width() - 18, 2, self.height()-4, self.height()-4)


        #END OF DRAWING !!
        p.end()


        # # if u want an original thing 
        # super(MyCheckBox, self).paintEvent(event)