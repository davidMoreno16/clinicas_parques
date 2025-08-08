import sqlite3

def conectar_db():
    try:
        conn = sqlite3.connect('clinicas_parques.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        exit()

def crear_tablas(cursor):
    # Crear tabla para Clínicas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clinicas (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        direccion TEXT NOT NULL,
        telefono TEXT NOT NULL,
        especialidades TEXT NOT NULL
    )
    ''')

    # Crear tabla para Parques
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Parques (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        ubicacion TEXT NOT NULL,
        tipo TEXT NOT NULL,
        horarios TEXT NOT NULL
    )
    ''')

def insertar_clinicas(cursor):
    clinicas = [
        (1, 'Clinica Salud', 'Calle Falsa 123', '555-1234', 'General'),
        (2, 'Clinica Bienestar', 'Avenida Siempre Viva 456', '555-5678', 'Pediatría')
    ]
    cursor.executemany('INSERT INTO Clinicas (id, nombre, direccion, telefono, especialidades) VALUES (?, ?, ?, ?, ?)', clinicas)

def insertar_parques(cursor):
    parques = [
        (1, 'Parque Central', 'Centro de la ciudad', 'Recreativo', '8:00 AM - 8:00 PM'),
        (2, 'Parque de Aventura', 'Zona Norte', 'Aventura', '9:00 AM - 9:00 PM')
    ]
    cursor.executemany('INSERT INTO Parques (id, nombre, ubicacion, tipo, horarios) VALUES (?, ?, ?, ?, ?)', parques)

def main():
    with conectar_db() as conn:
        cursor = conn.cursor()
        crear_tablas(cursor)
        insertar_clinicas(cursor)
        insertar_parques(cursor)
        conn.commit()
    
    print("Datos de clínicas y parques insertados correctamente.")

if __name__ == "__main__":
    main()

