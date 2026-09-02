import sqlite3
from datetime import date

class Membresia:
    def __init__(self, id_socio: int, tipo: str, fecha_inicio: date, fecha_fin: date ):
        if tipo not in ('estudiante','profesor','externo'):
            raise ValueError('Error: Tipo de Membresia incorrecto')
        self.id_socio = id_socio
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        cursor = conexion.cursor()
        query = "INSERT INTO Membresia VALUES (?, ?, ?, ?)"
        cursor.execute(query, (self.id_socio, self.tipo, self.fecha_inicio, self.fecha_fin))
        conexion.commit()


