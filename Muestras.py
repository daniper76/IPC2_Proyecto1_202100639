
class Muestra:
    
    def __init__ (self,fila,columna,codigo_organismo,color_organismo="nothing"):
        self.fila=fila
        self.columna =columna
        self.codigo_organismo=codigo_organismo
        self.color_organismo=color_organismo


    def ObtenerFila(self):
        return self.fila
    
    def ObtenerColumna(self):
        return self.columna
    
    def ObtenerCodigoOrganismo(self):
        return self.codigo_organismo
    
    def ObtenerColorOrganismo(self):
        return self.color_organismo