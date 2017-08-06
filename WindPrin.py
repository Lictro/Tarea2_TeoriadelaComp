import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from uiPrincipal import *
from WindAFD import *
from WindAFN import *
from WindAFNE import *

class MainWindow(QMainWindow, UIPrincipal):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.logica()

    def logica(self):
        self.actionNEW_AFD.triggered.connect(self.nuevoAFD)
        self.actionNew_AFN.triggered.connect(self.nuevoAFN)
        self.actionNEW_AFNE.triggered.connect(self.nuevoAFNE)

    def nuevoAFD(self):
        maquina = AFD()
        dfa = DFAWindow(self)
        dfa.cargarMaquina(maquina)
        dfa.show()

    def nuevoAFN(self):
        maquina = AFN()
        dfa = NFAWindow(self)
        dfa.cargarMaquina(maquina)
        dfa.show()

    def nuevoAFNE(self):
        maquina = Epsilon()
        dfa = NFAEWindow(self)
        dfa.cargarMaquina(maquina)
        dfa.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UIPrincipal()
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
