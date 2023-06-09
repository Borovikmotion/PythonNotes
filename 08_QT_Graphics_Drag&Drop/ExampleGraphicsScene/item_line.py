import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore


class Line(QtWidgets.QGraphicsLineItem):
    def __init__(self, circleA=None, circleB=None):
        super(Line, self).__init__()

        self.pen = QtGui.QPen(QtGui.QColor(104, 212, 232, 200), 5, QtCore.Qt.SolidLine)

        self.setPen(self.pen)

        self.circleA = circleA
        self.circleB = circleB

        CirclePosA = self.circleA.scenePos()
        CirclePosB = self.circleB.scenePos()

        self.setLine(CirclePosA.x(), CirclePosA.y(), CirclePosB.x(), CirclePosB.y())
    
    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super(Line, self).paint(painter, QStyleOptionGraphicsItem, widget)
        CirclePosA = self.circleA.scenePos()
        CirclePosB = self.circleB.scenePos()
        self.setLine(CirclePosA.x(), CirclePosA.y(), CirclePosB.x(), CirclePosB.y())