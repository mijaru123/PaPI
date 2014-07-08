# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui/manager/scope.ui'
#
# Created: Tue Jul  8 15:58:05 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScopeManager(object):
    def setupUi(self, ScopeManager):
        ScopeManager.setObjectName("ScopeManager")
        ScopeManager.resize(683, 380)
        self.centralwidget = QtGui.QWidget(ScopeManager)
        self.centralwidget.setObjectName("centralwidget")
        self.scopeList = QtGui.QListWidget(self.centralwidget)
        self.scopeList.setGeometry(QtCore.QRect(20, 20, 256, 192))
        self.scopeList.setObjectName("scopeList")
        ScopeManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ScopeManager)
        self.statusbar.setObjectName("statusbar")
        ScopeManager.setStatusBar(self.statusbar)

        self.retranslateUi(ScopeManager)
        QtCore.QMetaObject.connectSlotsByName(ScopeManager)

    def retranslateUi(self, ScopeManager):
        ScopeManager.setWindowTitle(QtGui.QApplication.translate("ScopeManager", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

