import marshal

def guardarAutomata(name,objeto):
    archivo = open("Maquinas Guardadas/"+name+".tc","wb")
    marshal.dump(objeto,archivo)
    archivo.close()

def cargarAutomata(name):
    archivo = open("Maquinas Guardadas/"+name+".tc","rb")
    objeto = marshal.load(archivo)
    archivo.close()
    return objeto
