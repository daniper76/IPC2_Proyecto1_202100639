from Organismo import*

class Nodo:

    def __init__(self,nombre,codigo):
        self.Orga =Organismo(nombre,codigo)
        self.Siguiente = None

    def ObtenerNombre(self):
        return self.Orga.ObtenerNombre()
    
    def ObtenerCodigo(self):
        return self.Orga.ObtenerCodigo()
    
    def ObtenerColor(self):
        return self.Orga.ObtenerColor()
    
    def ObtenerPosicionOrganismos(self):
        return self.Orga.ObtenerPosicionOrganismos()
    