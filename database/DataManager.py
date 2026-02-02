from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord
import os


class DataManager:
    def __init__(self, connection_name="main_worker"):
        self.connection_name = connection_name
        self.db = None

    def conectar(self, motor, config):
        # Si la conexión ya existe, la recuperamos en lugar de borrarla
        if QSqlDatabase.contains(self.connection_name):
            self.db = QSqlDatabase.database(self.connection_name)
        else:
            self.db = QSqlDatabase.addDatabase(motor, self.connection_name)

        if motor == 'QSQLITE':
            self.db.setDatabaseName(config['database'])
        else:
            self.db.setHostName(config.get('host', 'localhost'))
            self.db.setDatabaseName(config.get('database'))
            self.db.setUserName(config.get('user'))
            self.db.setPassword(config.get('password'))
            self.db.setPort(int(config.get('port', 5432)))

        if not self.db.isOpen():
            if not self.db.open():
                print(f"❌ Error en {self.connection_name}: {self.db.lastError().text()}")
                return False
        return True

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
        
