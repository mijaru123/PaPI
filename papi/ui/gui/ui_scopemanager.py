# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scopemanager.ui'
#
# Created: Mon Jul  7 11:40:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScopeManager(object):
    def setupUi(self, ScopeManager):
        ScopeManager.setObjectName("ScopeManager")
        ScopeManager.resize(574, 414)
        self.centralwidget = QtGui.QWidget(ScopeManager)
        self.centralwidget.setObjectName("centralwidget")
        self.scopeList = QtGui.QListWidget(self.centralwidget)
        self.scopeList.setGeometry(QtCore.QRect(10, 10, 261, 371))
        self.scopeList.setObjectName("scopeList")
        self.removeActive = QtGui.QPushButton(self.centralwidget)
        self.removeActive.setGeometry(QtCore.QRect(380, 130, 98, 27))
        self.removeActive.setObjectName("removeActive")
        ScopeManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ScopeManager)
        self.statusbar.setObjectName("statusbar")
        ScopeManager.setStatusBar(self.statusbar)

        self.retranslateUi(ScopeManager)
        QtCore.QMetaObject.connectSlotsByName(ScopeManager)

    def retranslateUi(self, ScopeManager):
        ScopeManager.setWindowTitle(QtGui.QApplication.translate("ScopeManager", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.removeActive.setText(QtGui.QApplication.translate("ScopeManager", "remove", None, QtGui.QApplication.UnicodeUTF8))

