/sistema-biblioteca

├── database/                   # Scripts para la base de datos (Ej. SQLite o PostgreSQL)

│   ├── 01\_schema.sql           # DDL: Creación de tablas (Sucursal, Libro, Socio, etc.)

│   ├── 02\_seed.sql             # DML: Datos iniciales (catálogos, sucursales base)

│   └── vistas\_triggers.sql     # Lógica en base de datos (Ej. vista de préstamos vencidos)

│

├── src/                        # Código fuente principal

&#x20;   ├── models/                 # Entidades del dominio (Clases/Modelos)

&#x20;       ├── Libro               # Título, ISBN, Editorial, etc.

&#x20;       ├── Autor               # Relación N:M con Libro

&#x20;       ├── Prestamo            # Conecta Socio con Ejemplar

&#x20;       └── Membresia           # Fechas de vigencia y tipo



