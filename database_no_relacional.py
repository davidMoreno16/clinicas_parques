from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('localhost', 27017)
db = client['clinicas_parques']

# Insertar datos de clínicas
clinicas = [
    {'nombre': 'Clinica Salud', 'direccion': 'Calle Falsa 123', 'telefono': '555-1234', 'especialidades': 'General'},
    {'nombre': 'Clinica Bienestar', 'direccion': 'Avenida Siempre Viva 456', 'telefono': '555-5678', 'especialidades': 'Pediatría'}
]
db.clinicas.insert_many(clinicas)

# Insertar datos de parques
parques = [
    {'nombre': 'Parque Central', 'ubicacion': 'Centro de la ciudad', 'tipo': 'Recreativo', 'horarios': '8:00 AM - 8:00 PM'},
    {'nombre': 'Parque de Aventura', 'ubicacion': 'Zona Norte', 'tipo': 'Aventura', 'horarios': '9:00 AM - 9:00 PM'}
]
db.parques.insert_many(parques)

print("Datos de clínicas y parques insertados correctamente.")