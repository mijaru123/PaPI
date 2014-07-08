# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui/main.ui'
#
# Created: Tue Jul  8 15:58:05 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainGUI(object):
    def setupUi(self, MainGUI):
        MainGUI.setObjectName("MainGUI")
        MainGUI.resize(1084, 918)
        self.centralwidget = QtGui.QWidget(MainGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scopeManagerButton = QtGui.QPushButton(self.centralwidget)
        self.scopeManagerButton.setObjectName("scopeManagerButton")
        self.horizontalLayout.addWidget(self.scopeManagerButton)
        self.parameterManagerButton = QtGui.QPushButton(self.centralwidget)
        self.parameterManagerButton.setObjectName("parameterManagerButton")
        self.horizontalLayout.addWidget(self.parameterManagerButton)
        self.addPlot = QtGui.QPushButton(self.centralwidget)
        self.addPlot.setObjectName("addPlot")
        self.horizontalLayout.addWidget(self.addPlot)
        self.showLicense = QtGui.QPushButton(self.centralwidget)
        self.showLicense.setObjectName("showLicense")
        self.horizontalLayout.addWidget(self.showLicense)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout.addWidget(self.quitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scopeArea = QtGui.QMdiArea(self.centralwidget)
        self.scopeArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scopeArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scopeArea.setObjectName("scopeArea")
        self.verticalLayout_2.addWidget(self.scopeArea)
        MainGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 25))
        self.menubar.setObjectName("menubar")
        MainGUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainGUI)
        self.statusbar.setObjectName("statusbar")
        MainGUI.setStatusBar(self.statusbar)

        self.retranslateUi(MainGUI)
        QtCore.QMetaObject.connectSlotsByName(MainGUI)

    def retranslateUi(self, MainGUI):
        MainGUI.setWindowTitle(QtGui.QApplication.translate("MainGUI", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeManagerButton.setText(QtGui.QApplication.translate("MainGUI", "ScopeManager", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterManagerButton.setText(QtGui.QApplication.translate("MainGUI", "ParameterManager", None, QtGui.QApplication.UnicodeUTF8))
        self.addPlot.setText(QtGui.QApplication.translate("MainGUI", "addPlot", None, QtGui.QApplication.UnicodeUTF8))
        self.showLicense.setText(QtGui.QApplication.translate("MainGUI", "ShowLicense", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainGUI", "Quit", None, QtGui.QApplication.UnicodeUTF8))

