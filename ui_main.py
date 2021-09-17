# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout = QVBoxLayout(self.tab1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.dropWidget = QWidget(self.tab1)
        self.dropWidget.setObjectName(u"dropWidget")
        self.dropLayout = QHBoxLayout(self.dropWidget)
        self.dropLayout.setObjectName(u"dropLayout")
        self.dropLayout.setContentsMargins(40, -1, 40, -1)
        self.convertBtn = QPushButton(self.dropWidget)
        self.convertBtn.setObjectName(u"convertBtn")
        self.convertBtn.setMinimumSize(QSize(0, 200))
        self.convertBtn.setMaximumSize(QSize(16777215, 200))
        self.convertBtn.setStyleSheet(u"background-color: #bfffbf;\n"
"font-size: 18pt;\n"
"border: 1px solid #aaaaaa;")
        self.convertBtn.setFlat(False)

        self.dropLayout.addWidget(self.convertBtn)


        self.verticalLayout.addWidget(self.dropWidget)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1, Qt.AlignTop)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"border-top: 1px #a0a0a0 solid;")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bitte eine *.odt Datei angeben. <br/>Diese Datei wird im Anschluss</span></p><p><span style=\" font-size:12pt;\">1. Nach Html konvertiert.<br/>2. F\u00fcr eine Webseite mit passendem CSS ausgestattet.</span></p><p><span style=\" font-size:12pt;\">Im Anschluss kann man den Html Code in einer Webseite mit Html Editoren verwenden.</span></p></body></html>", None))
        self.convertBtn.setText(QCoreApplication.translate("MainWindow", u"Dummy - Datei hier ablegen oder klicken", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"ODT Datei", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

