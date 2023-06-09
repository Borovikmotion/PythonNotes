from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin


class MyMIME(QtCore.QMimeData):
  """
  This class holds all the info that we need to transfer with a widget Drag
  """

  def __init__(self):
      super(MyMIME,  self).__init__()
      self.someText = "none"
      self.fromWidget = None

  def setText(self, text = None):
      self.someText = text

  def getText(self):
      return self.someText


class ButtonWidget(QtWidgets.QWidget):
  """
  The button that we gonna Click | Drag | Drop
  When we click - our cursor carries MimeData that we need to feed with some custom info
  """


  def __init__(self, parent = None, label = "TEST"):

      super(ButtonWidget, self).__init__()

      self.setFixedSize(200, 40)

      # Background Color
      self.setAutoFillBackground(True)
      color = 80
      self.p = self.palette()
      self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
      self.setPalette(self.p)

      # main layout
      self.mainLayout = QtWidgets.QHBoxLayout()
      self.setLayout(self.mainLayout)

      # label
      self.label = QtWidgets.QLabel(label)
      self.mainLayout.addWidget(self.label)

  def addLabel(self, t = ""):
      self.label.setText(t) # for Drag and Drop


  def mousePressEvent(self, event):

      if event.buttons() != QtCore.Qt.LeftButton:
          return

      mimeData = MyMIME() #create mimeData class | nothing too much happes here

      # Feed mimeData
      mimeData.setText(self.label.text())

      #Create Ghosty image behind the moving mouse cursor
      self.pixmap = self.grab()
      painter = QtGui.QPainter(self.pixmap)
      painter.setCompositionMode(painter.CompositionMode_DestinationIn)
      painter.fillRect(self.pixmap.rect(), QtGui.QColor(80, 80, 80, 127))
      painter.end()

      #Here we create the actual Drag class that does Dragging
      drag = QtGui.QDrag(self) # create Drag class to copy information between applications
      drag.setMimeData(mimeData) # data to be sent with Drag
      drag.setPixmap(self.pixmap) # set widget image
      drag.setHotSpot(event.pos()) #
      drag.exec_(QtCore.Qt.LinkAction | QtCore.Qt.MoveAction) # starts the Drag and Drop operation

      """
      Qt::MoveAction          0x2  (2)    Move the data from the source to the target.
      Qt::LinkAction          0x4  (4)    Create a link from the source to the target.
      """


class FieldWidget(QtWidgets.QWidget):

  def __init__(self, parent = None):

      super(FieldWidget, self).__init__()

      self.buttonsList = []

      # Some settings
      self.setFixedSize(240, 490)
      self.setAcceptDrops(True) # this is important - we can now drop widgets here

      # Add background color
      self.setAutoFillBackground(True)
      color = 40
      self.p = self.palette()
      self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
      self.setPalette(self.p)

      # Let's add main layout
      self.mainLayout = QtWidgets.QVBoxLayout()
      self.setLayout(self.mainLayout)

      #* scroll area
      self.scrollArea = QtWidgets.QScrollArea()
      self.scrollArea.setMinimumHeight(200)
      self.scrollArea.setWidgetResizable(True)
      self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
      self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
      self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
      self.scroll_area_widget = QtWidgets.QWidget()
      self.scrollArea.setWidget(self.scroll_area_widget)
      self.scroll_layout = QtWidgets.QGridLayout()
      self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
      self.scroll_layout.setContentsMargins(0,0,2,0)
      self.scroll_layout.setSpacing(5)
      self.scroll_area_widget.setLayout(self.scroll_layout) #* -> scroll_layout
      self.mainLayout.addWidget(self.scrollArea)


  def feedButtons(self):

      # We will create Drag&Drop buttons here
      
      for i in range(5):
          button = ButtonWidget()
          button.addLabel(t=  "Button {}".format(i) )
          self.buttonsList.append(button)
          self.scroll_layout.addWidget(button)


  '''DRAG & DROP'''
  def dragEnterEvent(self, e):
      # what happens when we start dragging our mouse
      # e - is QDragEnterEvent
      e.acceptProposedAction() # accept dragEnter action


  def dropEvent(self, e):

      # pos = e.scenePos() #get position where we released mouse button
      mimeData = e.mimeData() #get mime data from the cursor
      mimeText  = mimeData.getText()
      # mimeFrom = mimeData.getFrom()
      # print e.source, self
      e.source().deleteLater()


      # recreate button with Mime text and other data
      button = ButtonWidget()
      button.addLabel( t  = mimeText)
      self.scroll_layout.addWidget(button)


  def dragMoveEvent(self, e):
      e.acceptProposedAction()


        
class MyDDWnd(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self):

        super(MyDDWnd, self).__init__()

        self.setObjectName("myDragDropWnd_Ptr")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFixedSize(500,500)

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setSpacing(1)
        self.mainLayout.setContentsMargins(5,5,5,5)
        self.setLayout(self.mainLayout)
        
        self.w_1 = FieldWidget()
        self.w_1.feedButtons() # add Drag&Drop buttons to the first field

        self.w_2 = FieldWidget()

        self.mainLayout.addWidget(self.w_1)
        self.mainLayout.addWidget(self.w_2)



def main():

    if cmds.window("myDragDropWnd_Ptr", exists = 1):
        cmds.deleteUI("myDragDropWnd_Ptr")

    if cmds.windowPref("myDragDropWnd_Ptr", exists = 1):
        cmds.windowPref("myDragDropWnd_Ptr", remove = 1)

    myDragDropWnd = MyDDWnd()
    myDragDropWnd.show()

main()