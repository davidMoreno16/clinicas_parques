import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('clinicas_parques.db')
cursor = conn.cursor()

# Crear tabla para Clínicas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clinicas (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    telefono TEXT,
    especialidades TEXT
)
''')

# Crear tabla para Parques
cursor.execute('''
CREATE TABLE IF NOT EXISTS Parques (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    ubicacion TEXT,
    tipo TEXT,
    horarios TEXT
)
''')

# Insertar datos de clínicas
cursor.executemany('INSERT INTO Clinicas (id, nombre, direccion, telefono, especialidades) VALUES (?, ?, ?, ?, ?)', [
    (1, 'Clinica Salud', 'Calle Falsa 123', '555-1234', 'General'),
    (2, 'Clinica Bienestar', 'Avenida Siempre Viva 456', '555-5678', 'Pediatría')
])

# Insertar datos de parques
cursor.executemany('INSERT INTO Parques (id, nombre, ubicacion, tipo, horarios) VALUES (?, ?, ?, ?, ?)', [
    (1, 'Parque Central', 'Centro de la ciudad', 'Recreativo', '8:00 AM - 8:00 PM'),
    (2, 'Parque de Aventura', 'Zona Norte', 'Aventura', '9:00 AM - 9:00 PM')
])

conn.commit()
conn.close()