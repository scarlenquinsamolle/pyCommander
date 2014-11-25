'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui

class PanelTreeView(QtGui.QTreeView):
    '''
    constructor class, get a widget to be put on.
    '''
    def __init__(self, widget):
        super(PanelTreeView, self).__init__(widget)
    
    '''
    this method captures the tab pressed over a tree view and sends a signal
    '''
    def event(self, event):
        if (event.type()==QtCore.QEvent.KeyPress) and (event.key()==QtCore.Qt.Key_Tab):
            self.emit(QtCore.SIGNAL("tabPressed"))
            return True

        return super(PanelTreeView, self).event(event)