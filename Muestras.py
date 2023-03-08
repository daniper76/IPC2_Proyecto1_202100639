
class Muestra:
    
    def __init__ (self,fila,columna,codigo_organismo):
        self.fila=fila
        self.columna =columna
        self.codigo_organismo=codigo_organismo


    def ObtenerFila(self):
        return self.fila
    
    def ObtenerColumna(self):
        return self.columna
    
    def ObtenerCodigoOrganismo(self):
        return self.codigo_organismo