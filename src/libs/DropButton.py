from PySide6.QtWidgets import QPushButton


class DropButton(QPushButton):
    """ a Button able to drop something on it """
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        print('drop event')
        self.setText(event.mimeData().text())
