class Alfabeto:
    def __init__(self):
        self.Caracteres = []

    def cargar(self,tipo):
        self.Caracteres = []
        archivo = open("Alfabetos/"+tipo+".txt")
        linea=archivo.readline().rstrip('\n')
        while linea != '':
            self.Caracteres.append(str(linea))
            linea=archivo.readline().rstrip('\n')
