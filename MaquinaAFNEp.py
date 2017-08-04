from Conexion import Conexion
from Estado import Estado
from Alfabeto import Alfabeto

class Epsilon:
    def __init__(self,nom,tip):
        self.nombre = nom
        self.tipoAlfabeto = tip
        self.conexiones = []
        self.estados = []
        self.Alfabeto = Alfabeto()
        self.Alfabeto.cargar(self.tipoAlfabeto)
        self.Inicio = None

    def setNombre(self,nom):
        self.nombre = nom

    def setAlfabeto(self,tipo):
        self.tipoAlfabeto = tipo
        self.Alfabeto.cargar(tipo)

    def actuaAcep(self,lista):
        for elemento in self.estados:
            elemento.aceptacion = False

        for elemento in lista:
            for estado in self.estados:
                if estado.ID == elemento:
                    estado.aceptacion = True

    def reinicion(self):
        self.nombre = ""
        self.tipoAlfabeto=""
        self.conexiones = []
        self.estados = []
        self.Alfabeto = Alfabeto()
        self.Inicio = None

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

    def clausula(self,nodo,setNodo):
        setNodo.add(nodo)
        for elemento in self.misConexiones(nodo,"$"):
            setNodo | self.clausula(elemento,setNodo)
        return setNodo

    def unirClausulas(self,setNodos):
        setSecundario = set()
        for elemento in setNodos:
            setSecundario = setSecundario | self.clausula(elemento,setNodo=set())
        return setSecundario

    def evaluar(self, inicio, cadena):
        setInicial = self.clausula(inicio,setNodo=)




maquina = Epsilon("Hola","Binario")
maquina.agregarEstado(0,False)
maquina.agregarEstado(1,False)
maquina.agregarEstado(2,False)
maquina.agregarEstado(3,False)
maquina.agregarConexion(0,1,"$")
maquina.agregarConexion(1,2,"$")
maquina.agregarConexion(2,3,"$")
maquina.agregarEstado(4,False)
maquina.agregarConexion(2,4,"1")
maquina.agregarConexion(3,4,"$")
maquina.agregarEstado(5,False)
maquina.agregarConexion(4,5,"0")

print(maquina.misConexiones(0,"$"))
clau = maquina.clausula(0,setNodo=set())
print(maquina.unirClausulas(clau))

