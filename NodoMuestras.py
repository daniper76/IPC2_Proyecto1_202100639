from Muestras import*

class NodoMuestras:

    def __init__(self,fila,columna,codigo_organismo,color_organismo="nothing"):
        self.muestra=Muestra(fila,columna,codigo_organismo,color_organismo)
        self.Siguiente = None

    def ObtenerFila(self):
        return self.muestra.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.muestra.ObtenerColumna()
    
    def ObtenerCodigoOrganismo(self):
        return self.muestra.ObtenerCodigoOrganismo()
    
    def ObtenerColorOrganismo(self):
        return self.muestra.ObtenerColorOrganismo()