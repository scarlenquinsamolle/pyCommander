'''
Created on Nov 24, 2014

@author: jabber
'''
from PyQt4 import QtCore, QtGui

class PanelTreeView(QtGui.QTreeView):
    '''
    classdocs
    '''
    
    def __init__(self, widget):
        super(PanelTreeView, self).__init__(widget)
        
    def event(self, event):
        if (event.type()==QtCore.QEvent.KeyPress) and (event.key()==QtCore.Qt.Key_Tab):
            self.emit(QtCore.SIGNAL("tabPressed"))
            return True

        return super(PanelTreeView, self).event(event)