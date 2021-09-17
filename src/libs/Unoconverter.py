import logging
from PyQt6.QtCore import QThread, pyqtSignal


class Unoconverter(QThread):
    """ will use unoconv to convert ODT Files to Html """

    finished = pyqtSignal()

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.logger = logging.getLogger('Unoconverter')

    def run(self):
        # setting the done event
        self.finished.emit()

    def setFile(self, f):
        """ which File to convert """
        self.filename = f


    # C:\"Program Files"\LibreOffice\program\python.exe C:\Users\Stefan\Documents\GitHub\ODT2Html\unoconv.py -f pdf C:\Users\Stefan\Documents\GitHub\ODT2Html\TestFile.odt