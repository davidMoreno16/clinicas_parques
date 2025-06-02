from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['clinicas_parques']

# Consultar clínicas
clinicas = db.clinicas.find()
print("Clínicas:")
for clinica in clinicas:
    print(clinica)

# Consultar parques
parques = db.parques.find()
print("\nParques:")
for parque in parques:
    print(parque)