from prueba import Prueba

class lista_simple():
    
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def esta_vacia(self):
        return self.primero==None

    def agregar_primero(self):
        nuevo=Prueba(self)

        if self.esta_vacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp
            
    def agregar_ultimo(self):
        nuevo=Prueba(self)

        if self.esta_vacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=self.primero
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevo
            self.ultimo=nuevo
    
    def recorrer(self):
        temp=self.primero
        while temp.siguiente is not None:
            print("")
            temp=temp.siguiente

    
