from PyQt4 import QtGui

class ConnectionWindow(QtGui.QDialog):
    
    def __init__(self):
        super(ConnectionWindow, self).__init__()
        self.setWindowTitle('ConnectionSettings')