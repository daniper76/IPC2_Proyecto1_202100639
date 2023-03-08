import random
from ColaMuestras import ColaMuestras
class Organismo:
    
    def __init__ (self,nombre,codigo):
        self.a = random.randrange(256)
        self.b = random.randrange(256)
        self.c = random.randrange(256)
        self.nombre=nombre
        self.codigo = codigo
        self.color='#{0:02x}{1:02x}{2:02x}'.format(self.a,self.b,self.c)
        self.listaDeOrganismos=ColaMuestras()

    def ObtenerNombre(self):
        return self.nombre
    
    def ObtenerCodigo(self):
        return self.codigo
    
    def ObtenerColor(self):
        return self.color
    
    def ObtenerPosicionOrganismos(self):
        return self.listaDeOrganismos
    


