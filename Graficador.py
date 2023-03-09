from ColaGrafica import ColaGrafica
import subprocess

def Graficar(lista_posicion_organismos,tamano_horizontal_orga,tamano_vertical_orga):
    tamano_horizontal = tamano_horizontal_orga
    tamano_vertical=tamano_vertical_orga

    lista_inicial = ColaGrafica(tamano_horizontal,tamano_vertical)
    for filas in range(tamano_vertical):
        for columnas in range(tamano_horizontal):
            if lista_posicion_organismos.BuscarPosicion(filas,columnas):
                if columnas-1 >= 0 and filas-1 >= 0:
                    lista_inicial.Insertar(columnas-1, filas-1, 'White', 'Black')
                if filas-1 >= 0:
                    lista_inicial.Insertar(columnas, filas-1, 'White', 'Black')
                if filas-1 >= 0 and columnas+1 < tamano_horizontal:
                    lista_inicial.Insertar(columnas+1, filas-1, 'White', 'Black')
                if columnas-1 >= 0:
                    lista_inicial.Insertar(columnas-1, filas, 'White', 'Black')
                
                lista_inicial.Insertar(filas,columnas,lista_posicion_organismos.BuscarColor(filas,columnas), 'Black')

                if columnas+1 < tamano_horizontal:
                    lista_inicial.Insertar(columnas+1, filas, 'White', 'Black')
                if filas+1 < tamano_vertical and columnas-1 >= 0:
                    lista_inicial.Insertar(columnas-1, filas+1, 'White', 'Black')
                if filas+1 < tamano_vertical:
                    lista_inicial.Insertar(columnas, filas+1, 'White', 'Black')
                if filas+1 < tamano_vertical and columnas+1 < tamano_horizontal:
                    lista_inicial.Insertar(columnas+1, filas+1, 'White', 'Black')
    
    lista_inicial.GenerarDibujo()
    cmd_str = "dot -Tsvg -O Dibujo.dot"
    subprocess.run(cmd_str, shell=True)