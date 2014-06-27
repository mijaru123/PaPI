# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quitter.ui'
#
# Created: Fri Jun 27 14:44:59 2014
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
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 360, 671, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vertLay = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vertLay.setContentsMargins(0, 0, 0, 0)
        self.vertLay.setObjectName("vertLay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.showLicense.setText(QtGui.QApplication.translate("MainWindow", "ShowLicense", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.delPlot.setText(QtGui.QApplication.translate("MainWindow", "delPlot", None, QtGui.QApplication.UnicodeUTF8))
        self.addPlot.setText(QtGui.QApplication.translate("MainWindow", "addPlot", None, QtGui.QApplication.UnicodeUTF8))

