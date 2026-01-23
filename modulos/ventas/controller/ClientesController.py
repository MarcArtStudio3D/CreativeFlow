import os

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import QMessageBox, QHeaderView, QLineEdit, QTextEdit, QComboBox, QDateEdit

from colores import COLOR_NARANJA
from helpers.mapeoCampos import MapeoCampos
from helpers.messagebox_styles import aplicar_estilo_messagebox
from modulos.ventas.view.clientes_view import ClientesView
from modulos.comun.view.DBConsultaView import DBConsultaView
from helpers.validadores import ValidadorFiscal

import unicodedata
from PySide6.QtCore import QSortFilterProxyModel

class ClientesController:
    def __init__(self, vista: ClientesView, modelo, session_data: dict):
        self.vista = vista
        self.modelo = modelo
        self.columnas_actuales = []
        self.session_data = session_data
        self.validador = ValidadorFiscal()
        self._validando = False  # Flag para evitar validaciones en cascada
        self.set_edicion_bloqueada(True)  # Bloquea todos los campos al iniciar para solo lectura
        self.vista.id.setVisible(False)


        #conecto botones
        self.vista.btnCerrar.clicked.connect(self.vista.close)
        self.vista.btnSiguiente.clicked.connect(self.siguiente_nombre)
        self.vista.btnAnterior.clicked.connect(self.anterior_nombre)
        self.vista.btnBuscar.clicked.connect(self.mostrar_busqueda)
        self.vista.btnEditar.clicked.connect(self.editar_cliente)
        self.vista.btnGuardar.clicked.connect(self.guardar_datos)
        self.vista.btnDeshacer.clicked.connect(self.cargar_datos)
        self.vista.btnCerrar.clicked.connect(self.vista.close)

        #conecto señales de campos
        self.vista.cp.editingFinished.connect(self.buscar_poblacion_cp_handler)
        self.vista.poblacion.editingFinished.connect(self.buscar_poblacion_handler)
        self.vista.cif_nif_siren.editingFinished.connect(self.validar_codigo_identificacion)
        self.vista.siret.editingFinished.connect(self.validar_siret)

        self.vista.txtBuscar_cliente.textChanged.connect(self.filtrar_clientes)

        # Conectamos el doble clic de la tabla a la función de carga
        self.vista.tabla_busquedas.doubleClicked.connect(self.preparar_edicion_cliente)

        # Desactivo campos que no deben editarse
        #self.vista.pais.setReadOnly(True)
        self.vista.id_pais.setVisible(False)

        #campos que dependen del pais seleccionado
        if (self.session_data.get("pais", "") == "España"):
            self.vista.provincia_region.setVisible(True)
            self.vista.lblProvincia.setVisible(True)
            self.vista.label_cif_siren.setText("CIF:")
            self.vista.label_siret.setVisible(False)
            self.vista.siret.setVisible(False)
            self.vista.irpf.setVisible(True)


        else:
            self.vista.provincia_region.setVisible(False)
            self.vista.lblProvincia.setVisible(False)
            self.vista.label_cif_siren.setText("SIREN:")
            self.vista.label_siret.setVisible(True)
            self.vista.siret.setVisible(True)
            self.vista.irpf.setVisible(False)

        self.cargar_tabla_principal()
        self.vista.stackedWidget.setCurrentIndex(1)

    def set_edicion_bloqueada(self, bloquear=True):
        """
        Bloquea o desbloquea todos los campos de entrada de la ficha.
        """
        from PySide6.QtWidgets import QLineEdit, QTextEdit, QComboBox, QDateEdit

        widgets_a_bloquear = [QLineEdit, QTextEdit, QComboBox, QDateEdit]

        # Obtenemos la página 0 del stackedWidget
        pagina_edicion = self.vista.stackedWidget.widget(0)

        for tipo in widgets_a_bloquear:
            for widget in pagina_edicion.findChildren(tipo):
                # QLineEdit, QTextEdit y QDateEdit tienen setReadOnly
                if hasattr(widget, 'setReadOnly'):
                    widget.setReadOnly(bloquear)
                # QComboBox no tiene setReadOnly, usamos setEnabled
                else:
                    widget.setEnabled(not bloquear)

    """------------------------------------
    CARGAMOS LA TABLA PRINCIPAL DE CLIENTES
    ------------------------------------"""
    def cargar_tabla_principal(self):
        # Obtenemos el modelo de datos
        tabla_model = self.modelo.get_lista_clientes()

        # Lo inyectamos directamente al QTableView de la UI
        # Asegúrate de que en el ui el objeto se llama 'tabla_busquedas'
        self.vista.tabla_busquedas.setModel(tabla_model)

        # Ajuste visual rápido: expandir columnas
        self.vista.tabla_busquedas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Ajuste visual rápido: expandir columnas
        header = self.vista.tabla_busquedas.horizontalHeader()
        # Oculta la columna 0 (que suele ser la del ID)
        self.vista.tabla_busquedas.setColumnHidden(0, True)
        # Primero ponemos el modo en manual/fijo para esas columnas
        header.setStretchLastSection(False)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        header.setSectionResizeMode(4, QHeaderView.Fixed)
        header.setSectionResizeMode(5, QHeaderView.Fixed)


        # Luego definimos el ancho en píxeles

        self.vista.tabla_busquedas.setColumnWidth(3, 300)  # Email
        self.vista.tabla_busquedas.setColumnWidth(4, 200)  # teléfono
        self.vista.tabla_busquedas.setColumnWidth(5, 200)  # Poblacion

    def mostrar_busqueda(self):
        self.vista.stackedWidget.setCurrentIndex(1)
        self.vista.txtBuscar_cliente.setFocus()

    """------------------------------------
    CARGAMOS DATOS AUXILIARES EN COMBOS
    ------------------------------------"""
    def cargar_datos_auxiliares(self):
        """Carga todos los combos de la ficha de una sola vez."""

        # Definimos qué combo va con qué tabla
        configuracion = [
            (self.vista.id_divisa, "divisas","nombre_divisa"),
            (self.vista.id_idioma_documentos, "idiomas","idioma"),
            (self.vista.id_tarifa, "tarifas", "nombre_tarifa"),
            (self.vista.id_forma_pago, "formpago","forma_pago"),
            (self.vista.id_agente, "agentes","nombre"),
            (self.vista.id_transportista, "transportista","transportista"),
            (self.vista.grupo_iva, "tiposiva","nombre_interno")
        ]

        for combo, tabla, campo_nombre in configuracion:
            try:
                combo.clear()
                # Añadimos opción neutra para evitar el NOT NULL si el usuario no elige
                combo.addItem("--- Seleccione ---", None)

                datos = self.modelo.obtener_datos_tabla_auxiliar(tabla, campo_nombre)
                for id_reg, nombre in datos:
                    combo.addItem(str(nombre), id_reg)

            except Exception as e:
                print(f"Error cargando combo de {tabla}: {e}")

        print("✓ Todos los datos auxiliares cargados.")


    """--------------------------------------------------
    PREPARAMOS LA EDICIÓN AL HACER DOBLE CLIC EN LA TABLA
    --------------------------------------------------"""
    def preparar_edicion_cliente(self, index):

        try:
            # 1. Accedemos directamente al modelo que tiene la tabla ahora mismo
            # self.tabla_model es el QSqlQueryModel que asignamos en refrescar_tabla
            model = self.vista.tabla_busquedas.model()

            # 2. Obtenemos el ID (columna 0 de la fila donde se hizo doble clic)
            id_cliente = model.data(model.index(index.row(), 0))

            if id_cliente is not None:
                print(f"Editando cliente con ID: {id_cliente}")

                # 3. Cargamos los datos y cambiamos de pestaña
                self.cargar_datos(id_cliente)
                self.cargar_datos_auxiliares()
                self.vista.stackedWidget.setCurrentIndex(0)

        except Exception as e:
            print(f"Error al intentar editar: {e}")

    """-------------------------------------------
    VAMOS AL SIGUIENTE CLIENTE SEGÚN NOMBRE FISCAL
    -------------------------------------------"""
    def siguiente_nombre(self):
        # 1. Recuperamos el registro (tupla con fila y columnas)
        nombre_fiscal = self.vista.nombre_fiscal.text().strip()
        fila, columnas = self.modelo.buscar_cliente_por_nombre_fiscal(nombre_fiscal, 1)

        # 2. Verificamos que no sea None y que tenga datos
        if fila and len(fila) > 0:
            # Extraemos el ID (posición 0 de la fila)
            id_a_cargar = fila[0]

            # 3. Llamamos a cargar_datos enviando solo el ID
            self.cargar_datos(id_cliente=id_a_cargar)

    """----------------------------------------------
        VAMOS AL CLIENTE ANTERIOR SEGÚN NOMBRE FISCAL
    ----------------------------------------------"""
    def anterior_nombre(self):
        nombre_fiscal = self.vista.nombre_fiscal.text().strip()
        # 1. Recuperamos el registro (tupla con fila y columnas)
        fila, columnas = self.modelo.buscar_cliente_por_nombre_fiscal(nombre_fiscal, 2)

        # 2. Verificamos que no sea None y que tenga datos
        if fila and len(fila) > 0:
            # Extraemos el ID (posición 0 de la fila)
            id_a_cargar = fila[0]

            # 3. Llamamos a cargar_datos enviando solo el ID
            self.cargar_datos(id_cliente=id_a_cargar)

    """-----------------------------------------
    CARGAMOS LOS DATOS DE UN CLIENTE EN PANTALLA
    -----------------------------------------"""
    def cargar_datos(self, id_cliente=None):
        # 1. Obtenemos los datos del modelo (el ID viene del __init__)
        # El modelo debe devolver: (la_fila_de_datos, lista_nombres_columnas)
        fila, columnas = self.modelo.get_datos_cliente(id_cliente)

        if not fila:
            # Aquí puedes usar tu nuevo sistema de traducción
            ctx = "ClientesController"
            titulo = QtCore.QCoreApplication.translate(ctx, "Error de carga")
            msg = QtCore.QCoreApplication.translate(ctx, f"No se encontró el cliente con ID: {id_cliente}")

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



    def filtrar_clientes(self, texto):
        # Filtramos la tabla según el texto y el criterio seleccionado
        result = self.modelo.get_lista_clientes(self.vista.cboBuscarPor.currentText, texto)
        self.vista.tabla_busquedas.setModel(result)


    """------------------------------------
    GUARDAMOS LOS DATOS DEL CLIENTE EDITADO
    ------------------------------------"""
    def guardar_datos(self):
        contexto = "ClientesController"
        id_cliente = int(self.vista.id.text())  # Asumimos que la primera columna es el ID
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
        if self.modelo.actualizar_cliente(id_cliente, datos):
            titulo = QtCore.QCoreApplication.translate(contexto, "Éxito")
            mensaje = QtCore.QCoreApplication.translate(contexto, "Cliente actualizado correctamente")

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "information")
            msg_box.exec()
            self.modo_no_edicion()
        else:
            titulo = QtCore.QCoreApplication.translate(contexto, "Error")
            mensaje = QtCore.QCoreApplication.translate(contexto, "No se pudieron guardar los datos en la base de datos.")

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "critical")
            msg_box.exec()



    """------------------------------------
            PASAMOS A MODO EDICIÓN
    ------------------------------------"""
    def editar_cliente(self):
        self.set_edicion_bloqueada(False)
        # Activamos los botones de guardar y deshacer
        self.vista.btnGuardar.setEnabled(True)
        self.vista.btnDeshacer.setEnabled(True)

        # Desactivamos el resto de botones
        self.vista.btnCerrar.setEnabled(False)
        self.vista.btnSiguiente.setEnabled(False)
        self.vista.btnAnterior.setEnabled(False)
        self.vista.btnBuscar.setEnabled(False)

        # Desactivo campos no editables
        self.vista.codigo_cliente.setReadOnly(True)

        # Asigno el foco al primer campo editable
        self.vista.cif_nif_siren.setFocus()

    """------------------------------------
           PASAMOS A MODO NO EDICIÓN
    ------------------------------------"""

    def modo_no_edicion(self):
        self.set_edicion_bloqueada(True)
        # Activamos los botones de guardar y deshacer
        self.vista.btnGuardar.setEnabled(False)
        self.vista.btnDeshacer.setEnabled(False)

        # Desactivamos el resto de botones
        self.vista.btnCerrar.setEnabled(True)
        self.vista.btnSiguiente.setEnabled(True)
        self.vista.btnAnterior.setEnabled(True)
        self.vista.btnBuscar.setEnabled(True)

        # Desactivo campos no editables
        self.vista.codigo_cliente.setReadOnly(True)

    """------------------------------------
        ABRIMOS EL SELECTOR DE PAÍSES
    ------------------------------------"""
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

    """--------------------------------------------
    HANDLER PARA BUSCAR POBLACIÓN POR CÓDIGO POSTAL
    --------------------------------------------"""
    def buscar_poblacion_cp_handler(self):
        """Handler para editingFinished que obtiene el texto del campo cp"""
        cp = self.vista.cp.text().strip()
        poblacion = self.vista.poblacion.text().strip()
        if cp and not poblacion:  # Solo buscar si hay algo escrito
            self.buscar_poblacion_cp(cp)

    """------------------------------------
    BUSCAMOS POBLACIÓN POR CÓDIGO POSTAL
    ------------------------------------"""
    def buscar_poblacion_cp(self, texto_busqueda):
        """
        Busca población por código postal.
        No usa query.size() porque devuelve -1 en muchos drivers.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 1
        elif pais_text == "Francia":
            id_pais = 2

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

    """-------------------------------------
    HANDLER PARA BUSCAR POBLACIÓN POR NOMBRE
    -------------------------------------"""
    def buscar_poblacion_handler(self):
        """Handler para editingFinished que obtiene el texto del campo POBLACION"""
        cp = self.vista.cp.text().strip()
        poblacion = self.vista.poblacion.text().strip()
        if not cp and poblacion:  # Solo buscar si hay algo escrito
            self.buscar_poblacion(poblacion)

    """------------------------------------
    BUSCAMOS POBLACIÓN POR NOMBRE
    ------------------------------------"""
    def buscar_poblacion(self, texto_busqueda):
        """
        Busca población por nombre de población.
        No usa query.size() porque devuelve -1 en muchos drivers.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 1
        else:
            id_pais = 2

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

    """--------------------------------------------------------
    ABRIMOS EL SELECTOR DE LAS POBLACIONES DE UN  CÓDIGO POSTAL
    --------------------------------------------------------"""
    def abrir_selector_poblaciones_CP(self, sql_filtro=""):

        # Reutilizamos tu clase genérica
        buscador = DBConsultaView(self.modelo.sqlite_model.db)

        pais_text = self.vista.pais.text()
        if pais_text == "España":
            id_pais = 1
        else:
            id_pais = 2

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


    """------------------------------------
    ABRIMOS EL SELECTOR DE POBLACIONES
    ------------------------------------"""
    def abrir_selector_poblaciones(self, sql_filtro=""):

        # Reutilizamos tu clase genérica
        buscador = DBConsultaView(self.modelo.sqlite_model.db)

        pais_text = self.vista.pais.text()
        if pais_text == "España":
            id_pais = 1
        else:
            id_pais = 2

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

    """------------------------------------
    VALIDAMOS CIF/NIF/SIREN SEGÚN PAÍS
    ------------------------------------"""
    def validar_codigo_identificacion(self):
        # Evitar validaciones en cascada
        if self._validando:
            return

        pais_text = self.vista.pais.text()

        if (pais_text == "España"):
            identificador = self.vista.cif_nif_siren.text().strip()

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
                self.vista.cif_nif_siren.setFocus()
                return
        else:
            siren = self.vista.cif_nif_siren.text().strip()

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
                self.vista.cif_nif_siren.setFocus()
                return

    """------------------------------------
    VALIDAMOS SIRET si pais es Francia
    ------------------------------------"""
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
