from uiAFNEWin import *
from MaquinaAFNEp import *

class NFAEWindow(QMainWindow, UIAFNEWindow):
    def __init__(self,parent=None):
        super(NFAEWindow,self).__init__(parent)
        self.setupUi(self)
        self.logica()

    def cargarMaquina(self,maquina):
        self.workspace = maquina

    def logica(self):
        self.x = 0
        self.y = 0
        self.cargarMaquina(maquina=Epsilon())
        self.nodoBtn.clicked.connect(self.agregarNodo)
        self.aristaBtn.clicked.connect(self.agregarAristas)
        self.table1.cellClicked.connect(self.origenDestino)
        self.actuBtn.clicked.connect(self.drawing)
        self.aceptaBtn.clicked.connect(self.addDestino)
        self.inicioBtn.clicked.connect(self.setOrigen)
        self.borrarBtn1.clicked.connect(self.borrarNodo)
        self.borrarBtn2.clicked.connect(self.borrarEdge)
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionGuardar_y_Salir.triggered.connect(self.guardarSalir)
        self.actionSalir.triggered.connect(self.close)
        self.evaluarBtn.clicked.connect(self.Evaluacion)
        self.nodelist = []
        self.edgelist = []
        self.origen = "-1"
        self.destino = "-1"
        self.origenNodo = -1
        self.destinoNodos = []
        self.origenFlag = False
        self.destinoFlag = False
        self.countNodes = 0
        self.fichero_actual = ""
        self.ruta = "/Users/catedral/PycharmProjects/MacGraph/Maquinas"

    def abrir(self):
        nombre_fichero = QFileDialog.getOpenFileName(self, "Abrir Maquina", self.ruta)
        if nombre_fichero[0] != "":
            self.fichero_actual = nombre_fichero[0]
            rutas = self.fichero_actual.split("/")
            longitud = len(rutas)
            self.workspace.reinicio()
            self.workspace.cargar(rutas[longitud-1])
            self.sincronizar()

    def guardar(self):
        if self.fichero_actual:
            ruta_guardar = self.fichero_actual
        else:
            ruta_guardar = self.ruta

        nombre_fichero = QFileDialog.getSaveFileName(self, "Guardar Maquina", ruta_guardar)
        if nombre_fichero[0] != "":
            self.fichero_actual = nombre_fichero[0]
            rutas = self.fichero_actual.split("/")
            longitud = len(rutas)
            self.workspace.guardar(rutas[longitud-1])

    def guardarSalir(self):
        if self.fichero_actual:
            ruta_guardar = self.fichero_actual
        else:
            ruta_guardar = self.ruta

        nombre_fichero = QFileDialog.getSaveFileName(self, "Guardar Maquina", ruta_guardar)
        print(nombre_fichero)
        if nombre_fichero[0] != "":
            self.fichero_actual = nombre_fichero[0]
            rutas = self.fichero_actual.split("/")
            longitud = len(rutas)
            self.workspace.guardar(rutas[longitud-1])
            self.close()

    def drawing(self):
        scene = QGraphicsScene()
        for elemento in self.nodelist:
            scene.addItem(elemento)
        index1 = 0
        index2 = 0
        self.origen = "-1"
        self.destino = "-1"
        self.origenFlag = False
        self.destinoFlag = False
        for elemento in self.edgelist:
            con = 0
            while con<len(self.nodelist):
                if self.nodelist[con].num == elemento[0]:
                    index1 = con
                if self.nodelist[con].num == elemento[1]:
                    index2 = con
                con = con + 1
            scene.addItem(Edge(self.nodelist[index1],self.nodelist[index2],elemento[2]))
            index1 = 0
            index2 = 0
        self.graphicsView.setScene(scene)

    def agregarNodo(self):
        num = self.countNodes
        self.workspace.agregarEstado(num,False)
        nodo = Node(self.graphicsView,num)
        nodo.setPos(self.x,self.y)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        line = QtWidgets.QLabel(str(num))
        line.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        line.setFont(font)
        prox = QtWidgets.QGraphicsProxyWidget(nodo)
        prox.setWidget(line)
        self.nodelist.append(nodo)
        self.x = self.x + 50
        self.y = self.y + 50
        self.table1.insertRow(1)
        self.drawing()
        self.actualizarLista1()
        self.countNodes = self.countNodes + 1

    def actualizarLista1(self):
        self.table1.setRowCount(0)
        self.table1.setRowCount(len(self.nodelist))
        index = 0
        while index<len(self.nodelist):
            self.table1.setItem(index,0,QtWidgets.QTableWidgetItem("Nodo "+str(index)))
            index = index + 1

    def actualizarLista2(self):
        self.table2.setRowCount(0)
        self.table2.setRowCount(len(self.edgelist))
        index = 0
        while index<len(self.edgelist):
            self.table2.setItem(index,0,QtWidgets.QTableWidgetItem(str(self.edgelist[index][0])+"---->"+str(self.edgelist[index][2])+"---->"+str(self.edgelist[index][1])))
            index += 1

    def agregarAristas(self):
        if str(self.condTxt.text())!="":
            if int(self.origen) > -1:
                if self.workspace.salidas(str(self.condTxt.text()), int(self.origen))==False:
                    if int(self.origen) > -1 and int(self.destino) == -1:
                        self.destino = self.origen
                    if self.origenFlag:
                        if str(self.condTxt.text())!="":
                            self.edgelist.append((int(self.origen),int(self.destino),str(self.condTxt.text())))
                            self.workspace.agregarConexion(int(self.origen),int(self.destino),str(self.condTxt.text()))
                            self.origenFlag = False
                            self.destinoFlag = False
                            self.actualizarLista2()
                            self.drawing()
                            self.condTxt.setText("")
                            self.origen = "-1"
                            self.destino = "-1"
                        else:
                            self.MesVacio()
                else:
                    self.CondicionEnUso(self.workspace.salidas(str(self.condTxt.text()), int(self.origen))[1])
            else:
                self.seleccione()
        else:
            self.MesVacio()

    def origenDestino(self):
        if self.origenFlag==False:
            self.origen = (str(self.table1.currentItem().text()).split("Nodo "))[1]
            self.origenFlag=True
            return
        if self.destinoFlag==False:
            self.destino = (str(self.table1.currentItem().text()).split("Nodo "))[1]
            self.destinoFlag=True

    def sayHello(self):
        print("Hello")

    def setOrigen(self):
        self.origenNodo = int((str(self.table1.currentItem().text()).split("Nodo "))[1])
        print(self.origenNodo)
        self.drawing()

    def addDestino(self):
        self.destinoNodos.append(int((str(self.table1.currentItem().text()).split("Nodo "))[1]))
        print(self.destinoNodos)
        self.workspace.actuaAcep(self.destinoNodos)
        self.drawing()

    def MesVacio(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Condicion Vacia")
        msg.setInformativeText("Debe introducir una condicion")
        msg.setWindowTitle("Informacion")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()
        retval = msg.exec_()

    def EntradaInvalida(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Entrada Invalida. Use el alfabeto"+self.workspace.tipoAlfabeto)
        msg.setWindowTitle("Informacion")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()
        retval = msg.exec_()

    def CondicionEnUso(self,condi):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Condicion en uso,"+str(condi))
        msg.setWindowTitle("Informacion")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()
        retval = msg.exec_()

    def seleccione(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Primero selecciones nodos")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setWindowTitle("Informacion")
        msg.show()
        retval = msg.exec_()

    def Correcto(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Entrada Correcta")
        msg.setWindowTitle("Informacion")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()
        retval = msg.exec_()

    def Incorrecto(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Entrada Incorrecta")
        msg.setWindowTitle("Informacion")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()
        retval = msg.exec_()

    def borrarNodo(self):
        row = self.table1.currentRow()
        numNodo = int((str(self.table1.currentItem().text()).split("Nodo "))[1])
        for elemento in self.nodelist:
            if elemento.num == numNodo:
                self.nodelist.remove(elemento)
                self.workspace.eliminarEstado(numNodo)
                self.table1.removeRow(row)
                if self.origenNodo == numNodo:
                    self.origenNodo = -1
        for elemento in self.destinoNodos:
            if elemento == numNodo:
                self.destinoNodos.remove(elemento)
        for elemento in self.edgelist:
            if elemento[0]==numNodo or elemento[1]==numNodo:
                self.edgelist.remove(elemento)
        self.actualizarLista2()
        self.drawing()

    def borrarEdge(self):
        origen = int((str(self.table2.currentItem().text()).split("---->"))[0])
        destino = int((str(self.table2.currentItem().text()).split("---->"))[2])
        for elemento in self.edgelist:
            if int(elemento[0]) == origen and int(elemento[1]) == destino:
                self.edgelist.remove(elemento)
                self.workspace.eliminarConexion(origen,destino)
        self.actualizarLista2()
        self.drawing()

    def cambiarAlfabetico(self):
        self.workspace.setAlfabeto("Alfabetico")
        self.edgelist = []
        self.actualizarLista2()
        self.drawing()

    def cambiarAlfanumerico(self):
        self.workspace.setAlfabeto("Alfanumerico")
        self.edgelist = []
        self.actualizarLista2()
        self.drawing()

    def cambiarNumerico(self):
        self.workspace.setAlfabeto("Numerico")
        self.edgelist = []
        self.actualizarLista2()
        self.drawing()

    def cambiarCorreo(self):
        self.workspace.setAlfabeto("Correo")
        self.edgelist = []
        self.actualizarLista2()
        self.drawing()

    def cambiarBinario(self):
        self.workspace.setAlfabeto("Binario")
        self.edgelist = []
        self.actualizarLista2()
        self.drawing()


    def Evaluacion(self):
        if self.workspace.comprobarEntrada(str(self.inputTxt.text())):
            inicio = self.origenNodo
            cadena = str(self.inputTxt.text())
            self.workspace.imprimirEstados()
            self.workspace.imprimirConexiones()
            setEvalua = self.workspace.evaluar(inicio,cadena)
            if self.workspace.caimosBien(setEvalua):
                self.Correcto()
            else:
                self.Incorrecto()
        else:
            self.EntradaInvalida()

    def sincronizar(self):
        self.edgelist = []
        self.nodelist = []
        for estado in self.workspace.estados:
            nodo = Node(self.graphicsView,estado.ID)
            nodo.setPos(self.x,self.y)
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(15)
            line = QtWidgets.QLabel(str(estado.ID))
            line.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            line.setFont(font)
            prox = QtWidgets.QGraphicsProxyWidget(nodo)
            prox.setWidget(line)
            self.nodelist.append(nodo)
            self.x = self.x + 50
            self.y = self.y + 50
            self.countNodes = self.countNodes + 1
        self.actualizarLista1()
        for conexion in self.workspace.conexiones:
            self.edgelist.append((conexion.origen,conexion.destino,conexion.condicion))
        self.actualizarLista2()
        self.workspace.imprimirEstados()
        self.drawing()
