# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyCommander.ui'
#
# Created: Fri Nov 21 12:45:13 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import os, sys

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

############################################################################
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setup_ui()
        
    def setup_ui(self):
        self.resize(1024, 800)
        self.setWindowTitle("PyCommander")
        
        self.setup_body()
        self.setup_menu_bar()
        self.setup_status_bar()
        self.setup_connections()
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def setup_body(self):
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setAutoFillBackground(False)
        self.central_layout = QtGui.QVBoxLayout(self.central_widget)
        
        self.body_container = QtGui.QFrame(self.central_widget)
        self.body_layout = QtGui.QHBoxLayout(self.body_container)
        self.body_layout.setMargin(0)
                
        self.tab_left = Ui_MainPanel(self)
        self.tab_right = Ui_MainPanel(self)
        
        self.central_layout.addWidget(self.body_container)
        
        self.footer_container = QtGui.QFrame(self.central_widget)
        self.footer_container.setFrameShape(QtGui.QFrame.StyledPanel)
        self.footer_container.setFrameShadow(QtGui.QFrame.Raised)
        self.footer_layout = QtGui.QHBoxLayout(self.footer_container)
        self.footer_layout.setSpacing(0)
        self.footer_layout.setMargin(0)
        
        self.setup_footer()
        
        self.central_layout.addWidget(self.footer_container)
        
        self.setCentralWidget(self.central_widget)
    
    def setup_menu_bar(self):
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        
        # Setting up menu Files
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle("Files")
        
        self.actionQuit = QtGui.QAction(self)
        self.actionQuit.setText("Quit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setStatusTip("Exit application")
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        # Setting up configuration
        self.menuConfiguration = QtGui.QMenu(self.menubar)
        self.menuConfiguration.setTitle("Configuration")
        self.menubar.addAction(self.menuConfiguration.menuAction())
        
        # Setting up help
        self.menuHelp = QtGui.QMenu(self.menubar)        
        self.menuHelp.setTitle("Help")
        
        self.actionAboutPyComander = QtGui.QAction(self)
        self.actionAboutPyComander.setText("About PyComander...")
        
        self.menuHelp.addAction(self.actionAboutPyComander)
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.setMenuBar(self.menubar)
        
    def setup_status_bar(self):
        self.statusbar = QtGui.QStatusBar(self)        
        self.setStatusBar(self.statusbar)
                
    def setup_footer(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.push_button_f3 = QtGui.QPushButton(self.footer_container)
        self.push_button_f3.setFont(font)
        self.push_button_f3.setText("F3 View")
        self.push_button_f3.setShortcut("F3")
        self.footer_layout.addWidget(self.push_button_f3)
       
        self.push_button_f4 = QtGui.QPushButton(self.footer_container)
        self.push_button_f4.setFont(font)
        self.push_button_f4.setText("F4 Edit")
        self.push_button_f4.setShortcut("F4")
        self.footer_layout.addWidget(self.push_button_f4)
        
        self.push_button_f5 = QtGui.QPushButton(self.footer_container)
        self.push_button_f5.setFont(font)
        self.push_button_f5.setText("F5 Copy")
        self.push_button_f5.setShortcut("F5")
        self.footer_layout.addWidget(self.push_button_f5)
        
        self.push_button_f6 = QtGui.QPushButton(self.footer_container)
        self.push_button_f6.setFont(font)
        self.push_button_f6.setText("F6 Move")
        self.push_button_f6.setShortcut("F6")
        self.footer_layout.addWidget(self.push_button_f6)
        
        self.push_button_f7 = QtGui.QPushButton(self.footer_container)
        self.push_button_f7.setFont(font)
        self.push_button_f7.setText("F7 New Folder")
        self.push_button_f7.setShortcut("F7")
        self.footer_layout.addWidget(self.push_button_f7)
        
        self.push_button_f8 = QtGui.QPushButton(self.footer_container)
        self.push_button_f8.setFont(font)
        self.push_button_f8.setText("F8 View")
        self.push_button_f8.setShortcut("F8")
        self.footer_layout.addWidget(self.push_button_f8)
        
        self.push_button_alt_f4 = QtGui.QPushButton(self.footer_container)
        self.push_button_alt_f4.setFont(font)
        self.push_button_alt_f4.setText("ALT+F4 Exit")
        self.footer_layout.addWidget(self.push_button_alt_f4)
        
    def setup_connections(self):
        self.connect(self.tab_left.tree_view, QtCore.SIGNAL("tabPressed"), self.switch_to_right_panel)
        self.connect(self.tab_right.tree_view, QtCore.SIGNAL("tabPressed"), self.switch_to_left_panel)
    
    def switch_to_left_panel(self):
        self.tab_left.tree_view.setFocus()
        
    def switch_to_right_panel(self):
        self.tab_right.tree_view.setFocus()
        
############################################################################
class Ui_MainPanel(QtGui.QWidget):
    
    def __init__(self, main_window):
        super(Ui_MainPanel, self).__init__(main_window.body_container)
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
        
        self.tree_view = Ui_TreeView(self.tab_widget)
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
        
        self.tab.addTab(self.tab_widget, _fromUtf8(""))
        self.main_layout.addWidget(self.tab)
        
        self.tab.setCurrentIndex(0)
        self.goto_folder(self.model.index(self.current_folder_path))
    
    def goto_folder(self, index):
        self.tree_view.setRootIndex(index)
        self.set_current_folder(str(self.model.filePath(index)))
        self.model.setRootPath(self.current_folder_path)
        self.path_line_edit.setText(self.current_folder_path)
        self.tab.setTabText(self.tab.indexOf(self.tab_widget), self.current_folder_name)
    
    def tree_clicked(self, index):
        pass
    
    def tree_double_clicked(self, index):
        if index.model().isDir(index):
            self.goto_folder(index)
            
    def go_parent_clicked(self):
        self.goto_folder(self.model.parent(self.model.index(self.current_folder_path)))
        print self.current_folder_path
    
    # print self.model.itemFromIndex(index).text()
    
############################################################################
class Ui_TreeView(QtGui.QTreeView):
    def __init__(self, widget):
        super(Ui_TreeView, self).__init__(widget)
        
    def event(self, event):
        if (event.type()==QtCore.QEvent.KeyPress) and (event.key()==QtCore.Qt.Key_Tab):
            self.emit(QtCore.SIGNAL("tabPressed"))
            return True

        return super(Ui_TreeView, self).event(event)
############################################################################
def main():
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################
if __name__ == '__main__':
    main()