from NodoColor import NodoColor
class ColaGrafica:

    def __init__(self, tamano_horizontal,tamano_vertical):
        self.tamano_horizontal=tamano_horizontal
        self.tamano_vertical=tamano_vertical
        self.Cabeza = None
        self.Cola = None

    def Insertar(self,fila,columna,color,borde):
        NuevoNodo = NodoColor(fila,columna,color,borde)
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Cola = NuevoNodo
        else:
            Auxiliar = self.Cabeza
            while Auxiliar != None:
                if Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna:
                    
                    if color != 'White':
                        Auxiliar.ModificarColor(color)
                    if Auxiliar.ObtenerBorde() == 'Black':
                        
                        Auxiliar.ModificarBorde(borde)
                    return
                Auxiliar = Auxiliar.Siguiente
            self.Cola.Siguiente = NuevoNodo
            self.Cola = NuevoNodo

    def GenerarDibujo(self):
        Texto = "digraph {\n"
        Texto = Texto + "\ttbl [\n"
        Texto = Texto + "\t\tshape=plaintext\n"
        Texto = Texto + "\t\tlabel=<\n"
        Texto = Texto + "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        ContFilaVacia = 0
        for i in range(self.tamano_vertical):
            ListaFila = self.ObtenerTodaLaFila(i)
            if ListaFila.Cabeza != None:
                if ContFilaVacia > 0:
                    Texto = Texto + "\t\t\t\t<tr>\n"
                    Texto = Texto + "\t\t\t\t\t<td colspan='"+str(self.tamano_horizontal)+"'>...</td>\n"
                    Texto = Texto + "\t\t\t\t</tr>\n"
                ContFilaVacia = 0
                Texto = Texto + "\t\t\t\t<tr>\n"
                ContColumnaVacia = 0
                for j in range(self.tamano_horizontal):
                    Auxilar = ListaFila.ObtenerEnColumna(j)
                    if Auxilar != None:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        ContColumnaVacia = 0
                        if Auxilar.ObtenerBorde() == 'Black':
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='"+str(Auxilar.ObtenerColor())+"'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='"+str(Auxilar.ObtenerColor())+"'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>"+str(Auxilar.ObtenerFila())+","+str(Auxilar.ObtenerColumna())+"</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        
                            
                    else:
                        ContColumnaVacia = ContColumnaVacia + 1
                    if j+1 == self.tamano_horizontal:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                Texto = Texto + "\t\t\t\t</tr>\n"
            else:
                ContFilaVacia = ContFilaVacia + 1
                if i + 1 == self.tamano_vertical:
                    if ContFilaVacia > 0:
                        Texto = Texto + "\t\t\t\t<tr>\n"
                        Texto = Texto + "\t\t\t\t\t<td colspan='"+str(self.tamano_horizontal)+"'>...</td>\n"
                        Texto = Texto + "\t\t\t\t</tr>\n"
        Texto = Texto + "\t\t\t</table>\n"
        Texto = Texto + "\t\t>];\n"
        Texto = Texto + "}\n"
        Destino = open('Dibujo.dot', 'w')
        Destino.write(Texto)
        Destino.close()
    
    def ObtenerTodaLaFila(self, Fila):
        ListaFila = ColaGrafica(self.tamano_vertical, self.tamano_horizontal)
        Aux = self.Cabeza
        while Aux != None:
            if Aux.ObtenerFila() == Fila:
                ListaFila.Insertar(Aux.ObtenerFila(), Aux.ObtenerColumna(), Aux.ObtenerColor(), Aux.ObtenerBorde())
            Aux = Aux.Siguiente
        return ListaFila
    
    def ObtenerEnColumna(self, Columna):
        Aux = self.Cabeza
        while Aux != None:
            if Aux.ObtenerColumna() == Columna:
                return Aux
            Aux = Aux.Siguiente
        return None