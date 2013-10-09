from PyQt4 import QtGui
from connectionWindow import ConnectionWindow

class Window(QtGui.QMainWindow): 
    
    def __init__(self):
        super(Window, self).__init__()
        
    def showConnectionDialog(self):
        connectionWindow = ConnectionWindow()
        connectionWindow.show()
        connectionWindow.exec_()
        
        
    def initMenuBar(self):
        menuBar = self.menuBar()
        
        exitAction = QtGui.QAction("&Exit", self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        connectAction = QtGui.QAction("&Connect", self)
        connectAction.setShortcut('Ctrl + T') 
        connectAction.setToolTip('Click to Connect')
        connectAction.triggered.connect(self.showConnectionDialog)
        
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(connectAction)
        fileMenu.addAction(exitAction)
        
    def initUI(self):
        
        self.setGeometry(20,20,700,500)
        self.setWindowTitle('Mongster Beta 0.2')
        self.initMenuBar()
        self.showMaximized()
        
        