class Libro:
    def __init__(self, isbn: str, titulo: str, editorial: str, anio: int, categoria: str):
        self.isbn = isbn
        self.titulo = titulo
        self.editorial = editorial
        self.anio = anio
        self.categoria = categoria

    def guardar_en_bd(self, conexion) -> None:
        cursor = conexion.cursor()
        query = "INSERT INTO Libro (isbn, titulo, editorial, anio, categoria) VALUES (?, ?, ?, ?, ?)"

        cursor.execute(query, (self.isbn, self.titulo, self.editorial, self.anio, self.categoria))
        conexion.commit()