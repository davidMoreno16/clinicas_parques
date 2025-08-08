from pymongo import MongoClient

def conectar_mongo():
    try:
        client = MongoClient('localhost', 27017)
        db = client['clinicas_parques']
        return db
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        exit()

def validar_clinica(clinica):
    required_fields = ['nombre', 'direccion', 'telefono', 'especialidades']
    for field in required_fields:
        if field not in clinica or not clinica[field]:
            raise ValueError(f"El campo '{field}' es obligatorio.")

def insertar_clinicas(db, clinicas):
    for clinica in clinicas:
        try:
            validar_clinica(clinica)
            db.clinicas.insert_one(clinica)
            print(f"Clinica '{clinica['nombre']}' insertada correctamente.")
        except ValueError as e:
            print(f"Error al insertar clínica: {e}")
        except Exception as e:
            print(f"Error al insertar clínica: {e}")

def insertar_parques(db, parques):
    for parque in parques:
        try:
            db.parques.insert_one(parque)
            print(f"Parque '{parque['nombre']}' insertado correctamente.")
        except Exception as e:
            print(f"Error al insertar parque: {e}")

def main():
    db = conectar_mongo()

    clinicas = [
        {'nombre': 'Clinica Salud', 'direccion': 'Calle Falsa 123', 'telefono': '555-1234', 'especialidades': 'General'},
        {'nombre': 'Clinica Bienestar', 'direccion': 'Avenida Siempre Viva 456', 'telefono': '555-5678', 'especialidades': 'Pediatría'}
    ]
    insertar_clinicas(db, clinicas)

    parques = [
        {'nombre': 'Parque Central', 'ubicacion': 'Centro de la ciudad', 'tipo': 'Recreativo', 'horarios': '8:00 AM - 8:00 PM'},
        {'nombre': 'Parque de Aventura', 'ubicacion': 'Zona Norte', 'tipo': 'Aventura', 'horarios': '9:00 AM - 9:00 PM'}
    ]
    insertar_parques(db, parques)

if __name__ == "__main__":
    main()
