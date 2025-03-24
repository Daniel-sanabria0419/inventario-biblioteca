import json
from models.libro import Libro



def get_data(type):

    with open(type, "r", encoding="utf-8") as file:
        libros = json.load(file)
        return [Libro.to_object(libro) for libro in libros]
    
def save_data(libros: list[Libro], type: str):
    
    datos = [libro.to_json() for libro in libros]
    with open(type, "w") as file:
        
        json.dump(datos,file, indent=4)
        print(f"datos guardados en {type}")
