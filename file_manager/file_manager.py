'''
Created on Nov 24, 2014

@author: Scarlen Quinsamolle
'''
import sys
from PyQt4 import QtGui
from views.commander_panel import CommanderPanel


class FileManager(QtGui.QWidget):

    def __init__(self, commander_window):
        super(FileManager, self).__init__()
        self.commander_window = commander_window


    def add_new_file(self):



        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Add New File',self.commander_window.tab_left.current_folder_path, selectedFilter='*.txt')
        if fileName:
            print fileName



