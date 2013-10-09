from PyQt4 import QtGui

menuList = []

def initMenuBar():
    initFileMenu()
    
    
def initFileMenu():
    
    exitAction = QtGui.QAction("&Exit");
    exitAction.setShortcut('Ctrl + Q')
    exitAction.setToolTip('Exit Application')
    exitAction.triggered.connect(QtGui.qApp.quit())
    
    
    
    fileMenu = QtGui.QMenu()
    fileMenu.setTitle("&File")
    fileMenu.addAction(exitAction)
    
    menuList.append(fileMenu)