import sqlite3
import bcrypt
import os

# Configura tu ruta
NUEVA_PASS = "admin123" # La que tú quieras

# 1. Obtenemos la ruta absoluta de donde está este archivo (model.py)
dir_actual = os.path.dirname(os.path.abspath(__file__))

# 2. Subimos un nivel para llegar a la raíz del proyecto (CreativeFlow/)
dir_raiz = os.path.dirname(dir_actual)

# 3. Construimos la ruta completa al archivo .db
sqlite_path = os.path.join(dir_raiz, "creativeflow.db")

# 1. Generar el nuevo hash
salt = bcrypt.gensalt()
nuevo_hash = bcrypt.hashpw(NUEVA_PASS.encode('utf-8'), salt)

# 2. Guardar en la base de datos (se guarda como string decodificado)
conn = sqlite3.connect(sqlite_path)
cursor = conn.cursor()
cursor.execute("UPDATE usuarios SET contrasena = ? WHERE nombre = 'admin'", (nuevo_hash.decode('utf-8'),))
conn.commit()
conn.close()

print("¡Usuario actualizado a bcrypt correctamente!")