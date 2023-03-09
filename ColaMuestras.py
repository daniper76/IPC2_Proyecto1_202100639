from NodoMuestras import NodoMuestras

class ColaMuestras:

    def __init__(self):
        self.Cabeza = None
        self.Cola = None

    def Insertar(self,fila,columna,codigo_organismo,color_organismo="nothing"):
        NuevoNodo = NodoMuestras(fila,columna,codigo_organismo,color_organismo)
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

    def DeterminarTamanoTablero(self,tamano_horizontal,tamano_vertical):
        self.tamano_horizontal = tamano_horizontal
        self.tamano_vertical = tamano_vertical
    
    def LlenarFase1(self,color_orga):
        Auxiliar=self.Cabeza
        Fase1=ColaMuestras()
        color=color_orga
        while Auxiliar != None:
            Fase1.Insertar(Auxiliar.ObtenerFila(),Auxiliar.ObtenerColumna(),Auxiliar.ObtenerCodigoOrganismo(),color)
            Auxiliar=Auxiliar.Siguiente
        
        return Fase1
    
    def LlenarFase2(self,lista_fase1):
        Auxiliar=lista_fase1.Cabeza
        while Auxiliar != None:
            self.Insertar(Auxiliar.ObtenerFila(),Auxiliar.ObtenerColumna(),Auxiliar.ObtenerCodigoOrganismo(),Auxiliar.ObtenerColorOrganismo())
            Auxiliar=Auxiliar.Siguiente
    
    def BuscarPosicion(self,fila,columna):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            if (int(Auxiliar.ObtenerFila()) == int(fila) and int(Auxiliar.ObtenerColumna()) == int(columna)):
                return True
            Auxiliar = Auxiliar.Siguiente
        return False
    
    def ObtenerColorOrganismos(self):
        Auxiliar=self.Cabeza
        pintar_color=Auxiliar.ObtenerColorOrganismo()
        return pintar_color
    
    def BuscarColor(self,fila,columna):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            if (int(Auxiliar.ObtenerFila()) == int(fila) and int(Auxiliar.ObtenerColumna()) == int(columna)):
                colorama=Auxiliar.ObtenerColorOrganismo()
            Auxiliar=Auxiliar.Siguiente
        return colorama


        