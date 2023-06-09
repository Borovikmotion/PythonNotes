if self.scroll_layout.count(): # if layout has any children

    for i in range(self.scroll_layout.count()): #[0,1,2,3,4]

    item = self.scroll_layout.itemAt(i)
    widget = item.widget()

    if widget:
        widget.deleteLater()