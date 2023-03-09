from ColorOrganismo import *

class NodoColor:

    def __init__(self,fila,columna,color,borde):
        self.Fondo =Fondo(fila,columna,color,borde)
        self.Siguiente = None

    def ObtenerFila(self):
        return self.Fondo.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.Fondo.ObtenerColumna()
    
    def ObtenerColor(self):
        return self.Fondo.ObtenerColor()
    
    def ObtenerBorde(self):
        return self.Fondo.ObtenerBorde()
    
    def ModificarFila(self, fila):
        self.Fondo.ModificarFila(fila)
    
    def ModificarColumna(self, columna):
        self.Fondo.ModificarColumna(columna)
    
    def ModificarColor(self, color):
        self.Fondo.ModificarColor(color)

    def ModificarBorde(self, borde):
        self.Fondo.ModificarBorde(borde)
