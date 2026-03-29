


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

