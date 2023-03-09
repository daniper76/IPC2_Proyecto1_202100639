from NodoOrg import Nodo
from ColaMuestras import ColaMuestras

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

    def CrearListaInicial(self):
        Auxiliar=self.Cabeza
        ListaInicial=ColaMuestras()
        while Auxiliar != None:
            ListaInicial.LlenarFase2(Auxiliar.ObtenerPosicionOrganismos().LlenarFase1(Auxiliar.ObtenerColor()))
            Auxiliar=Auxiliar.Siguiente
        return ListaInicial


