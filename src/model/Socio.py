import sqlite3
from typing import Optional


class Socio:

    def __init__(self, nombre:str, id_sucursal_base: Optional[int] = None, activo:bool = True):
        self.nombre = nombre
        self.id_sucursal_base = id_sucursal_base
        self.activo = activo

    def guardar_en_bd(self, conexion:sqlite3.Connection) -> None:
        cursor = conexion.cursor()
        query = "INSERT INTO Socio (nombre, id_sucursal_base) VALUES (?, ?)"
        cursor.execute(query, (self.nombre, self.id_sucursal_base))
        conexion.commit()