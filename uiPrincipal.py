# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from uiAFDWin1 import *

class UIPrincipal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(292, 213)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 292, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFILE = QtWidgets.QMenu(self.menuBar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuNEW = QtWidgets.QMenu(self.menuFILE)
        self.menuNEW.setObjectName("menuNEW")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setEnabled(True)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNEW_AFD = QtWidgets.QAction(MainWindow)
        self.actionNEW_AFD.setObjectName("actionNEW_AFD")
        self.actionNew_AFN = QtWidgets.QAction(MainWindow)
        self.actionNew_AFN.setObjectName("actionNew_AFN")
        self.actionNEW_AFNE = QtWidgets.QAction(MainWindow)
        self.actionNEW_AFNE.setObjectName("actionNEW_AFNE")
        self.menuNEW.addAction(self.actionNEW_AFD)
        self.menuNEW.addAction(self.actionNew_AFN)
        self.menuNEW.addAction(self.actionNEW_AFNE)
        self.menuFILE.addAction(self.menuNEW.menuAction())
        self.menuBar.addAction(self.menuFILE.menuAction())
        self.menuBar.setNativeMenuBar(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        self.menuNEW.setTitle(_translate("MainWindow", "NEW"))
        self.actionNEW_AFD.setText(_translate("MainWindow", "New AFD"))
        self.actionNew_AFN.setText(_translate("MainWindow", "New AFN"))
        self.actionNEW_AFNE.setText(_translate("MainWindow", "New AFN-Epsilon"))
