class Fondo:
    def __init__(self, fila, columna, color, borde):
        self.fila=fila
        self.columna=columna
        self.color=color
        self.borde=borde

    def ObtenerFila(self):
        return self.fila
    
    def ObtenerColumna(self):
        return self.columna
    
    def ObtenerColor(self):
        return self.color
    
    def ObtenerBorde(self):
        return self.borde
    
    def ModificarFila(self, fila):
        self.fila = fila
    
    def ModificarColumna(self, columna):
        self.columna = columna
    
    def ModificarColor(self, color):
        self.color = color

    def ModificarBorde(self, borde):
        self.borde = borde