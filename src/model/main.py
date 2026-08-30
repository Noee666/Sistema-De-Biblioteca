import sqlite3
from pathlib import Path

ruta_raiz = Path(__file__).parent.parent.parent
ruta_bd = ruta_raiz / "database"

conexion = sqlite3.connect(ruta_bd / '01_schema.sqlite')
cursor = conexion.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
print(tablas)

conexion.close()