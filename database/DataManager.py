from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord
import os


class DataManager:
    def __init__(self, connection_name="main_worker"):
        self.connection_name = connection_name
        self.db = None
        self.engine = None

    def conectar(self, motor, config):
        """
        motor: 'QPSQL' (Postgres), 'QMARIADB' o 'QMYSQL', 'QSQLITE'
        config: diccionario con host, database, user, password, port
        """
        # Evitar duplicar conexiones con el mismo nombre
        if QSqlDatabase.contains(self.connection_name):
            QSqlDatabase.removeDatabase(self.connection_name)

        self.db = QSqlDatabase.addDatabase(motor, self.connection_name)

        if motor == 'QSQLITE':
            self.db.setDatabaseName(config['database'])  # Aquí va la ruta al .db
        else:
            self.db.setHostName(config.get('host', 'localhost'))
            self.db.setDatabaseName(config.get('database'))
            self.db.setUserName(config.get('user'))
            self.db.setPassword(config.get('password'))
            self.db.setPort(int(config.get('port', 5432)))

        if self.db.open():
            self.engine = motor
            print(f"✅ Conectado a {motor} con éxito")
            return True
        else:
            print(f"❌ Error: {self.db.lastError().text()}")
            return False

    def consultar(self, sql, params=None):
        """Equivalente a tu método actual, devuelve lista de diccionarios"""
        query = QSqlQuery(self.db)
        query.prepare(sql)

        if params:
            for p in params:
                query.addBindValue(p)

        resultados = []
        if query.exec():
            record = query.record()
            while query.next():
                fila = {}
                for i in range(record.count()):
                    fila[record.fieldName(i)] = query.value(i)
                resultados.append(fila)
        return resultados

    def ejecutar(self, sql, params=None):
        """Para INSERT, UPDATE, DELETE"""
        query = QSqlQuery(self.db)
        query.prepare(sql)

        if params:
            for p in params:
                query.addBindValue(p)

        if query.exec():
            return True, "Operación realizada"
        else:
            return False, query.lastError().text()