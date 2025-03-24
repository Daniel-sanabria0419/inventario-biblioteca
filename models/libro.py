
import re


class Libro:

    def __init__(self, nombre: str, autor: str, isbn: str, cliente):
        self.nombre = nombre
        self.autor = autor
        self.isbn = isbn
        self.cliente = cliente


    
    def to_json(self):
        return {
            "nombre_libro" : self.nombre ,
            "autor" : self.autor ,
            "isbn" : self.isbn,
            "cliente" : None
        }
    

    @classmethod
    def to_object(cls, data: list[str])-> object:
        libro = cls(data["nombre_libro"], data["autor"], data["isbn"], data["cliente"]) 
        return libro

