'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
import os

from PyQt4 import QtCore, QtGui
from panel_tree_view import PanelTreeView

class CommanderPanel(QtGui.QWidget):
    '''
    classdocs
    '''
    def __init__(self, main_window):
        super(CommanderPanel, self).__init__(main_window.body_container)
        self.set_current_folder()
        self.setup_widget()
        main_window.body_layout.addWidget(self)
        
    def set_current_folder(self, current_folder_path = ""):
        if (current_folder_path == ""):
            current_folder_path = os.getcwd()
            current_folder_name = os.path.basename(os.getcwd())
        else:
            current_folder_name = os.path.basename(current_folder_path)
            
        self.current_folder_path = current_folder_path
        self.current_folder_name = current_folder_name
        
    def setup_widget(self):        
        self.main_layout = QtGui.QVBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setMargin(0)
        
        self.tab = QtGui.QTabWidget(self)
        
        self.tab_widget = QtGui.QWidget()
        self.tab_layout = QtGui.QVBoxLayout(self.tab_widget)
        
        self.path_widget = QtGui.QWidget(self.tab_widget)
        self.path_layout = QtGui.QHBoxLayout(self.path_widget)
        self.path_layout.setMargin(0)
        self.path_layout.setSpacing(0)
        
        self.path_line_edit = QtGui.QLineEdit(self.path_widget)
        self.path_line_edit.setEnabled(False)
        self.path_layout.addWidget(self.path_line_edit)
        
        self.push_up_dir = QtGui.QPushButton(self.path_widget)
        self.push_up_dir.setToolTip("Go up folder")
        self.push_up_dir.setIcon(QtGui.QIcon('resources/icon/cdtoparent.png'))
        self.push_up_dir.setIconSize(QtCore.QSize(24,24))
        self.push_up_dir.clicked.connect(self.go_parent_clicked)
        self.path_layout.addWidget(self.push_up_dir)
        
        self.tab_layout.addWidget(self.path_widget)
        
        self.tree_view = PanelTreeView(self.tab_widget)
        self.model = QtGui.QFileSystemModel()
        #self.model.setFilter(QtCore.QDir.Drives)
        self.tree_view.setModel(self.model)
        self.tree_view.setItemsExpandable(False)    
        self.tree_view.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        
        self.tree_view.clicked.connect(self.tree_clicked)
        self.tree_view.doubleClicked.connect(self.tree_double_clicked)
        self.tab_layout.addWidget(self.tree_view)
        
        self.status_widget = QtGui.QWidget(self.tab_widget)
        self.status_layout = QtGui.QHBoxLayout(self.status_widget)
        self.status_layout.setMargin(0)
        self.status_layout.setSpacing(0)
        
        self.status_line_edit = QtGui.QLabel(self.status_widget)
        self.status_line_edit.setText(str(self.model.rowCount(self.model.index(self.current_folder_path))) + " / global folder data here")
        self.status_layout.addWidget(self.status_line_edit)
        self.tab_layout.addWidget(self.status_widget)
        
        self.tab.addTab(self.tab_widget, "")
        self.main_layout.addWidget(self.tab)
        
        self.tab.setCurrentIndex(0)
        self.goto_folder(self.model.index(self.current_folder_path))
    
    def goto_folder(self, index):
        self.tree_view.setRootIndex(index)
        self.set_current_folder(str(self.model.filePath(index)))
        self.model.setRootPath(self.current_folder_path)
        self.path_line_edit.setText(self.current_folder_path)
        if self.current_folder_name != "":
            self.tab.setTabText(self.tab.indexOf(self.tab_widget), self.current_folder_name)
        else:
            self.tab.setTabText(self.tab.indexOf(self.tab_widget), self.current_folder_path)
    
    def tree_clicked(self, index):
        pass
    
    def tree_double_clicked(self, index):
        if index.model().isDir(index):
            self.goto_folder(index)
            
    def go_parent_clicked(self):
        if self.current_folder_name != "":
            self.goto_folder(self.model.parent(self.model.index(self.current_folder_path)))