import mysql.connector

#conexion con la base de datos
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aa210980",
    database = "openbootcamp"
)

#creación del cursor
cursor = conexion.cursor()

try:
    cursor.execute("CREATE TABLE alumnos (id INT NOT NULL AUTO_INCREMENT, nombre VARCHAR (32) NOT NULL, apellidos VARCHAR (64) NOT NULL, PRIMARY KEY (id));")
    print("Se creó la base de datos")
except:
    print("Ocurrió un error al intentar crear la tabla. Inténtelo de nuevo.")

cursor.execute("INSERT INTO alumnos (id, nombre, apellidos) VALUES (1, 'Pepe', 'Perez')")