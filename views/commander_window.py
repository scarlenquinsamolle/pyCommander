'''
Created on Nov 24, 2014

@author: Jafeth Garcia
'''
from PyQt4 import QtCore, QtGui
from commander_panel import CommanderPanel

class CommanderWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''
    
    def __init__(self):
        super(CommanderWindow, self).__init__()
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
        
        self.body_container = QtGui.QSplitter(self.central_widget)
        self.body_layout = QtGui.QHBoxLayout(self.body_container)
        self.body_layout.setMargin(0)
                
        self.tab_left = CommanderPanel(self)
        self.tab_right = CommanderPanel(self)
        
        #splitter = QtGui.QSplitter(self.body_container)
        #splitter.addWidget(self.tab_left)
        #splitter.addWidget(self.tab_right)
        #self.body_layout.addWidget(splitter)
        
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