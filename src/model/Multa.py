import sqlite3
from datetime import date
from typing import Optional


class Multa:
    """Representa una penalización generada por el retraso en un préstamo."""

    def __init__(self, id_prestamo: int, id_multa: Optional[int] = None):
        """
        Inicializa el registro principal de una multa.

        Args:
            id_prestamo (int): El identificador del préstamo que generó la infracción.
            id_multa (int, optional): Identificador único generado por la BD.
        """
        self.id_prestamo = id_prestamo
        self.id_multa = id_multa

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """Inserta la multa en la base de datos SQL."""
        cursor = conexion.cursor()
        query = "INSERT INTO Multa (id_prestamo) VALUES (?)"
        cursor.execute(query, (self.id_prestamo,))
        conexion.commit()
        self.id_multa = cursor.lastrowid


class CuotaPago:
    """Registra los abonos financieros realizados para liquidar una multa."""

    def __init__(self, id_multa: int, monto: float, fecha_pago: date, metodo_pago: str, estado: str = 'pendiente',
                 id_pago: Optional[int] = None):
        """
        Inicializa un nuevo abono para una multa existente.

        Args:
            id_multa (int): El identificador de la multa que se está pagando.
            monto (float): La cantidad de dinero entregada con precisión decimal.
            fecha_pago (date): El día exacto en que se realiza la transacción.
            metodo_pago (str): La forma de pago (ej. 'efectivo', 'tarjeta').
            estado (str, optional): Situación del pago. Por defecto es 'pendiente'.
            id_pago (int, optional): ID generado por la base de datos.

        Raises:
            ValueError: Si el estado no es 'pendiente' o 'pagado'.
        """
        if estado not in ('pendiente', 'pagado'):
            raise ValueError("Error: El estado del pago debe ser 'pendiente' o 'pagado'.")

        self.id_multa = id_multa
        self.monto = monto
        self.fecha_pago = fecha_pago
        self.metodo_pago = metodo_pago
        self.estado = estado
        self.id_pago = id_pago

    def guardar_en_bd(self, conexion: sqlite3.Connection) -> None:
        """Inserta el registro del pago en la base de datos."""
        cursor = conexion.cursor()
        query = """
                INSERT INTO Cuota_Pago (id_multa, monto, fecha, metodo_pago, estado)
                VALUES (?, ?, ?, ?, ?) \
                """
        cursor.execute(query, (self.id_multa, self.monto, self.fecha_pago, self.metodo_pago, self.estado))
        conexion.commit()
        self.id_pago = cursor.lastrowid