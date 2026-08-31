import sqlite3
from typing import Optional

class Prestamo:
    """ Representa la toma de un libro por parte de un socio. """

    def __init__(
        self,
        id_socio: int,
        id_ejemplar: int,
        fecha_prestamo: str,
        fecha_esperada: str,
        fecha_real_dev: Optional[str] = None,
        id_prestamo: Optional[int] = None,
    ):
        """
        Inicializa un nuevo registro de préstamo.

        Args:
            id_socio (int): Identificador del socio que realiza el préstamo.
            id_ejemplar (int): Identificador del ejemplar prestado.
            fecha_prestamo (str): Fecha de inicio del préstamo (YYYY-MM-DD).
            fecha_esperada (str): Fecha acordada de entrega (YYYY-MM-DD).
            fecha_real_dev (str, opcional): Fecha de devolución efectiva. None si sigue activo.
            id_prestamo (int, opcional): Identificador único asignado por la BD.
        """
        self.id_prestamo = id_prestamo
        self.id_socio = id_socio
        self.id_ejemplar = id_ejemplar
        self.fecha_prestamo = fecha_prestamo
        self.fecha_esperada = fecha_esperada
        self.fecha_real_dev = fecha_real_dev

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """
        Inserta el préstamo en la base de datos y asigna su id_prestamo.

        Args:
            conexion (sqlite3.Connection): Conexión activa a SQLite.

        Returns:
            None
        """
        cursor = conexion.cursor()
        query = """
            INSERT INTO Prestamo (id_socio, id_ejemplar, fecha_prestamo, fecha_esperada_dev, fecha_real_dev)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            (
                self.id_socio,
                self.id_ejemplar,
                self.fecha_prestamo,
                self.fecha_esperada,
                self.fecha_real_dev,
            ),
        )
        conexion.commit()
        self.id_prestamo = cursor.lastrowid

    def registrar_devolucion(self, conexion: sqlite3.Connection, fecha_de_dev: str) -> None:
        """
        Actualiza la fecha de devolución real del préstamo en memoria y en la base de datos.

        Args:
            conexion (sqlite3.Connection): Conexión activa a SQLite.
            fecha_de_dev (str): Fecha efectiva en que se devuelve el ejemplar (YYYY-MM-DD).

        Raises:
            ValueError: Si el préstamo no ha sido guardado previamente en la base de datos.

        Returns:
            None
        """
        if self.id_prestamo is None:
            raise ValueError("No se puede actualizar un préstamo que no está guardado en la base de datos.")

        self.fecha_real_dev = fecha_de_dev
        cursor = conexion.cursor()
        query = """
            UPDATE Prestamo
            SET fecha_real_dev = ?
            WHERE id_prestamo = ?
        """
        cursor.execute(query, (self.fecha_real_dev, self.id_prestamo))
        conexion.commit()
