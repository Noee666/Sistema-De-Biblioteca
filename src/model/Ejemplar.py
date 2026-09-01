import sqlite3
from typing import Optional


class Ejemplar:
    """Representa un ejemplar físico de un libro en una sucursal específica."""

    def __init__(
        self,
        isbn: str,
        id_sucursal: int,
        estado: str = "disponible",
        id_ejemplar: Optional[int] = None,
    ):
        """Inicializa un nuevo ejemplar.

        Args:
            isbn (str): Código ISBN del libro al que pertenece la copia.
            id_sucursal (int): ID de la sucursal donde se encuentra el
              ejemplar.
            estado (str, opcional): Estado actual ('disponible', 'prestado', 'en
              reparación'). Por defecto es 'disponible'.
            id_ejemplar (int, opcional): Identificador único asignado por la BD.
        """
        self.id_ejemplar = id_ejemplar
        self.isbn = isbn
        self.id_sucursal = id_sucursal
        self.estado = estado

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """Inserta el ejemplar en la base de datos y asigna su id_ejemplar autoincremental.

        Args:
            conexion (sqlite3.Connection): Conexión activa a la base de datos
              SQLite.

        Returns:
            None
        """
        cursor = conexion.cursor()
        query = """
            INSERT INTO Ejemplar (isbn, id_sucursal, estado)
            VALUES (?, ?, ?)
        """
        cursor.execute(query, (self.isbn, self.id_sucursal, self.estado))
        conexion.commit()
        self.id_ejemplar = cursor.lastrowid
