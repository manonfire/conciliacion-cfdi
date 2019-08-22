'''
 Lee archivos XML y los datos los pasa a un archivo de lectura facil
 Version 1
 Autor: jorge Aguayo
 Fecha ultima revision: 2019/08/02
'''

# Esta libreria sirve para leer archvos
import glob
# Esta libreria es para leer xml
import xml.etree.ElementTree as ET


# Prueba para aprender a usar python
print("Primer prueba para leer xml")

# lee los archivos del folder especificado
# archivosxml = glob.glob("/Users/jorgeaguayo/Documents/Desarrollo/ConciliacionCFDI/conciliacion-cfdi/_xmlFiles/*.xml")
archivosxml = glob.glob("_xmlFiles/*.xml")


# for archivo in archivosxml:
#    aqui debe de leer cada arcxhivo xml que se le va dando y lo sube a un archivo de texto con el extracto
#  print(archivo)


tree = ET.parse('_xmlFiles/ade02b7b-e629-4dbb-a0e6-e17d9de74980@1000000000XX0.xml')
root = tree.getroot()

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)


# one specific item's data
print('\nDirecto:')
print(root[0].attrib)

print('\nDirecto2:')

for emisor in root.iter('cfdi:Emisor'):
    print(emisor.attrib)

