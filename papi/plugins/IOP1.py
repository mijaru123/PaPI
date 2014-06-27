#!/usr/bin/python3
#-*- coding: latin-1 -*-

"""


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

Contributors:
Stefan Ruppin
"""

from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Value, Array
import os
import time
import numpy
import math

class IOP1(IPlugin):
    def start_plugin(self,CoreQueue, IOPQueue, sharedArr_time, sharedArr_value, lock):
        print('Plugin1 started')
        goOn = 1
        t=1
        while(goOn):
            try:
                event=IOPQueue.get_nowait()
                if (event[1] == 'End'):
                    goOn=0
                    CoreQueue.put(['IOP', 'Join'])
                    break
            except:
                time.sleep(0)

            lock.acquire()
            for i in range(10):
                sharedArr_time[i] = t
                sharedArr_value[i] = math.sin(2*math.pi*0.01*t)
                t += 0.1
            lock.release()
            CoreQueue.put(['IOP', 'Data'])
            time.sleep(0.020)
        print('IOP1: is finished')

