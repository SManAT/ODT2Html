import sys

from pathlib import Path
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from src.config.LoggerConfiguration import configure_logging
import logging
from ui_main import Ui_MainWindow
from PySide6 import QtGui, QtCore
from src.libs.ConfigTool import ConfigTool
from src.libs.Dialogs import Dialogs
import re
from src.libs.DropButton import DropButton
from PySide6.QtCore import QSize
from PyQt6.QtCore import QThread
from src.worker.Unoconverter import Unoconverter


class MainWindow(QMainWindow):
    def __init__(self, screen):
        super(MainWindow, self).__init__()
        self.logger = logging.getLogger('MainWindow')
        self.ui = Ui_MainWindow()
        self.rootDir = Path(__file__).parent
        self.configFile = os.path.join(self.rootDir, 'src', 'config', 'config.yaml')
        self.configTool = ConfigTool(self)
        self.config = self.configTool.load_yml()

        self.dialogs = Dialogs()

        # UI Stuff
        self.ui.setupUi(self)
        self.setWindowTitle("ODT2Html Converter")
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.rootDir, 'src', 'icons', 'App.ico')))
        # Drop Button, replace dummy
        self.replaceButton()

        # set Size with Screen
        geometry = screen.availableGeometry()
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

        # Connectors
        # self.visibleChanged.connect(self.showwEvent)
        self.ui.convertBtn.clicked.connect(self.openFileNameDialog)
        # icon = QtGui.QIcon(os.path.join(self.rootDir, 'src', 'icons', 'error.png'))
        # self.dialogs.showErrorDialog("Oh dear!", "Something went very wrong.\n\njhghghgi", icon)

    def replaceButton(self):
        """ replace dummy Button with DragnDrop Button """
        # remove from Layout
        self.ui.dropLayout.removeWidget(self.ui.convertBtn)
        self.ui.convertBtn.close()
        self.ui.convertBtn = DropButton("Datei hier ablegen oder klicken", self)
        self.ui.convertBtn.setMinimumSize(QSize(0, 200))
        self.ui.convertBtn.setMaximumSize(QSize(16777215, 200))
        self.ui.convertBtn.setFlat(True)
        self.ui.convertBtn.setStyleSheet(u"background-color: #bfffbf;font-size: 18pt;border: 1px solid #aaaaaa;")

        # add to Layout
        self.ui.dropLayout.addWidget(self.ui.convertBtn)
        self.ui.dropLayout.update()

    def show(self):
        QMainWindow.show(self)
        QtCore.QTimer.singleShot(500, lambda: self.checkLibreOfficePath())

    def clearMessage(self):
        """ clear the Statusbar Message """
        self.ui.statusbar.clearMessage()
        QApplication.processEvents()

    def showStatusMessage(self, msg, time=0):
        """ show a Statusmessage now """
        self.ui.statusbar.showMessage(msg, time)
        QApplication.processEvents()

    def checkLibreOfficePath(self):
        """ search for LO if its set probably """
        self.showStatusMessage("Searching for LibreOffice Path ...", 2000)

        loPath = self.config['app']['LOPath']
        # test if there is python.exe and soffice.exe
        if self.LOCheck(loPath) is True:
            self.LOPath = loPath
        else:
            self.LOPath = self.searchLO()
            # check again
            if self.LOCheck(self.LOPath) is False:
                icon = QtGui.QIcon(os.path.join(self.rootDir, 'src', 'icons', 'error.png'))
                self.dialogs.showErrorDialog("Error!", "Can't find path to LibreOffice\nPlease set it manually in config.yaml ...", icon)

        self.showStatusMessage("Found a Path to LibreOffice ...", 2000)
        # write Back to Config
        self.config['app']['LOPath'] = self.LOPath
        self.configTool.updateConfig()

    def searchLO(self):
        """ search for Libre Office """
        paths = ["C:\\Program Files", "C:\\Program Files (x86)"]
        for p in paths:
            for root, dirs, files in os.walk(p):  # noqa
                # print(root)
                result = re.search(r"(LibreOffice|OpenOffice)+", root)
                if result:
                    # found it
                    return os.path.join(root, "program")

    def LOCheck(self, path):
        """ test if there is python.exe and soffice.exe """
        f1 = os.path.join(path, "python.exe")
        f2 = os.path.join(path, "soffice.exe")
        if os.path.exists(f1) and os.path.exists(f2):
            return True
        else:
            return False

    def openFileNameDialog(self):
        """ File Open Dialog """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Select a File to convert",
                                                  "",
                                                  "Libre Office Writer (*.odt)",
                                                  options=options
                                                  )
        if fileName:
            self.convert(fileName)

    def convert(self, filename):
        """ Convert a odt File to html """
        self.logger.info("Converting File: %s" % filename)
        self.showStatusMessage("Converting %s to Html ..." % Path(filename).stem)
        # Start the Thread
        self.unoconv = Unoconverter(self.rootDir)
        self.unoconvThread = QThread()  # no parent!
        try:
            self.unoconv.setFile(filename)
            self.unoconv.setLOPath(self.LOPath)
            # Move the Worker object to the Thread object
            self.unoconv.moveToThread(self.unoconvThread)
            # entry point from Thread
            self.unoconvThread.started.connect(self.unoconv.convert)
            # connect signal
            self.unoconv.finished.connect(self.unoconvThread.quit)
            self.unoconvThread.finished.connect(self.unoconvertDone)

            self.unoconvThread.start()
        except Exception as e:
            self.logger.error(e)

    def unoconvertDone(self):
        """ will be fired when unoconv finished converting a ODT Document """
        self.clearMessage()
        self.showStatusMessage("Converting done ...")
        # switch to new Tab
        self.ui.tabWidget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    configure_logging()
    window = MainWindow(screen)
    window.show()
    sys.exit(app.exec())
