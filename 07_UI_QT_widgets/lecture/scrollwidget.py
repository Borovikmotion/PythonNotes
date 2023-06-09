# scroll area
self.scrollArea = QtWidgets.QScrollArea()
self.scrollArea.setMinimumHeight(200)
self.scrollArea.setWidgetResizable(True)
self.scrollArea.setMinimumWidth(390)
self.scrollArea.setMaximumWidth(390)
self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

self.scroll_area_widget = QtWidgets.QWidget()
self.scrollArea.setWidget(self.scroll_area_widget)

self.scroll_layout = QtWidgets.QVBoxLayout()
self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
self.scroll_layout.setContentsMargins(0,0,0,0)
self.scroll_layout.setSpacing(5) #layout
self.scroll_area_widget.setLayout(self.scroll_layout)

self.mainLayout.addWidget(self.scrollArea) #add to main layout