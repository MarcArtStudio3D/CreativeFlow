import sqlite3
import os
import bcrypt


class DataModel:
    def __init__(self):
        # 1. Obtenemos la ruta absoluta de donde está este archivo (model.py)
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # 2. Subimos un nivel para llegar a la raíz del proyecto (CreativeFlow/)
        dir_raiz = os.path.dirname(dir_actual)

        # 3. Construimos la ruta completa al archivo .db
        self.sqlite_path = os.path.join(dir_raiz, "creativeflow.db")

        print(f"DEBUG: Buscando base de datos en: {self.sqlite_path}")

    def get_empresas_list(self):
        """Devuelve nombres de empresas para el ComboBox"""
        # Usamos 'uri=True' para que si no existe, falle en lugar de crear una vacía
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_comercial FROM empresas")
            res = [row[0] for row in cursor.fetchall()]
            conn.close()
            return res
        except sqlite3.OperationalError as e:
            print(f"Error crítico: ¿Existe el archivo .db? {e}")
            return []

    def validar_acceso(self, empresa, usuario, password_ingresada):
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            query = """
                    SELECT u.contrasena, r.nombre_rol
                    FROM usuarios u
                             JOIN roles r ON u.id_rol = r.id
                    WHERE u.nombre = ? \
                    """
            cursor.execute(query, (usuario,))
            result = cursor.fetchone()
            conn.close()

            if result:
                hash_db_str = result[0]
                rol_nombre = result[1]

                # EL TRUCO ESTÁ AQUÍ:
                # 1. Convertimos la password del usuario a bytes
                password_bytes = password_ingresada.encode('utf-8')

                # 2. Convertimos el hash de la base de datos a bytes
                # Si el hash es None o vacío, bcrypt fallará, así que validamos
                if not hash_db_str:
                    return {"success": False, "error": "El usuario no tiene contraseña asignada."}

                hash_db_bytes = hash_db_str.encode('utf-8')

                # 3. Comparación binaria
                if bcrypt.checkpw(password_bytes, hash_db_bytes):
                    return {"success": True, "rol": rol_nombre}
                else:
                    return {"success": False, "error": "Contraseña incorrecta."}

            return {"success": False, "error": "Usuario no encontrado."}

        except Exception as e:
            # Esto capturará el error de 'PyBytes' si algo falla y te lo mostrará en tu popup
            return {"success": False, "error": f"Error técnico: {str(e)}"}