
import class_usuarios
import class_libros

import json
import os

Libros = [
    {"id": 1, "titulo": "Don_Quijote_de_la_Mancha", "autor": "Miguel de Cervantes", "genero": "Novela", "contenido": "Don_Quijote_de_la_Mancha.txt", "prestado": False},
    {"id": 2, "titulo": "La_Divina_Comedia", "autor": "Dante Alighieri", "genero": "Poesía épica", "contenido": "La_Divina_Comedia.txt", "prestado": False},
    {"id": 3, "titulo": "Orgullo_y_Prejucio", "autor": "Jane Austen", "genero": "Novela romántica", "contenido": "Orgullo_y_Prejucio.txt", "prestado": False},
    {"id": 4, "titulo": "Frankenstein", "autor": "Mary Shelley", "genero": "Terror", "contenido": "Frankenstein.txt", "prestado": False},
    {"id": 5, "titulo": "Dracula", "autor": "Bram Stoker", "genero": "Terror", "contenido": "Dracula.txt", "prestado": False},
    {"id": 6, "titulo": "La_Ilíada", "autor": "Homero", "genero": "Épica", "contenido": "La_Ilíada.txt", "prestado": False},
    {"id": 7, "titulo": "La_Odisea", "autor": "Homero", "genero": "Épica", "contenido": "La_Odisea.txt", "prestado": False},
    {"id": 8, "titulo": "Hamlet", "autor": "William Shakespeare", "genero": "Tragedia", "contenido": "Hamlet.txt", "prestado": False},
    {"id": 9, "titulo": "Romeo_y_Julieta", "autor": "William Shakespeare", "genero": "Tragedia", "contenido": "Romeo_y_Julieta.txt", "prestado": False},
    {"id": 10, "titulo": "El_Principito", "autor": "Antoine de Saint-Exupéry", "genero": "Fábula", "contenido": "El_Principito.txt", "prestado": False},
    {"id": 11, "titulo": "Moby_Dick", "autor": "Herman Melville", "genero": "Aventura", "contenido": "Moby_Dick.txt", "prestado": False},
    {"id": 12, "titulo": "Alicia_en_el_Pais_de_las_Maravillas", "autor": "Lewis Carroll", "genero": "Fantasía", "contenido": "Alicia_en_el_Pais_de_las_Maravillas.txt", "prestado": False},
    {"id": 13, "titulo": "Viaje_al_Centro_de_la_Tierra", "autor": "Julio Verne", "genero": "Ciencia ficción", "contenido": "Viaje_al_Centro_de_la_Tierra.txt", "prestado": False},
    {"id": 14, "titulo": "La_Isla_del_Tesoro", "autor": "Robert Louis Stevenson", "genero": "Aventura", "contenido": "La_Isla_del_Tesoro.txt", "prestado": False},
    {"id": 15, "titulo": "El_Conde_de_Montecristo", "autor": "Alexandre Dumas", "genero": "Aventura", "contenido": "El_Conde_de_Montecristo.txt", "prestado": False},
    {"id": 16, "titulo": "Los_Tres_Mosqueteros", "autor": "Alexandre Dumas", "genero":"Aventura" , "contenido" : "Los_Tres_Mosqueteros.txt" , "prestado" : False},
    {"id": 17, "titulo": "Fausto", "autor": "Johann Wolfgang von Goethe", "genero": "Drama", "contenido": "Fausto.txt" , "prestado": False},
    {"id": 18, "titulo": "La_Metamorfosis", "autor": "Franz Kafka", "genero": "Ficción", "contenido": "La_Metamorfosis.txt", "prestado": False},
    {"id": 19, "titulo": "Las_Mil_y_Una_Noches", "autor": "Anónimo", "genero": "Cuentos", "contenido": "Las_Mil_y_Una_Noches.txt", "prestado": False},
    {"id": 20, "titulo": "El_Arte_de_la_Guerra", "autor": "Sun Tzu", "genero": "Estrategia", "contenido": "El_Arte_de_la_Guerra.txt", "prestado": False}
]

# Crear archivos .txt vacíos para cada libro
for li in Libros:
    if not os.path.exists(li["contenido"]):
        open(li["contenido"], "w", encoding="utf-8").close()

