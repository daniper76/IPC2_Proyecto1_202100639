from NodoMuestras import NodoMuestras

class ColaMuestras:

    def __init__(self):
        self.Cabeza = None
        self.Cola = None

    def Insertar(self,fila,columna,codigo_organismo):
        NuevoNodo = NodoMuestras(fila,columna,codigo_organismo)
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Cola = NuevoNodo
        else: 
            self.Cola.Siguiente = NuevoNodo
            self.Cola = NuevoNodo

    def Imprimir(self):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            print("Fila: " + str(Auxiliar.ObtenerFila()))
            print("Columna: "+ str(Auxiliar.ObtenerColumna()))
            print("Codigo Organismo:"+str(Auxiliar.ObtenerCodigoOrganismo()))
            Auxiliar = Auxiliar.Siguiente
