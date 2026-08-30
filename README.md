# Sistema de Biblioteca

Sistema de gestión para una red de bibliotecas diseñado con Programación Orientada a Objetos (POO) y una base de datos relacional local.

## Arquitectura del Proyecto


\`\`\`text
Sistema-De-Biblioteca/
├── .gitignore               # Archivos excluidos del control de versiones.
├── README.md                # Documentación principal del proyecto.
├── database/                
│   └── 01_schema.sqlite     # Archivo binario de la base de datos SQLite con las tablas ya creadas.
└── src/                     
    └── model/               # Clases que representan las entidades del negocio.
        ├── Libro.py         # Constructor y métodos de conexión a SQL para los libros.
        ├── Socio.py         # Constructor y métodos de conexión a SQL para los socios.
        └── main.py          # Punto de entrada principal para testear la conexión y ejecución.
\`\`\`

Interprete Python ver: 3.14.0