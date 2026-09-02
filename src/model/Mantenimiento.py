import sqlite3
from datetime import datetime
from typing import Optional


class Mantenimiento:
    """Representa los costos de mantenimiento de un ejemplar"""

    def __init__(self, id_ejemplar: int, fecha: datetime, descripcion: str, costo: float, responsable: str, id_mantenimiento: Optional[int] = None):
        self.id_ejemplar = id_ejemplar
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        self.responsable = responsable
        self.id_mantenimiento = id_mantenimiento


    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:

        cursor = conexion.cursor()
        query: str = """
                INSERT INTO mantenimiento (id_ejemplar, fecha, descripcion, costo, responsable) 
                VALUES (?, ?, ?, ?, ?) 
                """

        cursor.execute(query, (self.id_ejemplar, self.fecha, self.descripcion, self.costo, self.responsable))
        self.id_mantenimiento = cursor.lastrowid
        conexion.commit()