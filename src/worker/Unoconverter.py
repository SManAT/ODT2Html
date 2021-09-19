import logging
from PyQt6.QtCore import pyqtSignal, QObject, pyqtSlot
from src.libs.CmdRunner import CmdRunner
import os
import sys
import shutil


class Unoconverter(QObject):
    """
    Worker Thread
    will use unoconv to convert ODT Files to Html
    """

    finished = pyqtSignal()
    LOPath = None

    def __init__(self, rootDir, parent=None):
        QObject.__init__(self, parent)
        self.logger = logging.getLogger('Unoconverter')
        self.rootDir = rootDir
        self.tmpDir = os.path.join(self.rootDir, "tmp")
        # be sure tmp Dir exists
        self.createDir(self.tmpDir)

    def __del__(self):
        self.wait()

    @pyqtSlot()
    def convert(self):
        if self.LOPath is None:
            self.logger.error("No Path to Libre Office is set ... exit")
            sys.exit(-1)

        print("XXX")

        self.copyODT2TempDir()

        batchPath = self.createBatchFile()
        print("batch")

        """
        worker = CmdRunner()
        worker.runCmd(batchPath)
        self.logger.info(worker.getStderr())
        self.logger.info(worker.getStdout())
        """

        self.finished.emit()

    def makeWindowsSavePath(self, path):
        """ will e.g. C:\\Program Files\\ to C:\\"Program Files"\\ """
        parts = path.split("\\")
        erg = ""
        for p in parts:
            if p.find(" ", 1) > 0:
                erg += '"%s"\\' % p
            else:
                erg += "%s\\" % p
        return erg[:-1]

    def createBatchFile(self):
        """ creates a temp Batch File """
        pypath = os.path.join(self.LOPath, "python.exe")
        pypath = self.makeWindowsSavePath(pypath)

        unopath = os.path.abspath(os.path.join(self.rootDir, "unoconv.py"))
        unopath = self.makeWindowsSavePath(unopath)

        # using copied odt file in tmp path
        cmd = "START %s %s -f html %s" % (pypath, unopath, self.tmpODTFile)
        batchPath = os.path.join(self.tmpDir, "TemporaryBatchFile.bat")
        tempBatch = open(r'%s' % batchPath, 'w')
        tempBatch.write(cmd)
        tempBatch.close()

        return batchPath

    def copyODT2TempDir(self):
        """ copy the ODT File to temp directory """
        try:
            filepath = os.path.abspath(self.filename)

            # create new target Path
            filename = os.path.basename(self.filename)
            targetPath = os.path.join(self.tmpDir, filename)

            filepath = self.makeWindowsSavePath(filepath)
            self.tmpODTFile = self.makeWindowsSavePath(targetPath)

            # copy File
            shutil.copyfile(filepath, self.tmpODTFile)
        except Exception as ex:
            self.logger.error(ex)

    def createDir(self, path):
        """ create dir if it not exists """
        if os.path.isdir(path) is False:
            os.mkdir(path)

    def setFile(self, f):
        """ which File to convert """
        self.filename = f

    def setLOPath(self, path):
        self.LOPath = path
