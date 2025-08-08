import json
from pymongo import MongoClient

def conectar_mongo():
    try:
        cliente = MongoClient('mongodb://localhost:27017/')
        db = cliente.db_no_relacional
        return db
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        exit()

def leer_datos_json(archivo):
    try:
        with open(archivo, encoding='utf-8') as f:
            datos = json.load(f)
        return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        exit()
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")
        exit()

def insertar_datos(coleccion, datos):
    if isinstance(datos, list):
        coleccion.insert_many(datos)
        print(f"Se insertaron {len(datos)} documentos en la colección 'empleados'.")
    else:
        coleccion.insert_one(datos)
        print("Se insertó 1 documento en la colección 'empleados'.")

def main():
    db = conectar_mongo()
    coleccion = db.empleados  # Cambia el nombre de la colección si lo deseas
    
    datos = leer_datos_json('data.json')
    insertar_datos(coleccion, datos)

if __name__ == "__main__":
    main()
