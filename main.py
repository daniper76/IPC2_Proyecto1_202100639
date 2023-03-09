from colorama import Fore, Back, Style
from Cola import Cola
from LecturaArchivo import LecturaXML
from ColaMuestras import ColaMuestras
from Graficador import Graficar

bandera=True
while bandera:
    print(Fore.MAGENTA+'-------------Menu-------------')
    print(Fore.GREEN+'A continuacion se muestran las opciones del programa')
    print(Fore.CYAN+'1. Cargar el archivo xml')
    print(Fore.CYAN+'2. Mostrar la imagen de las muestras')
    print(Fore.CYAN+'5. Salir del programa')

    opcion=input(Fore.YELLOW+'Ingrese una opcion: ')
    print(opcion)

    if opcion=='1':
        archivo=input(Fore.BLUE+'Ingrese la direccion del archivo xml del archivo xml: ')
        lista_organismos=Cola()
        LecturaXML(lista_organismos,archivo)     
    elif opcion=='2':
        largo_tablero=input(Fore.BLUE+'Ingrese el tamaño horizontal del tablero: ')
        ancho_tablero=input(Fore.BLUE+'Ingrese el tamaño vertical del tablero: ')
        Graficar(lista_organismos.CrearListaInicial(),int(largo_tablero),int(ancho_tablero))
    elif opcion=="5":
        bandera=False
    
    else:
        print("opcion invalida :/")

