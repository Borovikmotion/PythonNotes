import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore


class View(QtWidgets.QGraphicsView):

    """ viewport """

    def __init__(self):
        super(View, self).__init__()

        #viewport size
        self.setSceneRect(-5000, -5000, 10000, 10000)

        #hide scrollbars
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        #hide blue border
        self.setStyleSheet("border: no-border")

        #enable rectangle selection and mode which allows to select obecjt by only it's part
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)

        #antialiasing 
        self.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)

        #make size of the viewport follow the size of a scene
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)