# Guardar la base de datos en un archivo JSON
with open("libros.json", "w", encoding="utf-8") as file_l_global:
    json.dump(Libros, file_l_global, indent=4, ensure_ascii=False)

usuarios = [
    {"id": 1, "nombre": "sneijder", "contraseña": "123contraseña", "libros_tenidos": []},
]

with open("usuarios.json", "w", encoding="utf-8") as file_u_global:
    json.dump(usuarios, file_u_global, indent=4, ensure_ascii=False)
    
#

class Biblioteca:
    def __init__(self, name_biblioteca, contraseña):
        self.name_biblioteca = name_biblioteca
        self.contraseña = contraseña

####


def ver_libros():
    libros = cargar_libros()
    for l in libros:
        if not l["prestado"]:
            print(f"\n{l}")
##############################################
#   agregar libro

def cargar_libros():
    with open("libros.json", "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_libros(libros):
    with open("libros.json", "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)


def calcular_nuevo_id_libros(libros_a):
    if libros_a:
        return libros_a[-1]["id"] + 1
    else:
        return 1


def agregar_libro(titulo, autor, genero, contenido):
    libros_a = cargar_libros()

    # calcular el nuevo id
    nuevo_id = calcular_nuevo_id_libros(libros_a)

    # crear objeto libro
    libro = class_libros.Libro(titulo, autor, genero, contenido)

    # convertir a dict y agregar id
   # libro_dict = libro.to_dict()
    #libro_dict["id"] = nuevo_id   pero habia una mejor manera:
    nombre_archivo = os.path.basename(contenido)
    
    LIBRO = libro.to_dict() # esto es un diccionario sin el id
    LIBRO["contenido"] = nombre_archivo # actualizamos el valor de "contenido" para que sea solo el nombre del archivo

  # guardar en la variable un diccionario con el id y los atributos(convertidos a diccionario)
    libro_dict = {"id": nuevo_id, **LIBRO} # esto es un diccionario con el id y los atributos(convertidos a diccionario)

    # agregar y guardar
    libros_a.append(libro_dict)
    guardar_libros(libros_a)


################################

def eliminar_libro(id_libro_elim):
    libros = cargar_libros()

    # Eliminar el libro sin modificar la lista mientras se recorre
    libros = [lib for lib in libros if lib["id"] != int(id_libro_elim)] 

    # Guardar cambios
    guardar_libros(libros)


####################################################

def eliminar_usuario(id_usuario_elim):
    Usuarios = cargar_usuarios()

    # Eliminar el usuario sin modificar la lista mientras se recorre
    Usuarios = [usu for usu in Usuarios if usu["id"] != int(id_usuario_elim)]

    # Guardar cambios
    guardar_usuarios(Usuarios)


####################################
def ver_usuarios():
    users = cargar_usuarios()
    for user in users:
        print(f"\n{user}")


######################################################################||||||||||||||||||||||||||||||||||
######################################################################||||||||||||||||||||||||||||||||||
#      FUNCION QUE NO SE USA LITERAL EN LA CLASE, SINO EN LO DEMAS    ||||||||||||||||||||||||||||||||||
######################################################################||||||||||||||||||||||||||||||||||
#      agregar usuario :

def cargar_usuarios():
    with open("usuarios.json", "r", encoding="utf-8") as file:
        return json.load(file)


def guardar_usuarios(usuarios_a):
    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(usuarios_a, archivo, indent=4, ensure_ascii=False)


def calcular_nuevo_id_usuarios(usuarios_a):
    if usuarios_a:
        return usuarios_a[-1]["id"] + 1
    else:
        return 1


def agregar_usuario(nombre, contraseña, libros_tenidos=None):
    usuarios_a = cargar_usuarios()

    # calcular el nuevo id
    nuevo_id = calcular_nuevo_id_usuarios(usuarios)

    # crear objeto usuario
    usuario = class_usuarios.Usuario(nombre, contraseña, libros_tenidos)

    # guardar en la variable un diccionario con el id y los atributos(convertidos a diccionario)
    usuario_dict = {"id": nuevo_id, **usuario.to_dict()}
   
    # agregar y guardar
    usuarios_a.append(usuario_dict)
    guardar_usuarios(usuarios_a)

#########################################################################
#########################################################################

biblioteca = Biblioteca("Biblioteca Central", "biblioteca123job")
