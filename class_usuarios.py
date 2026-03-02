import class_biblioteca
#import os
import subprocess

class Usuario:
    def __init__(self, nombre, contraseña, libros_tenidos=None):
        self.nombre = nombre
        self.contraseña = contraseña
        if libros_tenidos is None:
            self.libros_tenidos = []
        else:
            self.libros_tenidos = libros_tenidos
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "contraseña": self.contraseña,
            "libros_tenidos": self.libros_tenidos
        }

#######

def validar_usuario(nombre_usuario, usuario_contraseña):
    usuarios = class_biblioteca.cargar_usuarios()
    for usuario in usuarios:
        if nombre_usuario == usuario["nombre"] and usuario_contraseña == usuario["contraseña"]:
            return usuario

    return None


def ver_libros_tenidos(usuario): #(usuario_valido)
    usuarioz = class_biblioteca.cargar_usuarios()
    for uz in usuarioz:
        if uz["id"] == usuario["id"]:
            for lt in uz["libros_tenidos"]:
                print(lt)



def leer(usuario, id_libro_tenido): #(usuario_valido, id_libro_tenido):
    for libro in usuario["libros_tenidos"]:
        if int(libro["id"]) == int(id_libro_tenido):
            ruta = libro["contenido"]
            try:
                #os.startfile(ruta)
                subprocess.run(f'start "" /MAX "{ruta}"', shell=True, check=True)  # Esto es para abrir el archivo en Windows
                  # Esto abrirá el archivo con la aplicación predeterminada en Windows
               # with open(ruta, "r", encoding="utf-8") as archivo:
                #    for linea in archivo:
                 #       print(linea.strip())
            except FileNotFoundError:
                print("El archivo no existe.")
            return

    print("Libro no encontrado")



def pedir_prestado(usuario, id_libro):  #(usuario_valido, id_libro):

    id_usu = usuario["id"]
    
    libros = class_biblioteca.cargar_libros()
    for libro in libros:
        if libro["id"] == id_libro:
            libro["prestado"] = True
            libr_a = libro
            break
    
    usuarioz = class_biblioteca.cargar_usuarios()
    for usu in usuarioz: 
        if usu["id"] == id_usu:  
            usu["libros_tenidos"].append(libr_a)    
            break
    # Dentro de pedir_prestado(), después de añadir el libro al JSON: X
    usuario["libros_tenidos"].append(libr_a)

    class_biblioteca.guardar_libros(libros)
    class_biblioteca.guardar_usuarios(usuarioz)
    
    return



def devolver_libro(usuario, id_libro): #(usuario_valido, id_libro):
    id_usu = usuario["id"]
    
    usuarios = class_biblioteca.cargar_usuarios()

    for usu in usuarios: 
        if usu["id"] == id_usu:  
            usu["libros_tenidos"] = [libro for libro in usu["libros_tenidos"] if libro["id"] != id_libro]
            break
    class_biblioteca.guardar_usuarios(usuarios)

    libros = class_biblioteca.cargar_libros()
    for libro in libros:
        if libro["id"] == id_libro:
            libro["prestado"] = False
            break

    class_biblioteca.guardar_libros(libros)

########################################################################################################
#      FUNCIONES PARA LA INTERFAZ DE USUARIOS  X
 

#def ver_libros_tenidos():
    #pass

def validar_id_usuario(id_usuario):
    usuarios = class_biblioteca.cargar_usuarios()
    for usuario in usuarios:
        if int(usuario["id"]) == int(id_usuario):
            return True

    return False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   el objeto usuario1 creado

usuario1 = Usuario("sneijder", "123contraseña")

