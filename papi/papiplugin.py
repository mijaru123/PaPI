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

__author__ = 'controll'

from yapsy.IPlugin import IPlugin

class PaPIPlugin(IPlugin):

    __core_msg_queue__ = ''
    __msg_queue__ = ''
    def __init__(self):
        self.__core_msg_queue__ = ''

    def start_plugin(self,sharedArr, core_msg_queue,msg_queue,lock):
        print("StartPlugin")
        self.__msg_queue__ = msg_queue
        self.__core_msg_queue__ == core_msg_queue
        self.__lock__ = lock
    def end_plugin(self):
        print("StartPlugin")


    def __static__(self):
        print("StaticPart")

    def custom(self):
        print("CustomPart")

    def __iterate__(self):
        while 1==1:
            self.header()
            self.custom()

