#!/usr/bin/python
# -*- coding:Utf-8 -*-

# Copyright (C) 2013 Pâris Quentin
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import socket, threading, thread, os, wx, time, random
import string

class Observer(object): 
    def __init__(self):
        self.subjects = []
        
    def addSubject(self, subjectToSet):
        self.subjects.append(subjectToSet)
        self.notify()
    
    def removeSubjects(self):
        self.subjects = []
        
    def getSubject(self, subject_number = 0):
        return self.subjects[subject_number]
        
    # Abstract methode
    def notify(self):
        return None