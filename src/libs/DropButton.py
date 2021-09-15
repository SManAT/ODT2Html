from PySide6.QtWidgets import QPushButton
import os


class DropButton(QPushButton):
    acceptedExtensions = ["odt"]

    """ a Button able to drop something on it """
    def __init__(self, title, parent):
        super().__init__(title, parent.ui.dropWidget)
        self.setAcceptDrops(True)
        self.parent = parent

    def dragEnterEvent(self, event):
        # see https://doc.qt.io/qt-5/qmimedata.html
        if self.handleExtension(event.mimeData().text()):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        print("File dropped: %s" % event.mimeData().text())
        self.filename = event.mimeData().text()
        # callback
        self.parent.convert(self.filename)

    def handleExtension(self, filename):
        """ only accept some extensions """
        extension = os.path.splitext(filename)[1][1:].strip().lower()
        if extension in self.acceptedExtensions:
            return True
        else:
            return False
