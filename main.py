'''
Created on 21/11/2014

@author: jabber
'''

import sys

from PyQt4 import QtGui
from pyCommander import Ui_MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################
if __name__ == '__main__':
    main()