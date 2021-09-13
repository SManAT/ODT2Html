from PySide6.QtWidgets import QMessageBox


class Dialogs():
    """ Some Standard PyQT Dialogs """
    def __init__(self):
        pass

    def showErrorDialog(self, titel, msg, icon):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowIcon(icon)
        msgBox.setText(msg)
        msgBox.setWindowTitle(titel)
        msgBox.exec()
        return msgBox
