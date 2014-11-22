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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setup_ui()
        
    def setup_ui(self):
        self.resize(1024, 800)
        
        self.setup_body()
        self.setup_menu_bar()
        self.setup_status_bar()
        
        self.retranslateUi()        
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "PyCommander", None))
        self.pushButton.setText(_translate("MainWindow", "F3 View", None))
        self.pushButton_2.setText(_translate("MainWindow", "F4 Edit", None))
        self.pushButton_3.setText(_translate("MainWindow", "F5 Copy", None))
        self.pushButton_4.setText(_translate("MainWindow", "F6 Move", None))
        self.pushButton_5.setText(_translate("MainWindow", "F7 New Folder", None))
        self.pushButton_6.setText(_translate("MainWindow", "F8 Delete", None))
        self.pushButton_7.setText(_translate("MainWindow", "Alt+F4 Exit", None))
        
    def setup_body(self):
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.bodyContainer = QtGui.QFrame(self.centralwidget)
        
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.bodyContainer)
        self.horizontalLayout_2.setMargin(0)
                
        self.tabLeft = Ui_MainPanel(self.bodyContainer)
        self.horizontalLayout_2.addWidget(self.tabLeft.widget)
        
        self.tabRight = Ui_MainPanel(self.bodyContainer)
        self.horizontalLayout_2.addWidget(self.tabRight.widget)
        
        self.verticalLayout.addWidget(self.bodyContainer)
        
        
        self.footerContainer = QtGui.QFrame(self.centralwidget)
        self.footerContainer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.footerContainer.setFrameShadow(QtGui.QFrame.Raised)
        self.footerContainer.setObjectName(_fromUtf8("footerContainer"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.footerContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.pushButton = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.footerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.verticalLayout.addWidget(self.footerContainer)
        
        self.setCentralWidget(self.centralwidget)
    
    def setup_menu_bar(self):
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        
        # Setting up menu Files
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle("Files")
        
        self.actionQuit = QtGui.QAction(self)
        self.actionQuit.setText("Quit")
        
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
        pass

class Ui_MainPanel(object):
    
    def __init__(self, container, current_folder_path = ""):
        if (current_folder_path == ""):
            current_folder_path = os.getcwd()
            current_folder_name = os.path.basename(os.getcwd())
        else:
            current_folder_name = os.path.basename(current_folder_path)
            
        self.current_folder_path = current_folder_path
        self.current_folder_name = current_folder_name
        self.setup_widget(container)
        
    def setup_widget(self, container):
        self.widget = QtGui.QWidget(container)
        
        self.main_layout = QtGui.QVBoxLayout(self.widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setMargin(0)
        
        self.tab = QtGui.QTabWidget(self.widget)
        
        self.tab_widget = QtGui.QWidget()
        self.tab_layout = QtGui.QVBoxLayout(self.tab_widget)
        
        self.path_widget = QtGui.QWidget(self.tab_widget)
        self.path_layout = QtGui.QGridLayout(self.path_widget)
        self.path_layout.setMargin(0)
        self.path_layout.setSpacing(0)
        
        self.path_line_edit = QtGui.QLineEdit(self.path_widget)
        self.path_line_edit.setText(self.current_folder_path)
        self.path_line_edit.setEnabled(False)
        self.path_layout.addWidget(self.path_line_edit, 0, 0, 1, 1)
        self.tab_layout.addWidget(self.path_widget)
        
        self.tree_view = QtGui.QTreeView(self.tab_widget)
        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath(os.getcwd())
        #self.modelLeft.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)
        self.tree_view.setModel(self.model)
        self.tree_view.setItemsExpandable(False)    
        self.tree_view.setRootIndex(self.model.index(self.current_folder_path))
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
        self.tab.setTabText(self.tab.indexOf(self.tab_widget), self.current_folder_name)
        
        self.tab.setCurrentIndex(0)
        
def main():
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()