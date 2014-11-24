# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyCommander.ui'
#
# Created: Fri Nov 21 12:45:13 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(872, 707)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bodyContainer = QtGui.QFrame(self.centralwidget)
        self.bodyContainer.setObjectName(_fromUtf8("bodyContainer"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.bodyContainer)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabLeft = QtGui.QTabWidget(self.bodyContainer)
        self.tabLeft.setObjectName(_fromUtf8("tabLeft"))
        self.tabL_1 = QtGui.QWidget()
        self.tabL_1.setObjectName(_fromUtf8("tabL_1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabL_1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame_3 = QtGui.QFrame(self.tabL_1)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_2.addWidget(self.frame_3, 3, 0, 1, 1)
        self.widget = QtGui.QWidget(self.tabL_1)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.treeViewLeft = QtGui.QTreeView(self.tabL_1)
        self.treeViewLeft.setObjectName(_fromUtf8("treeViewLeft"))

        #self.modelLeft = QtGui.QDirModel()
        #Using model QFileSystemModel
        self.treeViewLeft.model = QtGui.QFileSystemModel()
        self.treeViewLeft.model.setRootPath( QtCore.QDir.currentPath() )
        self.treeViewLeft.setModel(self.treeViewLeft.model)


        self.gridLayout_2.addWidget(self.treeViewLeft, 1, 0, 1, 1)
        self.tabLeft.addTab(self.tabL_1, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabLeft)
        self.tabRight = QtGui.QTabWidget(self.bodyContainer)
        self.tabRight.setObjectName(_fromUtf8("tabRight"))
        self.tabR_1 = QtGui.QWidget()
        self.tabR_1.setObjectName(_fromUtf8("tabR_1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabR_1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame_2 = QtGui.QFrame(self.tabR_1)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.tabR_1)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.treeViewRight = QtGui.QTreeView(self.tabR_1)
        self.treeViewRight.setObjectName(_fromUtf8("treeViewRight"))

#        self.modelRight = QtGui.QDirModel()
        #self.treeViewRight.setModel(self.modelRight)

        self.treeViewRight.model = QtGui.QFileSystemModel()
        self.treeViewRight.model.setRootPath( QtCore.QDir.currentPath() )
        self.treeViewRight.setModel(self.treeViewRight.model)


        self.gridLayout_3.addWidget(self.treeViewRight, 1, 0, 1, 1)
        self.tabRight.addTab(self.tabR_1, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabRight)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuConfiguration = QtGui.QMenu(self.menubar)
        self.menuConfiguration.setObjectName(_fromUtf8("menuConfiguration"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_PyComander = QtGui.QAction(MainWindow)
        self.actionAbout_PyComander.setObjectName(_fromUtf8("actionAbout_PyComander"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_PyComander)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabLeft.setCurrentIndex(0)
        self.tabRight.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #events on first attempt
        self.treeViewLeft.clicked.connect(self.on_treeview_clicked)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyCommander", None))
        self.tabLeft.setTabText(self.tabLeft.indexOf(self.tabL_1), _translate("MainWindow", "Tab 1", None))
        self.tabRight.setTabText(self.tabRight.indexOf(self.tabR_1), _translate("MainWindow", "Tab 1", None))
        self.pushButton.setText(_translate("MainWindow", "F3 View", None))
        self.pushButton_2.setText(_translate("MainWindow", "F4 Edit", None))
        self.pushButton_3.setText(_translate("MainWindow", "F5 Copy", None))
        self.pushButton_4.setText(_translate("MainWindow", "F6 Move", None))
        self.pushButton_5.setText(_translate("MainWindow", "F7 New Folder", None))
        self.pushButton_6.setText(_translate("MainWindow", "F8 Delete", None))
        self.pushButton_7.setText(_translate("MainWindow", "Alt+F4 Exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "Files", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration", None))
        self.actionAbout_PyComander.setText(_translate("MainWindow", "About PyComander...", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))


    # Obtaining the path of the selected file-row

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.treeViewLeft.model.index(index.row(), 0, index.parent())
       # indexItem.QFontsetStyleSheet("QTreeView::item:selected { border-color:green; "
                      # "border-style:outset; border-width:2px; color:black; }");

        # path or filename selected
        fileName = self.treeViewLeft.model.fileName(indexItem)
        # full path/filename selected
        filePath = self.treeViewLeft.model.filePath(indexItem)
       # filePermissions = self.treeViewLeft.model.file(indexItem)

        fileInfo = QtCore.QFileInfo(fileName)
        fileDetails = self.treeViewLeft.model.fileInfo(indexItem)




        #print (filePermissions)
        print (fileDetails, fileInfo)
        print(fileName)
        print(filePath)




