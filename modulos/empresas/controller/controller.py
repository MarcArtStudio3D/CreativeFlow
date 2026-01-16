import os

from PySide6 import QtCore
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import QMessageBox

from helpers.mapeoCampos import MapeoCampos
from helpers.messagebox_styles import aplicar_estilo_messagebox
from modulos.empresas.view.EmpresaConfigView import EmpresaConfigView
from modulos.comun.view.DBConsultaView import DBConsultaView
from helpers.validadores import ValidadorFiscal


class EmpresaController:
    def __init__(self, vista: EmpresaConfigView, modelo, session_data: dict):
        self.vista = vista
        self.modelo = modelo
        self.id_empresa = session_data.get("id_empresa", 0)
        self.columnas_actuales = []
        self.session_data = session_data
        self.validador = ValidadorFiscal()
        self._validando = False  # Flag para evitar validaciones en cascada


        #conecto botones
        self.vista.btn_guardar_nuevo.clicked.connect(self.guardar_datos)
        self.vista.btn_deshacer.clicked.connect(self.cargar_datos)
        self.vista.btn_salir.clicked.connect(self.vista.close)
        self.vista.btnBuscarPais.clicked.connect(self.abrir_selector_paises)
        self.vista.btnCrearDBMariaDb.clicked.connect(self.preparar_base_datos_mariadb)
        self.vista.btnTestBDMariaDB.clicked.connect(self.probar_conexion_mariadb)

        #conecto señales de campos
        self.vista.cp.editingFinished.connect(self.buscar_poblacion_cp_handler)
        self.vista.poblacion.editingFinished.connect(self.buscar_poblacion_handler)
        self.vista.cif_siren.editingFinished.connect(self.validar_codigo_identificacion)
        self.vista.siret.editingFinished.connect(self.validar_siret)

        # Desactivo campos que no deben editarse
        self.vista.pais.setReadOnly(True)

        #campos que dependen del pais seleccionado
        if (session_data.get("pais", "") == "España"):
            self.vista.provincia.setVisible(True)
            self.vista.label_provincia.setVisible(True)
            self.vista.label_cif_siren.setText("CIF:")
            self.vista.label_siret.setVisible(False)
            self.vista.siret.setVisible(False)
            self.vista.label_APE_NAF.setVisible(False)
            self.vista.ape_naf.setVisible(False)
            self.vista.label_N_RCS.setVisible(False)
            self.vista.rcs.setVisible(False)
            self.vista.label_ciudad_rcs.setVisible(False)
            self.vista.ciudad_rcs.setVisible(False)
            self.vista.label_forma_juridica.setVisible(False)
            self.vista.forma_juridica.setVisible(False)
            self.vista.non_tva.setVisible(False)
            self.vista.label_n_rm.setVisible(False)
            self.vista.registro_mercantil.setVisible(False)
            self.vista.groupBox_IRPF.setVisible(True)


        else:
            self.vista.provincia.setVisible(False)
            self.vista.label_provincia.setVisible(False)
            self.vista.label_cif_siren.setText("SIREN:")
            self.vista.label_siret.setVisible(True)
            self.vista.siret.setVisible(True)
            self.vista.label_APE_NAF.setVisible(True)
            self.vista.ape_naf.setVisible(True)
            self.vista.label_N_RCS.setVisible(True)
            self.vista.rcs.setVisible(True)
            self.vista.label_ciudad_rcs.setVisible(True)
            self.vista.ciudad_rcs.setVisible(True)
            self.vista.label_forma_juridica.setVisible(True)
            self.vista.forma_juridica.setVisible(True)
            self.vista.label_n_rm.setVisible(True)
            self.vista.non_tva.setVisible(True)
            self.vista.registro_mercantil.setVisible(True)
            self.vista.groupBox_IRPF.setVisible(False)


        # Solo cargamos datos si hay un id_empresa válido
        if self.id_empresa and self.id_empresa > 0:
            self.cargar_datos()


    def cargar_datos(self):
        # 1. Obtenemos los datos del modelo (el ID viene del __init__)
        # El modelo debe devolver: (la_fila_de_datos, lista_nombres_columnas)
        fila, columnas = self.modelo.get_datos_empresa(self.id_empresa)

        if not fila:
            # Aquí puedes usar tu nuevo sistema de traducción
            ctx = "EmpresaController"
            titulo = QtCore.QCoreApplication.translate(ctx, "Error de carga")
            msg = QtCore.QCoreApplication.translate(ctx, f"No se encontró la empresa con ID: {self.id_empresa}")

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(msg)
            aplicar_estilo_messagebox(msg_box, "critical")
            msg_box.exec()
            return

        # 2. La magia: MapeoCampos rellena TODO el formulario de golpe
        # Buscando widgets que se llamen como las columnas
        MapeoCampos.mapear_datos_a_vista(self.vista, columnas, fila)

        # 3. Guardamos las columnas para cuando toque capturar los datos al guardar
        self.columnas_actuales = columnas

    def guardar_datos(self):
        contexto = "EmpresaController"
        # 1. Validar
        valido, campos_faltantes = MapeoCampos.validar_campos(self.vista)

        if not valido:
            msg = QtCore.QCoreApplication.translate(contexto, "Los siguientes campos son obligatorios:\n\n- ") + "\n- ".join(campos_faltantes)
            tit = QtCore.QCoreApplication.translate(contexto, "Faltan datos")

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle(tit)
            msg_box.setText(msg)
            aplicar_estilo_messagebox(msg_box, "warning")
            msg_box.exec()
            return

        # 2. Capturar (usando tu lógica espejo)
        datos = MapeoCampos.capturar_datos_vista(self.vista, self.columnas_actuales)

        # 3. Mandar al modelo
        if self.modelo.actualizar_empresa(self.id_empresa, datos):
            titulo = QtCore.QCoreApplication.translate(contexto, "Éxito")
            mensaje = QtCore.QCoreApplication.translate(contexto, "Empresa actualizada correctamente")

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "information")
            msg_box.exec()
        else:
            titulo = QtCore.QCoreApplication.translate(contexto, "Error")
            mensaje = QtCore.QCoreApplication.translate(contexto, "No se pudieron guardar los datos en la base de datos.")

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "critical")
            msg_box.exec()

    def abrir_selector_paises(self):
        """
        Abre el selector de países reutilizando la conexión SQLite existente.
        """
        # Reutilizamos la conexión existente del modelo
        db = self.modelo.sqlite_model.db

        if not db.isOpen():
            QMessageBox.critical(
                self.vista,
                "Error de conexión",
                "La base de datos no está abierta"
            )
            return

        # Instanciamos el buscador genérico
        buscador = DBConsultaView(db)

        # Lo configuramos igual que hacías en C++
        buscador.set_config(
            titulo="Seleccione País",
            sql_base="SELECT id, nombre, iso FROM paises",
            campos_busqueda=["nombre", "iso"],
            headers=["ID", "País", "Código ISO"]
        )
        buscador.set_tamano_columnas([0,600,80])

        if buscador.exec():
            # Recuperamos el ID y el nombre
            id_pais = buscador.id_seleccionado
            nombre_pais = buscador.registro.value("nombre")

            # Actualizamos la vista de empresas
            self.vista.pais.setText(nombre_pais)
            # Guardamos el ID en alguna parte para el UPDATE
            # (podrías agregar un campo oculto en la vista o un atributo temporal)

    def buscar_poblacion_cp_handler(self):
        """Handler para editingFinished que obtiene el texto del campo cp"""
        cp = self.vista.cp.text().strip()
        poblacion = self.vista.poblacion.text().strip()
        if cp and not poblacion:  # Solo buscar si hay algo escrito
            self.buscar_poblacion_cp(cp)

    def buscar_poblacion_cp(self, texto_busqueda):
        """
        Busca población por código postal.
        No usa query.size() porque devuelve -1 en muchos drivers.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 57
        else:
            id_pais = 64

        # SQL preparado con placeholders
        sql = """SELECT poblacion, provincia_region, cp, region_code
                 FROM poblaciones
                 WHERE id_pais = ? AND (cp = ? OR cp_adicionales LIKE ?)"""

        query = QSqlQuery(self.modelo.sqlite_model.db)
        query.prepare(sql)
        query.addBindValue(id_pais)
        query.addBindValue(texto_busqueda)
        query.addBindValue(f"%{texto_busqueda}%")

        if not query.exec():
            print(f"❌ Error SQL: {query.lastError().text()}")
            return

        # Recolectamos todas las filas (query.size() no funciona bien)
        filas = []
        while query.next():
            filas.append({
                "poblacion": query.value("poblacion"),
                "provincia_region": query.value("provincia_region"),
                "cp": query.value("cp"),
            })

        print(f"🔍 Búsqueda CP '{texto_busqueda}' en país {id_pais}: {len(filas)} resultados")

        # Sin resultados
        if len(filas) == 0:
            return

        # 1 resultado: rellenar directamente
        if len(filas) == 1:
            fila = filas[0]
            self.vista.poblacion.setText(str(fila["poblacion"] or ""))
            self.vista.cp.setText(str(fila["cp"] or ""))

            if pais_text == "España":
                self.vista.provincia.setText(str(fila["provincia_region"] or ""))
            return

        # Múltiples resultados: abrir selector
        self.abrir_selector_poblaciones_CP(texto_busqueda)


    def buscar_poblacion_handler(self):
        """Handler para editingFinished que obtiene el texto del campo POBLACION"""
        cp = self.vista.cp.text().strip()
        poblacion = self.vista.poblacion.text().strip()
        if not cp and poblacion:  # Solo buscar si hay algo escrito
            self.buscar_poblacion(poblacion)

    def buscar_poblacion(self, texto_busqueda):
        """
        Busca población por nombre de población.
        No usa query.size() porque devuelve -1 en muchos drivers.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 57
        else:
            id_pais = 64

        # SQL preparado con placeholders
        sql = """SELECT poblacion, provincia_region, cp, region_code
                 FROM poblaciones
                 WHERE id_pais = ? AND (poblacion LIKE ?)"""

        query = QSqlQuery(self.modelo.sqlite_model.db)
        query.prepare(sql)
        query.addBindValue(id_pais)
        query.addBindValue(f"%{texto_busqueda}%")

        if not query.exec():
            print(f"❌ Error SQL: {query.lastError().text()}")
            return

        # Recolectamos todas las filas (query.size() no funciona bien)
        filas = []
        while query.next():
            filas.append({
                "poblacion": query.value("poblacion"),
                "provincia_region": query.value("provincia_region"),
                "cp": query.value("cp"),
            })

        print(f"🔍 Búsqueda Población '{texto_busqueda}' en país {id_pais}: {len(filas)} resultados")

        # Sin resultados
        if len(filas) == 0:
            return

        # 1 resultado: rellenar directamente
        if len(filas) == 1:
            fila = filas[0]
            self.vista.poblacion.setText(str(fila["poblacion"] or ""))
            self.vista.cp.setText(str(fila["cp"] or ""))

            if pais_text == "España":
                self.vista.provincia.setText(str(fila["provincia_region"] or ""))
            return

        # Múltiples resultados: abrir selector
        self.abrir_selector_poblaciones(texto_busqueda)

    def abrir_selector_poblaciones_CP(self, sql_filtro=""):

        # Reutilizamos tu clase genérica
        buscador = DBConsultaView(self.modelo.sqlite_model.db)

        pais_text = self.vista.pais.text()
        if pais_text == "España":
            id_pais = 57
        else:
            id_pais = 64

        sql_base = f"SELECT id, cp, poblacion, provincia_region FROM poblaciones WHERE id_pais = {id_pais}"

        if sql_filtro:
            sql_base += f" AND cp = '{sql_filtro}'"

        buscador.set_config(
            titulo="Seleccione Localidad",
            sql_base=sql_base,
            campos_busqueda=["cp"],
            headers=["ID", "C.P.", "Población", "Provincia/Región"]
        )

        # Ajustamos tamaños: ID oculto, CP pequeño, Población grande, Código región pequeño
        buscador.set_tamano_columnas([0, 80, 250, 200])

        if buscador.exec():
            # Actualizamos la vista de empresas
            self.vista.poblacion.setText(buscador.registro.value("poblacion"))
            if self.vista.pais == "España":
                self.vista.provincia.setText(buscador.registro.value("provincia_region"))

    def abrir_selector_poblaciones(self, sql_filtro=""):

        # Reutilizamos tu clase genérica
        buscador = DBConsultaView(self.modelo.sqlite_model.db)

        pais_text = self.vista.pais.text()
        if pais_text == "España":
            id_pais = 57
        else:
            id_pais = 64

        sql_base = f"SELECT id, cp, poblacion, provincia_region FROM poblaciones WHERE id_pais = {id_pais}"

        if sql_filtro:
            sql_base += f" AND poblacion like '%{sql_filtro}%'"

        buscador.set_config(
            titulo="Seleccione Localidad",
            sql_base=sql_base,
            campos_busqueda=["poblacion"],
            headers=["ID", "C.P.", "Población", "Provincia/Región"]
        )

        # Ajustamos tamaños: ID oculto, CP pequeño, Población grande, Código región pequeño
        buscador.set_tamano_columnas([0, 80, 250, 200])

        if buscador.exec():
            # Actualizamos la vista de empresas
            self.vista.cp.setText(buscador.registro.value("cp"))
            self.vista.poblacion.setText(buscador.registro.value("poblacion"))
            if self.vista.pais == "España":
                self.vista.provincia.setText(buscador.registro.value("provincia_region"))

    def validar_codigo_identificacion(self):
        # Evitar validaciones en cascada
        if self._validando:
            return

        pais_text = self.vista.pais.text()

        if (pais_text == "España"):
            identificador = self.vista.cif_siren.text().strip()

            # No validar si está vacío (evita errores al cargar datos)
            if not identificador:
                return

            es_valido = self.validador.validar_identidad_espana(identificador)
            if not es_valido:
                self._validando = True  # Bloquear otras validaciones
                titulo = QtCore.QCoreApplication.translate("EmpresaController", "Identificador no válido")
                mensaje = QtCore.QCoreApplication.translate("EmpresaController", "El CIF introducido no es válido según las reglas de España.")

                msg_box = QMessageBox(self.vista)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle(titulo)
                msg_box.setText(mensaje)
                aplicar_estilo_messagebox(msg_box, "warning")
                msg_box.exec()

                self._validando = False  # Desbloquear
                # Devolver el foco al campo erróneo para que el usuario lo corrija
                self.vista.cif_siren.setFocus()
                return
        else:
            siren = self.vista.cif_siren.text().strip()

            # No validar si está vacío (evita errores al cargar datos)
            if not siren:
                return

            es_siren_valido = self.validador.validar_siren(siren)

            if not es_siren_valido:
                self._validando = True  # Bloquear otras validaciones
                titulo = QtCore.QCoreApplication.translate("EmpresaController", "Identificador no válido")
                mensaje = QtCore.QCoreApplication.translate("EmpresaController", "El SIREN introducido no es válido según las reglas de Francia.")

                msg_box = QMessageBox(self.vista)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle(titulo)
                msg_box.setText(mensaje)
                aplicar_estilo_messagebox(msg_box, "warning")
                msg_box.exec()

                self._validando = False  # Desbloquear
                # Devolver el foco al campo erróneo para evitar que se dispare validar_siret()
                self.vista.cif_siren.setFocus()
                return


    def validar_siret(self):
        # Evitar validaciones en cascada
        if self._validando:
            return

        pais_text = self.vista.pais.text()
        if pais_text != "España":
            siret = self.vista.siret.text().strip()

            # No validar si está vacío (evita errores al cargar datos)
            if not siret:
                return

            es_siret_valido = self.validador.validar_siret(siret)
            if not es_siret_valido:
                self._validando = True  # Bloquear otras validaciones
                titulo = QtCore.QCoreApplication.translate("EmpresaController", "Identificador no válido")
                mensaje = QtCore.QCoreApplication.translate("EmpresaController", "El SIRET introducido no es válido según las reglas de Francia.")

                msg_box = QMessageBox(self.vista)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle(titulo)
                msg_box.setText(mensaje)
                aplicar_estilo_messagebox(msg_box, "warning")
                msg_box.exec()

                self._validando = False  # Desbloquear
                # Devolver el foco al campo erróneo
                self.vista.siret.setFocus()
                return
    def probar_conexion_mariadb(self):
        contexto = "EmpresaController"
        host = self.vista.mariadb_host.text().strip()
        puerto = self.vista.mariadb_port.value()
        usuario = self.vista.mariadb_user.text().strip()
        password = self.vista.mariadb_password.text()
        nombre_bd = self.vista.mariadb_name.text().strip()

        exito, mensaje = self.modelo.probar_conexion_mariadb(host, puerto, usuario, password, nombre_bd)

        if exito:
            titulo = QtCore.QCoreApplication.translate(contexto, "Conexión exitosa")
            msg = QtCore.QCoreApplication.translate(contexto, "La conexión a la base de datos MariaDB fue exitosa.")
            icono = QMessageBox.Information
            tipo_msg = "information"
        else:
            titulo = QtCore.QCoreApplication.translate(contexto, "Error de conexión")
            msg = QtCore.QCoreApplication.translate(contexto, f"No se pudo conectar a la base de datos MariaDB:\n\n{mensaje}")
            icono = QMessageBox.Critical
            tipo_msg = "critical"

        msg_box = QMessageBox(self.vista)
        msg_box.setIcon(icono)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(msg)
        aplicar_estilo_messagebox(msg_box, tipo_msg)
        msg_box.exec()

    # Crear base de datos para la empresa seleccionada (MariaDB/PostgreSQL)
    def preparar_base_datos_mariadb(self):
        """
        Crea la base de datos usando Qt SQL (QMYSQL o QPSQL driver).
        Compatible con QTableView y QSqlTableModel.
        Detecta automáticamente el motor y usa el script SQL correcto.
        """
        db_name = self.vista.mariadb_name.text().strip()

        # Detectar motor de BD desde la pestaña activa o config
        # Por ahora asumimos MariaDB (puedes añadir lógica para detectar)
        motor_bd = "mariadb"  # TODO: detectar desde vista si hay selector

        # Ruta al script SQL específico según el motor
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

        if motor_bd == "postgresql":
            ruta_sql = os.path.join(project_root, "database", "init_empresa_postgresql.sql")
            driver_qt = "QPSQL"
        else:  # mariadb/mysql
            ruta_sql = os.path.join(project_root, "database", "init_empresa_mariadb.sql")
            driver_qt = "QMYSQL"

        # 1. Configuración de parámetros
        host = self.vista.mariadb_host.text().strip()
        user = self.vista.mariadb_user.text().strip()
        pasw = self.vista.mariadb_password.text().strip()

        try:
            puerto = int(self.vista.mariadb_port.text().strip() or 3306)
        except ValueError:
            puerto = 3306

        # 2. Conexión inicial al SERVIDOR (sin especificar DB aún)
        # Usamos "temp_conn" para no pisar la conexión principal si ya existiera
        temp_db = QSqlDatabase.addDatabase(driver_qt, "temp_conn")
        temp_db.setHostName(host)
        temp_db.setUserName(user)
        temp_db.setPassword(pasw)
        temp_db.setPort(puerto)

        if not temp_db.open():
            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(f"No se pudo conectar al servidor {motor_bd.upper()}:\n{temp_db.lastError().text()}")
            msg_box.exec()
            return

        # 3. Verificar si existe la DB
        query = QSqlQuery(temp_db)
        query.exec(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{db_name}'")

        if query.next():
            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Aviso")
            msg_box.setText(f"La base de datos '{db_name}' ya existe.")
            msg_box.exec()
            temp_db.close()
            QSqlDatabase.removeDatabase("temp_conn")
            return

        # 4. Crear DB y ejecutar Script
        if motor_bd == "postgresql":
            # PostgreSQL usa CREATE DATABASE sin opciones de charset
            crear_db_sql = f"CREATE DATABASE {db_name}"
        else:
            # MariaDB/MySQL con charset y collation
            crear_db_sql = f"CREATE DATABASE `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"

        if query.exec(crear_db_sql):
            query.exec(f"USE `{db_name}`") if motor_bd != "postgresql" else query.exec(f"\\c {db_name}")

            if self.ejecutar_script_sql(query, ruta_sql):
                msg_box = QMessageBox(self.vista)
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Éxito")
                msg_box.setText(f"Base de datos '{db_name}' y tablas creadas correctamente.")
                msg_box.exec()

                # --- AHORA QUE LA DB EXISTE ---
                # Cerramos la conexión temporal
                temp_db.close()
                QSqlDatabase.removeDatabase("temp_conn")

                # Creamos la conexión oficial Default que usarán todos los QSqlTableModels
                self.db_principal = QSqlDatabase.addDatabase(driver_qt)  # Sin nombre = Default
                self.db_principal.setHostName(host)
                self.db_principal.setUserName(user)
                self.db_principal.setPassword(pasw)
                self.db_principal.setPort(puerto)
                self.db_principal.setDatabaseName(db_name)

                if not self.db_principal.open():
                    msg_box = QMessageBox(self.vista)
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setWindowTitle("Advertencia")
                    msg_box.setText(f"BD creada pero no se pudo abrir la conexión principal:\n{self.db_principal.lastError().text()}")
                    msg_box.exec()
            else:
                msg_box = QMessageBox(self.vista)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Error Parcial")
                msg_box.setText("BD creada pero falló la ejecución del script SQL.")
                msg_box.exec()
        else:
            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(f"No se pudo crear la base de datos:\n{query.lastError().text()}")
            msg_box.exec()

        temp_db.close()
        QSqlDatabase.removeDatabase("temp_conn")

    def ejecutar_script_sql(self, query_obj, ruta):
        """Lee el archivo .sql y ejecuta comando por comando"""
        if not os.path.exists(ruta):
            message = f"Archivo no encontrado en: {ruta}"
            QMessageBox.critical(self.vista, "ERROR CRITICO", message)
            return False

        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                # Quitamos comentarios y unimos líneas
                sql_completo = ""
                for linea in f:
                    if not linea.strip().startswith("--") and linea.strip():
                        sql_completo += linea

                # Separamos por punto y coma y ejecutamos cada instrucción
                comandos = sql_completo.split(';')
                for comando in comandos:
                    if comando.strip():
                        if not query_obj.exec(comando):
                            print(f"Fallo en: {comando[:50]}... Error: {query_obj.lastError().text()}")
                            return False
                return True
        except Exception as e:
            print(f"Error leyendo el archivo: {e}")
            return False