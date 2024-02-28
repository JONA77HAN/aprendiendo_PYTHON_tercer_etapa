import os

archivo = open('hola.txt')
archivoContenido = archivo.read()
archivo.close()

print(archivoContenido)