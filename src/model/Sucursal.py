import sqlite3
from typing import Optional

class Sucursal:
    """Representa una sucursal de la biblioteca en la base de datos."""

    def __init__(
        self,
        nombre: str,
        direccion: str,
        horario: str,
        id_sucursal: Optional[int] = None,
    ):
        """Inicializa una nueva sucursal.

        Args:
            nombre (str): Nombre identificativo de la sucursal.
            direccion (str, opcional): Dirección física de la sucursal.
            horario (str, opcional): Horario de atención al público.
            id_sucursal (int, opcional): Identificador único (autogenerado por
            la BD).
        """
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """Inserta la sucursal en la base de datos y asigna el id_sucursal generado.

        Args:
            conexion (sqlite3.Connection): Conexión activa a la base de datos
            SQLite.

        Returns:
            None
        """
        cursor = conexion.cursor()
        query = """
                INSERT INTO Sucursal (nombre, direccion, horario)
                VALUES (?, ?, ?)
                """
        cursor.execute(query, (self.nombre, self.direccion, self.horario))
        conexion.commit()
        self.id_sucursal = cursor.lastrowid
