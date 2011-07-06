#!/usr/bin/python
#
#   AutomaPlugSessionManager.py
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


from AutomaPlug.AutomaPlugSession import AutomaPlugSession

## AutomaPlugSessionManager
#
# Creates a new session manager for running AutomaPlug module sessions.
#
class AutomaPlugSessionManager:
    def __init__(self):
        self.moduleSessions = []
        self.activeModuleSession = None
    def startSession(self,moduleReference,sessionName,setActive=True):
        s = AutomaPlugSession()
        s.start(moduleReference,sessionName)
        self.moduleSessions.append(s)
        if (setActive == True):
            self.activeModuleSession = len(self.moduleSessions) - 1
    def endSession(self,sessionIndex):
        if (sessionIndex < len(self.moduleSessions)):
            self.moduleSessions[sessionIndex].kill()
            self.moduleSessions.pop(sessionIndex)
    def getActiveSessionOutputBuffer(self):
        if self.activeModuleSession != None:
            if (0 <= self.activeModuleSession < len(self.moduleSessions)):
                return self.moduleSessions[self.activeModuleSession].getOutput()
    def setActiveSessionInputBuffer(self,inputText):
        if self.activeModuleSession != None:
            if (0 <= self.activeModuleSession < len(self.moduleSessions)):
                self.moduleSessions[self.activeModuleSession].setInput(inputText)
    def setActiveModuleSession(self,sessionIndex):
        if (sessionIndex == None):
            self.activeModuleSession = None
        elif (0 <= sessionIndex < len(self.moduleSessions)):
            self.activeModuleSession = sessionIndex
        else:
            self.activeModuleSession = None

