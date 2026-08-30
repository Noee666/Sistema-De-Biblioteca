import sqlite3

class Libro:
    """
    Representa una libro en la base de datos
    """

    def __init__(self, isbn: str, titulo: str, editorial: str, anio: int, categoria: str):
        """
        Inicializa un nuevo libro.

        Args:
            isbn (str): Código numérico único de 13 dígitos.
            titulo (str): El título completo del libro.
            editorial (str): La editorial del libro.
            anio (int): El año de publicación del libro.
            categoria (str): La temática que maneja el libro.
        """
        self.isbn = isbn
        self.titulo = titulo
        self.editorial = editorial
        self.anio = anio
        self.categoria = categoria

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """
        Inserta los atributos del libro en la base de datos.

        Esta función crea un objeto de la clase Cursor y ejecuta un script
        en la base de datos con los valores inicializados en el constructor.

        Args:
            conexion (sqlite3.Connection): Conexión activa a la base de datos SQLite.

        Returns:
            None
        """

        cursor = conexion.cursor()
        query = "INSERT INTO Libro (isbn, titulo, editorial, anio, categoria) VALUES (?, ?, ?, ?, ?)"

        cursor.execute(query, (self.isbn, self.titulo, self.editorial, self.anio, self.categoria))
        conexion.commit()