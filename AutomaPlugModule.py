#!/usr/bin/python
#
#   AutomaPlugModule.py
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

class AutomaPlugModule:
    def __init__(self):
        self.interactionPipe = None
        self.inboundEventsQueue = None
        self.variables = {}
        self.outboundEventsQueue = None
        self.pluginName = 'Untitled Module'
    def input(self):
        return self.interactionPipe.recv()
    def output(self,outputText):
        self.interactionPipe.send(outputText)
    def signalEvent(self,event):
        self.outboundEventsQueue.put(event)
    def setVar(self,key,value):
        self.variables[key] = value
    def getVar(self,key):
        return self.variables[key]
    def getVars(self):
        return self.variables
    #def returnVars(self):
    #    self.variablesPipe.send(self.variables)
    def run(self,interactionPipe,outboundEventsQueue=None,inboundEventsQueue=None,variables={}):
        self.interactionPipe = interactionPipe
        self.inboundEventsQueue = inboundEventsQueue
        self.variables = variables
        self.outboundEventsQueue = outboundEventsQueue
        self.setVar('returnValue',self.execute())
    def cleanup(self):
        if self.interactionPipe != None:
            self.interactionPipe.close()
    def execute(self):
        return None
    