import sqlite3
from pathlib import Path
from Socio import Socio
from Sucursal import Sucursal
from Ejemplar import Ejemplar
from Libro import Libro


# Utilidades necesarias para establecer conexion a la base de datos
RUTA_RAIZ = Path(__file__).parent.parent.parent
RUTA_BD = RUTA_RAIZ / "database"

conexion = sqlite3.connect(RUTA_BD / '01_schema.sqlite')
cursor = conexion.cursor()



def crear_nueva_sucursal(nombre: str, direccion: str, horario: str):

    sucursal_01: Sucursal = Sucursal(nombre, direccion, horario, None)
    sucursal_01.guardar_en_bd(conexion)

def crear_nuevo_ejemplar(nombre: str, id_sucursal: int, estado: str) -> None:
    ejemplar_01: Ejemplar = Ejemplar(nombre, id_sucursal, estado, None)
    ejemplar_01.guardar_en_bd(conexion)

def crear_nuevo_socio(nombre: str, id_sucursal: int) -> None:

    socio_01: Socio = Socio(nombre , id_sucursal, )
    socio_01.guardar_en_bd(conexion)

def crear_nuevo_libro(isbn: str, titulo: str, editorial: str, anio: int, categoria: str) -> None:

    libro_01: Libro = Libro(isbn, titulo, editorial, anio, categoria)
    libro_01.guardar_en_bd(conexion)



conexion.close()