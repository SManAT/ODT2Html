import logging
from PyQt6.QtCore import QThread, pyqtSignal
from src.libs.CmdRunner import CmdRunner
import os
import sys
import re


class Unoconverter(QThread):
    """ will use unoconv to convert ODT Files to Html """

    finished = pyqtSignal()
    LOPath = None

    def __init__(self, rootDir, parent=None):
        QThread.__init__(self, parent)
        self.logger = logging.getLogger('Unoconverter')
        self.rootDir = rootDir

    def run(self):
        if self.LOPath is None:
            self.logger.error("No Path to Libre Office is set ... exit")
            sys.exit(-1)

        batchPath = self.createBatchFile()
        
        
        worker = CmdRunner()
        worker.runCmd(batchPath)
        self.logger.info(worker.getStderr())
        self.logger.info(worker.getStdout())

        self.finished.emit()

    def makeWindowsSavePath(self, path):
        """ will e.g. C:\Program Files\ to C:\"Program Files"\ """
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

        filepath = os.path.abspath(self.filename)
        filepath = self.makeWindowsSavePath(filepath)

        cmd = "START %s %s -f html %s" % (pypath, unopath, filepath)
        batchPath = os.path.join(self.rootDir, "tmp", "TemporaryBatchFile.bat")
        tempBatch = open(r'%s' % batchPath, 'w')
        tempBatch.write(cmd)
        tempBatch.close()

        return batchPath


    def setFile(self, f):
        """ which File to convert """
        self.filename = f
        
    def setLOPath(self, path):
        self.LOPath = path


    