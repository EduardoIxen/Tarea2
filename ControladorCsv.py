import csv

class ControladorCsv:
    def cargarCsv(self,ruta):
        with open(ruta) as cargarDatos:
            animales = csv.reader(cargarDatos, delimiter=",")
            print('///////////////////////CARGANDO ARCHIVO CSV////////////////////////')
            for animal in animales:
                print(f"Tipo Animal: {animal[0]}")
                print(f"    Ejemplo1: {animal[1]}")
                print(f"    Ejemplo2: {animal[2]}")
                print(f"    Ejemplo3: {animal[3]}")
                print('///////////////////////////////////////////////////////////////////')
            print(f'Tipo de archivo cargado: {type(animal)}')