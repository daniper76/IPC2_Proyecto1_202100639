from xml.dom import minidom

def LecturaXML(lista_organismo,archivo):

    doc = minidom.parse(str(archivo))

    print("-------- Leyendo documento --------")

    datos_marte=doc.getElementsByTagName("datosMarte")

    for dato_marte in datos_marte:

        archivo_organismos= dato_marte.getElementsByTagName("listaOrganismos")
        
        for listado_organismo in archivo_organismos:
        
            organismos = listado_organismo.getElementsByTagName("organismo")

            for organismo in organismos:
                nombre = organismo.getElementsByTagName("nombre")
                codigo = organismo.getElementsByTagName("codigo")
                
                nombre_organismo = str(nombre[0].firstChild.nodeValue)
                codigo_organismo = str(codigo[0].firstChild.nodeValue)
                print("Nombre: " + str(nombre_organismo))
                print("Código: "+ str(codigo_organismo))
                lista_organismo.Insertar(nombre_organismo,codigo_organismo)
            
        archivo_muestras=dato_marte.getElementsByTagName("listadoMuestras")
        
        for listado_muestras in archivo_muestras:

            muestras=listado_muestras.getElementsByTagName("muestra")

            for muestra in muestras:
                archivo_celda_vivas=muestra.getElementsByTagName("listadoCeldasVivas")

                for celdaVivas in archivo_celda_vivas:
                    celdaViva=celdaVivas.getElementsByTagName("celdaViva")
                    
                    for posicion in celdaViva:
                        fila = posicion.getElementsByTagName("fila")
                        columna = posicion.getElementsByTagName("columna")
                        codigoOrganismo=posicion.getElementsByTagName("codigoOrganismo")

                        fila_organismo = int(fila[0].firstChild.nodeValue)
                        columna_organismo = int(columna[0].firstChild.nodeValue)
                        codigoOrganismo_organismo = str(codigoOrganismo[0].firstChild.nodeValue)

                        print("Fila:"+str(fila_organismo))
                        print("Columan:"+str(columna_organismo))
                        print("Codigo del Organismo:"+str(codigoOrganismo_organismo))

                        lista_organismo.IngresarPosicionesOrganismos(int(fila_organismo),int(columna_organismo),str(codigoOrganismo_organismo))






