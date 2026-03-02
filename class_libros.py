
import class_biblioteca

class Libro:
    def __init__(self, titulo, autor, genero, contenido, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.contenido = contenido
        self.prestado = prestado

    def to_dict(self):
        #Convierte el objeto en un diccionario
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "contenido": self.contenido,
            "prestado": self.prestado
        }


def validar_id_libro(id_libro):
    libros = class_biblioteca.cargar_libros()
    for libro in libros:
        if int(libro["id"]) == int(id_libro):
            return True

    return False
    

