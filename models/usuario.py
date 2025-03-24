import json

class Usuario:
    def __init__(self, nombre: str, direccion: str, ID: str, celular:int, libros: dict):
        """llamar esta clase con sus parametro crea una usuario con los datos que se le asigno"""

        self.nombre = nombre
        self.direccion = direccion
        self.ID = ID
        self.celular = celular
        self.libros = libros
    
    