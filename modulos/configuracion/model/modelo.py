class EmpresaModel:
    def __init__(self, db_manager):
        self.db = db_manager

    def obtener_empresa(self, id_empresa):
        # Usamos row_factory para que devuelva un diccionario {columna: valor}
        return self.db.fetch_one_as_dict("SELECT * FROM empresas WHERE id = ?", (id_empresa,))

    def actualizar_empresa(self, id_empresa, datos_dict):
        # Construimos la query dinámicamente
        columnas = [f"{k} = ?" for k in datos_dict.keys()]
        query = f"UPDATE empresas SET {', '.join(columnas)} WHERE id = ?"

        valores = list(datos_dict.values())
        valores.append(id_empresa)

        return self.db.execute(query, tuple(valores))