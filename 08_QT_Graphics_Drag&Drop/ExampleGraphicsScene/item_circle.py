import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore


class Circle(QtWidgets.QGraphicsItem):
    def __init__(self):
        super(Circle, self).__init__()

        self.selected_object = None

        self.brush = QtGui.QBrush(QtGui.QColor(244, 206, 66, 255))
        self.pen = QtGui.QPen(QtGui.QColor(242, 86, 51,200), 2, QtCore.Qt.SolidLine)

        #make object movable and selectable
        self.setFlags( QtWidgets.QGraphicsItem.ItemIsMovable | QtWidgets.QGraphicsItem.ItemIsSelectable)


    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(-30, -30, 60, 60)

    def boundingRect(self):
        return QtCore.QRectF(-30, -30, 60, 60)

    # SELECTION THING
    def set_selected(self):
        self.pen = QtGui.QPen(QtGui.QColor(87, 255, 140,200), 3, QtCore.Qt.SolidLine)
        self.update()

    def set_unselected(self):
        self.pen = QtGui.QPen(QtGui.QColor(242, 86, 51,200), 2, QtCore.Qt.SolidLine)
        self.update()