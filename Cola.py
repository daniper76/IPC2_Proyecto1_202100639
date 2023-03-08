from NodoOrg import Nodo

class Cola:

    def __init__(self):
        self.Cabeza = None
        self.Cola = None

    def Insertar(self,nombre,codigo):
        NuevoNodo = Nodo(nombre,codigo)
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Cola = NuevoNodo
        else: 
            self.Cola.Siguiente = NuevoNodo
            self.Cola = NuevoNodo

    def Imprimir(self):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            print("Nombre: " + str(Auxiliar.ObtenerNombre()))
            print("Código: "+ str(Auxiliar.ObtenerCodigo()))
            print("Color:"+str(Auxiliar.ObtenerColor()))
            Auxiliar = Auxiliar.Siguiente

    def IngresarPosicionesOrganismos(self,fila,columna,codigo_organismo):
        Auxiliar=self.Cabeza
        while Auxiliar != None:
            if Auxiliar.ObtenerCodigo()==codigo_organismo:
                Auxiliar.ObtenerPosicionOrganismos().Insertar(fila,columna,codigo_organismo)
            Auxiliar=Auxiliar.Siguiente

    def DeterminarTamanoTablero(self,tamano_horizontal,tamano_vertical):
        self.tamano_horizontal = tamano_horizontal
        self.tamano_vertical = tamano_vertical
