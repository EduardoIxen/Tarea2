from xml.dom import minidom
class ControladorXml:
    def cargarXml(self,ruta):
        print('///////////////////////CARGANDO ARCHIVO XML////////////////////////')
        cargarDatos = minidom.parse(ruta)
        usuarios = cargarDatos.getElementsByTagName("usuario")

        for usuario in usuarios:
            id = usuario.getAttribute("id")
            nombre = usuario.getElementsByTagName("nombre")[0]
            apellido = usuario.getElementsByTagName("apellido")[0]
            nombreUsuario = usuario.getElementsByTagName("nombreUsuario")[0]
            contrasenia = usuario.getElementsByTagName("contrasenia")[0]
            print("ID:%s " % id)
            print("Nombre:%s " % nombre.firstChild.data)
            print("Apellido:%s " % apellido.firstChild.data)
            print("Nombre de Usuario:%s " % nombreUsuario.firstChild.data)
            print("Contrasenia:%s " % contrasenia.firstChild.data)
            print('///////////////////////////////////////////////////////////////////')
        print(f'Tipo de archivos cargados: {type(usuario)}')
