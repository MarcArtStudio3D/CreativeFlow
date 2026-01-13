# modulos/comun/model/MasterModel.py

class MasterModel:
    def __init__(self, sqlite_model):
        self.sqlite_model = sqlite_model

    def get_paises(self):
        cursor = self.sqlite_model.db.cursor()
        cursor.execute("SELECT id, nombre FROM paises ORDER BY nombre ASC")
        return cursor.fetchall()

    def get_provincias(self, id_pais):
        cursor = self.sqlite_model.db.cursor()
        cursor.execute("SELECT id, nombre FROM provincias WHERE id_pais = ?", (id_pais,))
        return cursor.fetchall()


    def get_ciudadesEspana(self):
        cursor = self.sqlite_model.db.cursor()
        cursor.execute("SELECT id, nombre FROM ciudades ORDER BY nombre ASC")
        return cursor.fetchall()
    def get_ciudadesFrancia(self):
        cursor = self.sqlite_model.db.cursor()
        cursor.execute("SELECT id, nombre FROM villagesfrance ORDER BY nombre ASC")
        return cursor.fetchall()