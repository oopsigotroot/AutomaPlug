#!/usr/bin/python
#
#   AutomaPlugSession.py
#
#
#   Copyright 2011 Patrick F. Wilbur
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#

from multiprocessing import Process, Pipe, Queue
from time import sleep
import os,signal

## AutomaPlugSession
#
# Creates a new session to execute an AutomaPlug module within.
#
class AutomaPlugSession():
    def __init__(self):
        self.interactionPipe = None
        self.moduleProcessReference = None
        self.eventsQueue = None
        self.sessionName = None
    def setInput(self,inputText):
        self.interactionPipe.send(inputText)
    def getOutput(self):
        if self.interactionPipe.poll():
            return self.interactionPipe.recv()
        else:
            return None
    def isRunning(self):
        if (self.moduleProcessReference != None):
            return self.moduleProcessReference.is_alive()
        else:
            return False
    def getPid(self):
        if self.moduleProcessReference.is_alive():
            return self.moduleProcessReference.pid
        else:
            return None
    def getEventsQueue(self):
        return self.eventsQueue
    def getSessionName(self):
        return self.sessionName
    def start(self,moduleReference,sessionName,timeout=None):
        self.sessionName = sessionName
        self.interactionPipe, interactionPipeChild = Pipe()
        self.eventsQueue = Queue()
        p = Process(target=moduleReference.run, args=(interactionPipeChild,self.eventsQueue))
        p.start()
        self.moduleProcessReference = p
        if (timeout != None):
            Timer(timeout, self.kill).start()
    def kill(self):
        if self.isRunning():
            os.kill(self.moduleProcessReference.pid,signal.SIGKILL)
        self.interactionPipe = None
        self.moduleProcessReference = None  
