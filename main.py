'''
Created on 08-Oct-2013

@author: Alok
'''
import sys
from PyQt4 import QtGui
from gui import window

def main():
    app = QtGui.QApplication(sys.argv)
    mongsterwindow = window.Window()
    mongsterwindow.initUI()  
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()