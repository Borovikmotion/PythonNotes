import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from item_circle import Circle
from item_line import Line

class Scene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(Scene, self).__init__()

        self.selected_object = []

        self.item_1 = Circle()
        self.item_1.selected_object = "pSphere1"
        self.addItem(self.item_1)

        self.item_2 = Circle()
        self.item_2.selected_object = "pSphere2"
        self.addItem(self.item_2)
        self.item_2.moveBy(100,0)

        # self.group = QtWidgets.QGraphicsItemGroup()
        # self.group.addToGroup(self.self.item_1)
        # self.group.addToGroup(self.self.item_2)

        self.item_line = Line(circleA=self.item_1, circleB=self.item_2)
        self.addItem(self.item_line)
    
    def define_selection(self):
        for i in self.selected_object:
            i.set_unselected()
        
        self.selected_object = self.selectedItems()

        for i in self.selected_object:
            i.set_selected()
    
            cmds.select(i.selected_object)

    def mouseMoveEvent(self, event):
        super(Scene, self).mouseMoveEvent(event)
        pos = event.scenePos()

        for i in self.selected_object:
            maya_object = i.selected_object

            if not cmds.objExists(maya_object):
                continue
            
            coord_x = pos.x() / float(10)
            coord_y = pos.y() / float(10)

            cmds.xform(maya_object, t = [coord_x, coord_y, 0], a=1)


    # def mousePressEvent(self, even):
    #     click_pos = event.scenePos()
    #     item_at = self.itemAt(click_pos)


# QGraphicsItemGroup