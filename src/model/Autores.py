import sqlite3
from typing import Optional

class Autor:
    """Representa un autor en la base de datos."""

    def __init__(self, nombre: str, id_autor: Optional[int] = None):
        """Inicializa un nuevo autor.

        Args:
            nombre (str): Nombre completo del autor.
            id_autor (int, opcional): Identificador único asignado por la BD.
        """
        self.id_autor = id_autor
        self.nombre = nombre

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """Inserta el autor en la base de datos y asigna su id_autor autoincremental.

        Args:
            conexion (sqlite3.Connection): Conexión activa a la base de datos SQLite.

        Returns:
            None
        """
        cursor = conexion.cursor()
        query = "INSERT INTO Autor (nombre) VALUES (?)"

        # Se usa una tupla (self.nombre,) de un solo elemento para evitar inyecciones SQL
        cursor.execute(query, (self.nombre,))
        conexion.commit()

        # Recupera el ID generado automáticamente por la base de datos
        self.id_autor = cursor.lastrowid