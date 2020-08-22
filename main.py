from ControladorJson import *
from ControladorXml import *
from ControladorCsv import *

opcion = 0
while(opcion != 4):
    print("\n"
          "////////////////////////////////// MENU ///////////////////////////")
    print("1. Cargar archivo JSON")
    print("2. Cargar archivo XML")
    print("3. Cargar archivo CSV")
    print("4. Salir")
    opcion = int (input("Ingrese la opcion deseada\n"))
    if (opcion == 1):
        ruta = 'scripts/Productos.json'
        controladorJson = ControladorJson()
        controladorJson.cargarJson(ruta)
        print()
    elif opcion == 2:
        ruta2 = 'scripts/Usuarios.xml'
        controladorXml = ControladorXml()
        controladorXml.cargarXml(ruta2)
        print()
    elif opcion == 3:
        ruta3 = 'scripts/Animales.csv'
        controladorCsv = ControladorCsv()
        controladorCsv.cargarCsv(ruta3)
    elif opcion == 4:
        print("Saliendo...")