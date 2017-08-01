import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from uiPrincipal import *
from WindAFD import *
from WindAFN import *

class MainWindow(QMainWindow, UIPrincipal):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.logica()

    def logica(self):
        self.actionNEW_AFD.triggered.connect(self.nuevoAFD)
        self.actionNew_AFN.triggered.connect(self.nuevoAFN)

    def nuevoAFD(self):
        dfa = DFAWindow(self)
        dfa.show()

    def nuevoAFN(self):
        dfa = NFAWindow(self)
        dfa.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UIPrincipal()
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
