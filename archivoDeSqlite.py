import sqlite3

# Conexión a la base de datos (si no existe, se creará automáticamente)
conexion = sqlite3.connect('agenda_clientes.db')

# Creación del cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Crear tabla para almacenar información de clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    dato_extra TEXT
                )''')

# Función para agregar un cliente a la base de datos
def agregar_cliente(nombre, telefono, direccion, dato_extra=None):
    cursor.execute('''INSERT INTO clientes (nombre, telefono, direccion, dato_extra)
                      VALUES (?, ?, ?, ?)''', (nombre, telefono, direccion, dato_extra))
    conexion.commit()

# Función para obtener todos los clientes de la base de datos
def obtener_clientes():
    cursor.execute('''SELECT * FROM clientes''')
    return cursor.fetchall()

# Ejemplo de uso
agregar_cliente("Juan Perez", "123456789", "Calle Principal 123", "Cliente VIP")
agregar_cliente("María López", "987654321", "Avenida Central 456")

clientes = obtener_clientes()
for cliente in clientes:
    print(cliente)

# Cerrar conexión y cursor cuando hayas terminado
cursor.close()
conexion.close()
