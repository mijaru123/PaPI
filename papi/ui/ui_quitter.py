# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quitter.ui'
#
# Created: Fri Jun 27 14:40:17 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 870)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 20, 491, 221))
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 128))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.showLicense = QtGui.QPushButton(self.gridLayoutWidget)
        self.showLicense.setObjectName("showLicense")
        self.gridLayout.addWidget(self.showLicense, 4, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 5, 0, 1, 1)
        self.delPlot = QtGui.QPushButton(self.gridLayoutWidget)
        self.delPlot.setObjectName("delPlot")
        self.gridLayout.addWidget(self.delPlot, 1, 0, 1, 1)
        self.addPlot = QtGui.QPushButton(self.gridLayoutWidget)
        self.addPlot.setObjectName("addPlot")
        self.gridLayout.addWidget(self.addPlot, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 290, 761, 511))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.showLicense.setText(QtGui.QApplication.translate("MainWindow", "ShowLicense", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.delPlot.setText(QtGui.QApplication.translate("MainWindow", "delPlot", None, QtGui.QApplication.UnicodeUTF8))
        self.addPlot.setText(QtGui.QApplication.translate("MainWindow", "addPlot", None, QtGui.QApplication.UnicodeUTF8))

