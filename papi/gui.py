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
from papi import VPlugin

__author__ = 'control'




import sys

from PySide.QtGui import QMainWindow, QApplication

from multiprocessing import Process, Value, Array, Lock, Queue

import pyqtgraph as pg
import time

from pyqtgraph import QtGui, QtCore

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

from papi.ui.ui_quitter import Ui_MainWindow


class GUI(QMainWindow, Ui_MainWindow):
    goOn = 1;
    def __init__(self, parent=None, CoreQueue=Queue(), GUIQueue=Queue(), timeArr=[], valueArr=[], lock=Lock() ):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.showLicense.clicked.connect(self.fn_fileRead)
        self.addPlot.clicked.connect(self.fn_addPlot)
        self.delPlot.clicked.connect(self.fn_delPlot)

        self.coreq = CoreQueue
        self.guiq = GUIQueue
        self.valueArr = valueArr
        self.timeArr = timeArr

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkEventsCore)
        self.timer.start(50)


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
        my_plot.startUpdating()

    def fn_delPlot(self):
        '''
        Used to remove plot
        :return:
        '''

        wItem = self.vertLay.takeAt(0)

    def checkEventsFromCore(self):
        """

        :return:
        """
        try:
            coreEvents = self.coreq.get_nowait()
        except:
            time.sleep(0)

    def sendEventToCore(self):
        """

        :return:
        """
        try:
            guiEvents = self.guiq.get_nowait()
        except:
            time.sleep(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QtGui.QMainWindow
    frame = GUI()
    frame.show()

    app.exec_()


def startGUI( CoreQueue, GUIQueue, timeArr, valueArr, lock):
    app = QApplication(sys.argv)
    mw = QtGui.QMainWindow
    gui = GUI(CoreQueue=CoreQueue, GUIQueue=GUIQueue, timeArr=timeArr, valueArr=valueArr, lock=lock)
    gui.show()
    app.exec_()