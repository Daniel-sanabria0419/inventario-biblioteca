from models.libro import Libro
from models.usuario import Usuario
from utils.file_handler import get_data, save_data
def main():

    books = get_data("biblioteca/data/libros.json")
    print(books)
    for book in books:
        print(book.nombre)
    
if __name__ == "__main__":
    main()