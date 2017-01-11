#Programa que lee un XML y muestra en consola el resultado


#Importar un XML
import xml.etree.ElementTree as ET
tree = ET.parse("menu.xml")
root = tree.getroot()



#Caso Test

#Mostrar los 5 platos:

contador = 0
#for child in root:
#    print(root[contador][0].text + " | "+root[contador][1].text)
#    contador +=1

#Insertar en diccionario, mostrando el resultado
menu = {}

for child in root:
    menu[root[contador][0].text] = root[contador][1].text
    contador +=1
print(menu)



