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
import time

from PySide.QtGui import QMainWindow, QApplication

import pyqtgraph as pg
from pyqtgraph import QtGui, QtCore
from papi.VPlugin import VPlugin
from papi.gui.manager.scope import ScopeManger

from multiprocessing import Process, Array, Lock, Queue

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

from papi.ui.gui.main import Ui_MainGUI


class GUI(QMainWindow, Ui_MainGUI):
    goOn = 1;
    activeScopes = {}
    scopeID = 1
    scopeManger = None

    def __init__(self, parent=None, CoreQueue=Queue(), GUIQueue=Queue(), timeArr=[], valueArr=[], lock=Lock() ):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.showLicense.clicked.connect(self.fn_fileRead)

        self.addPlot.clicked.connect(self.fn_addPlot)

        self.parameterManagerButton.clicked.connect(self.openParameterManager)

        self.quitButton.clicked.connect(self.fn_quit)
        self.scopeManagerButton.clicked.connect(self.openScopeManager)
        self.lock = lock;

        self.coreq = CoreQueue
        self.guiq = GUIQueue
        self.valueArr = valueArr
        self.timeArr = timeArr

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkOwnEvents)
        self.timer.start(1/25*1000)

    def fn_fileRead(self):
        '''Read and display GPL licence.'''
        print(open('../README.md').read())

    def fn_addPlot(self):
        '''
        Used to add plot
        :return:
        '''

        scope = VPlugin()

        self.scopeArea.addSubWindow(scope.getSubWindow())

        scope.setID(self.scopeID)

        self.activeScopes[self.scopeID] = scope
        scope.getSubWindow().show()

        self.scopeID += 1

       # scope.getSubWindow().close.connect(self.openParameterManager)

    def fn_delPlot(self):
        '''
        Used to remove plot
        :return:
        '''

        wItem = self.vertLay.takeAt(0)

    def checkOwnEvents(self):
        """

        :return:
        """

        try:
            while self.guiq.full :
                event = self.guiq.get_nowait()
                self.evaluateEvent(event)
        except:
            time.sleep(0)

    def evaluateEvent(self,event):
        if event[0] == 'Core':
            if event[1] == 'Data':
                #print("GUI: New Data")
                #self.lock.aquire()

                for key in self.activeScopes.keys():
                    scope = self.activeScopes[key]
                    scope.addData( self.timeArr, self.valueArr )
                    scope.updateplot()

                #self.lock.release()

    def fn_quit(self):
        self.sendEventToCore(['GUI','EndJoin'])
        self.close()

    def sendEventToCore(self,event):
        """

        :return:
        """

        self.coreq.put(event)

    def openScopeManager(self):
        self.scopeManger = ScopeManger(scopes=self.activeScopes)
        self.scopeManger.listScopes()
        self.scopeManger.show()

    def openParameterManager(self):
        print("OpenParameterManager")


    def scopeClosed(self):
        print("Scope Closed")

  #  def closeScope(self):

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
