import os

from PySide6 import QtCore
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import QMessageBox, QHeaderView

from helpers.mapeoCampos import MapeoCampos
from helpers.messagebox_styles import aplicar_estilo_messagebox
from modulos.ventas.view.clientes_view import ClientesView
from modulos.comun.view.DBConsultaView import DBConsultaView
from helpers.validadores import ValidadorFiscal


class ClientesController:
    def __init__(self, vista: ClientesView, modelo, session_data: dict):
        self.vista = vista
        self.modelo = modelo
        self.columnas_actuales = []
        self.session_data = session_data
        self.validador = ValidadorFiscal()
        self._validando = False  # Flag para evitar validaciones en cascada


        #conecto botones
        self.vista.btnGuardar.clicked.connect(self.guardar_datos)
        self.vista.btnDeshacer.clicked.connect(self.cargar_datos)
        self.vista.btnCerrar.clicked.connect(self.vista.close)

        #conecto señales de campos
        self.vista.cp.editingFinished.connect(self.buscar_poblacion_cp_handler)
        self.vista.poblacion.editingFinished.connect(self.buscar_poblacion_handler)
        self.vista.cif_nif_siret.editingFinished.connect(self.validar_codigo_identificacion)
        self.vista.siret.editingFinished.connect(self.validar_siret)

        # Desactivo campos que no deben editarse
        self.vista.pais.setReadOnly(True)

        #campos que dependen del pais seleccionado
        if (self.session_data.get("pais", "") == "España"):
            self.vista.provincia.setVisible(True)
            self.vista.lblProvincia.setVisible(True)
            self.vista.label_cif_siren.setText("CIF:")
            self.vista.label_siret.setVisible(False)
            self.vista.siret.setVisible(False)
            self.vista.irpf.setVisible(True)


        else:
            self.vista.provincia.setVisible(False)
            self.vista.lblProvincia.setVisible(False)
            self.vista.label_cif_siren.setText("SIREN:")
            self.vista.label_siret.setVisible(True)
            self.vista.siret.setVisible(True)
            self.vista.irpf.setVisible(False)

        self.cargar_tabla_principal()
        self.vista.stackedWidget.setCurrentIndex(1)

    def cargar_tabla_principal(self):
        # Obtenemos el modelo de datos
        tabla_model = self.modelo.get_todos_clientes()

        # Lo inyectamos directamente al QTableView de la UI
        # Asegúrate de que en el .ui el objeto se llama 'tabla_busquedas' o similar
        self.vista.tabla_busquedas.setModel(tabla_model)

        # Ajuste visual rápido: expandir columnas
        self.vista.tabla_busquedas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def cargar_datos(self):
        # 1. Obtenemos los datos del modelo (el ID viene del __init__)
        # El modelo debe devolver: (la_fila_de_datos, lista_nombres_columnas)
        fila, columnas = self.modelo.get_datos_cliente(self.id_empresa)

        if not fila:
            # Aquí puedes usar tu nuevo sistema de traducción
            ctx = "ClientesController"
            titulo = QtCore.QCoreApplication.translate(ctx, "Error de carga")
            msg = QtCore.QCoreApplication.translate(ctx, f"No se encontró el cliente con ID: {self.id_cliente}")

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
        contexto = "ClientesController"
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
        if self.modelo.actualizar_cliente(self.id_cliente, datos):
            titulo = QtCore.QCoreApplication.translate(contexto, "Éxito")
            mensaje = QtCore.QCoreApplication.translate(contexto, "Cliente actualizado correctamente")

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
