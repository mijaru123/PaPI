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

__author__ = 'Knuth'

from yapsy.IPlugin import IPlugin
from pyqtgraph import PlotWidget
from math import sin
from numpy import linspace
import numpy as np

import collections
import random
import time
import math

from pyqtgraph import QtGui, QtCore

class VPlugin(PlotWidget):

    count = 0.0;
    _interval = 0.1;
    def __init__(self, name='Plot', sampleinterval=1, timewindow=10000., size=(600,350)):

        self.name = name
        PlotWidget.__init__(self)

        self._interval = int(sampleinterval*1000)
        self._bufsize = int(timewindow/sampleinterval)
        self.tDatabuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.yDatabuffer = collections.deque([0.0]*self._bufsize, self._bufsize)

        self.x = np.linspace(-timewindow, 0.0, self._bufsize)
        self.y = np.zeros(self._bufsize, dtype=np.float)

        self.resize(*size)
        self.showGrid(x=True, y=True)
        self.setLabel('left', 'amplitude', 'V')
        self.setLabel('bottom', 'time', 's')
        self.curve = self.plot(self.x, self.y, pen=(255,0,0))
        self._interval = sampleinterval
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self._interval)

    def updateplot(self):
        self.x[:] = self.tDatabuffer
        self.y[:] = self.yDatabuffer
        self.curve.setData(self.x, self.y)

    def addData(self,t,y):

        for elem in t:
            self.tDatabuffer.append( elem )

        for elem in y:
            self.yDatabuffer.append( elem )