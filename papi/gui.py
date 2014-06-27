#!/usr/bin/python3
# -*- coding: latin-1 -*-

"""
Copyright (C) 2014 Technische Universität Berlin,
Fakultät IV - Elektrotechnik und Informatik,
Fachgebiet Regelungssysteme,
Einsteinufer 17, D-10587 Berlin, Germany

This file is part of PaPI.

PaPI is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PaPI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with PaPI.  If not, see <http://www.gnu.org/licenses/>.

Contributors
Sven Knuth
"""

__author__ = 'control'

import sys
import math
from PySide.QtGui import QMainWindow, QPushButton, QApplication, QTextEdit, QToolBar, QLayoutItem, QWidget
from PySide import QtCore, QtGui

import numpy as np
import pyqtgraph as pg

from pyqtgraph import QtGui, QtCore

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

from papi.ui.ui_quitter import Ui_MainWindow
from papi.plugins.VPlugin import VPlugin

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showLicense.clicked.connect(self.fn_fileRead)
        self.addPlot.clicked.connect(self.fn_addPlot)
        self.delPlot.clicked.connect(self.fn_delPlot)

    def fn_fileRead(self):
        '''Read and display GPL licence.'''
        self.textEdit.setText(open('../README.md').read())

    def fn_addPlot(self):
        '''
        Used to add plot
        :return:
        '''

        my_plot = VPlugin()
        self.vertLay.addWidget(my_plot)
        #my_plot.createSample()
        my_plot.startUpdating()



    def fn_delPlot(self):
        '''
        Used to remove plot
        :return:
        '''
        wItem = self.vertLay.takeAt(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QtGui.QMainWindow

    frame = MainWindow()
    frame.show()
    app.exec_()