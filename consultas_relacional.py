import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('clinicas_parques.db')
cursor = conn.cursor()

# Consultar clínicas
cursor.execute('SELECT * FROM Clinicas')
print("Clínicas:")
for row in cursor.fetchall():
    print(row)

# Consultar parques
cursor.execute('SELECT * FROM Parques')
print("\nParques:")
for row in cursor.fetchall():
    print(row)

conn.close()