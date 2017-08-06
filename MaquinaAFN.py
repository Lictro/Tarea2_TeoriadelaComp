from Conexion import Conexion
from Estado import Estado
from Alfabeto import Alfabeto

class AFN:
    def __init__(self):
        self.conexiones = []
        self.estados = []

    def actuaAcep(self,lista):
        con = 0
        print(lista)
        while con>len(self.estados):
            self.estados[con]=False
            con = con + 1

        for elementos in lista:
            con = 0
            while con>len(self.estados):
                if con == elementos:
                    self.getEstado(elementos)
                con = con + 1
        self.imprimirEstados()

    def reinicio(self):
        self.conexiones = []
        self.estados = []

    def agregarConexion(self,Origen,Destino,Condicion):
        self.conexiones.append(Conexion(Condicion,Origen,Destino))

    def eliminarConexion(self,origen,destino):
        cursor = 0
        while cursor < len(self.conexiones):
            if self.conexiones[cursor].origen == origen and self.conexiones[cursor].destino == destino:
                self.conexiones.__delitem__(cursor)
                break
            cursor = cursor + 1

    def agregarEstado(self,pId,pAcepta):
        if len(self.estados) == 0:
            self.Inicio = Estado(pId,pAcepta)
        self.estados.append(Estado(pId,pAcepta))

    def eliminarEstado(self,pId):
        cursor = 0
        while cursor < len(self.estados):
            if self.estados[cursor].ID == pId:
                self.estados.__delitem__(cursor)
                break
            cursor = cursor + 1

    def estadoEnUso(self,pId):
        for elemento in self.conexiones:
            if elemento.origen == pId or elemento.destino == pId:
                return True
        return False

    def imprimirEstados(self):
        for elemento in self.estados:
            print(elemento.ID,"---",elemento.aceptacion)

    def getEstado(self,pId):
        for elemento in self.estados:
            if elemento.ID == pId:
                return elemento
        return None

    def cambiarAcepta(self,pId,pAce):
        self.estados[pId].aceptacion = pAce


    def imprimirConexiones(self):
        for elemento in self.conexiones:
            print(elemento.origen," -->", elemento.condicion,"--> ",elemento.destino)

    def getListaConexiones(self):
        lista = []
        for elemento in self.conexiones:
            lista.append(str(elemento.origen)+"--->"+elemento.condicion+"--->"+str(elemento.destino))
        return lista

    def evaluarCondicion(self,condicion,caracter):
        listaCond = condicion.split("/")
        for elemento in listaCond:
            if elemento == caracter:
                return True
        return False

    def buscarDestino(self,pOrigen,caracter):
        for elemento in self.conexiones:
            if elemento.origen == pOrigen and self.evaluarCondicion(elemento.condicion,caracter):
                return elemento.destino
        return pOrigen

    def comprobarEntrada(self,entrada):
        for caracter in entrada:
            flag = True
            for elemento in self.Alfabeto.Caracteres:
                if flag and str(caracter) == str(elemento):
                    flag = False
                    break
            if flag:
                return False
        return True

    def salidas(self,condicion,origen):
        return False

    def guardadito(self):
        arch = open("Maquinas Guardadas/"+self.nombre+".txt", "w")
        arch.write(self.nombre+"\n")
        arch.write(self.tipoAlfabeto+"\n")
        arch.write(str(len(self.estados))+"\n")
        for estado in self.estados:
            arch.write(str(estado.ID)+"\n")
            arch.write(str(estado.aceptacion)+"\n")
        arch.write(str(len(self.conexiones))+"\n")
        for conexion in self.conexiones:
            arch.write(str(conexion.origen)+"\n")
            arch.write(str(conexion.destino)+"\n")
            arch.write(str(conexion.condicion)+"\n")
        arch.close()

    def misConexiones(self,nodo,caracter):
        setNodos = set()
        for elemento in self.conexiones:
            if elemento.origen == nodo:
                if self.evaluarCondicion(elemento.condicion,caracter):
                    setNodos.add(elemento.destino)
        return setNodos

    def evaluar(self,inicio,cadena):
        setInicial = self.misConexiones(inicio,cadena[0])
        return self.evaluarP2(setInicial,cadena,1)

    def evaluarP2(self,setEstados,cadena,cursor):
        if len(cadena)>cursor:
            return self.evaluarP2(self.unirSets(setEstados, cadena[cursor]), cadena, cursor + 1)
        return setEstados

    def unirSets(self,setPrincipal,caracter):
        setSecundario = set()
        for elemento in setPrincipal:
            setSecundario = setSecundario | self.misConexiones(elemento,caracter)
        return setSecundario

    def caimosBien(self,setRespuesta):
        for elemento in setRespuesta:
            if self.getEstado(elemento).aceptacion:
                return True
        return False

    def guardar(self,nombre):
        arch = open("Maquinas/"+nombre+".txt", "w")
        arch.write(str(len(self.estados))+"\n")
        for estado in self.estados:
            arch.write(str(estado.ID)+"\n")
            arch.write(str(estado.aceptacion)+"\n")
        arch.write(str(len(self.conexiones))+"\n")
        for conexion in self.conexiones:
            arch.write(str(conexion.origen)+"\n")
            arch.write(str(conexion.destino)+"\n")
            arch.write(str(conexion.condicion)+"\n")
        arch.close()

    def cargar(self,nombre):
        self.conexiones = []
        self.estados = []
        archivo = open("Maquinas/"+nombre+".txt")
        cNodos = archivo.readline().rstrip('\n')
        con = 0
        while con < int(cNodos):
            id = archivo.readline().rstrip('\n')
            acep = archivo.readline().rstrip('\n')
            self.estados.append(Estado(int(id),acep))
            con = con + 1
        cConexiones = archivo.readline().rstrip('\n')
        con = 0
        while con < int(cConexiones):
            origen = archivo.readline().rstrip('\n')
            destino = archivo.readline().rstrip('\n')
            cond = archivo.readline().rstrip('\n')
            self.conexiones.append(Conexion(int(origen),int(destino),str(cond)))
            con = con + 1
