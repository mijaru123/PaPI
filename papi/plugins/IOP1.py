#!/usr/bin/python3
#-*- coding: latin-1 -*-

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
 
Contributors:
Stefan Ruppin
"""

from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Value, Array
import os
import time
import numpy


class IOP1(IPlugin):
    def start_plugin(self,CoreQueue,IOPQueue,sharedArr_time,sharedArr_value,lock):
        print('Plugin1 started')
        goOn = 1
        t=0
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
            sharedArr_value = numpy.random.rand(1,100)
            sharedArr_time = numpy.linspace(t,t+10,100)
            lock.release()
            time.sleep(0.1)
            t += 1
            CoreQueue.put(['IOP', 'Data'])


