import xml.etree.ElementTree as ET

tree=ET.parse('archivo.xml')
#Acceder a valores de atributos
root=tree.getroot()

#Obtención del nombre del organismo
x1=root[0][0][1]