import json

class ControladorJson:
    def cargarJson(self,ruta):
        print('///////////////////////CARGANDO ARCHIVO JSON///////////////////////')
        with open(ruta) as contenido:
            productos = json.load(contenido)
            for producto in productos:
                print("Nombre:%s "%producto.get('Nombre'))
                print("ID Producto:%s "%producto.get('ID_Producto'))
                print("Precio:%s "%producto.get('Precio'))
                print("Cantidad:%s "%producto.get('Cantidad'))
                print('///////////////////////////////////////////////////////////////////')
            print(f'Tipo de archivos cargados: {type(producto)}')