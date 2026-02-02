from operator import index
import os
from turtle import title
import unicodedata

from PySide6 import QtCore
from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QHeaderView,
    QLineEdit,
    QMessageBox,
    QTextEdit,
)

from colores import COLOR_NARANJA
from helpers.mapeoCampos import MapeoCampos
from helpers.messagebox_styles import aplicar_estilo_messagebox
from helpers.validadores import ValidadorFiscal
from modulos.comun.view.DBConsultaView import DBConsultaView
from modulos.ventas.view.clientes_view import ClientesView


class ClientesController:
    def __init__(self, vista: ClientesView, modelo, session_data: dict):
        self.vista = vista
        self.modelo = modelo
        self.columnas_actuales = []
        self.session_data = session_data
        self.validador = ValidadorFiscal()
        self._validando = False  # Flag para evitar validaciones en cascada
        self._direcciones_tabla_connected = False  # Flag para evitar conexiones duplicadas
        self.set_edicion_bloqueada(
            True
        )  # Bloquea todos los campos al iniciar para solo lectura
        self.vista.id.setVisible(False)

        """------------------------------------
                CONEXIONES DE BOTONES
        -------------------------------------"""
        self.vista.btnCerrar.clicked.connect(self.vista.close)
        self.vista.btnSiguiente.clicked.connect(self.siguiente_nombre)
        self.vista.btnAnterior.clicked.connect(self.anterior_nombre)
        self.vista.btnBuscar.clicked.connect(self.mostrar_busqueda)
        self.vista.btnEditar.clicked.connect(self.editar_cliente)
        self.vista.btnGuardar.clicked.connect(self.guardar_datos)
        self.vista.btnDeshacer.clicked.connect(self.deshacer_cambios)
        self.vista.btnCerrar.clicked.connect(self.vista.close)
        self.vista.btnBorrar.clicked.connect(self.borrar_cliente)
        self.vista.btnBuscarPais.clicked.connect(self.abrir_selector_paises)
        self.vista.btnAnadir.clicked.connect(self.nuevo_cliente)
        self.vista.btnAnadirdireccion.clicked.connect(self.anadir_direccion_alternativa)
        self.vista.btnGuardardireccionAlternativa.clicked.connect(self.guardar_direccion_alternativa)
        

        # conecto señales de campos
        self.vista.cp.editingFinished.connect(self.buscar_poblacion_cp_handler)
        self.vista.poblacion.editingFinished.connect(self.buscar_poblacion_handler)
        self.vista.cif_nif_siren.editingFinished.connect(
            self.validar_codigo_identificacion
        )
        self.vista.siret.editingFinished.connect(self.validar_siret)
        #señales de campos de direcciones alternativas
        self.vista.cp_alternativa.editingFinished.connect(self.buscar_poblacion_cp_alternativa_handler)
        self.vista.poblacion_alternativa.editingFinished.connect(self.buscar_poblacion_alternativa_handler)
        self.vista.btnBuscarPaisAlternativo.clicked.connect(self.abrir_selector_paises_alternativo)

        self.vista.txtBuscar_cliente.textChanged.connect(self.filtrar_clientes)

        # Conectamos las tablas
        self.vista.tabla_busquedas.doubleClicked.connect(self.abrir_cliente_desde_tabla)
        self.vista.tbDirecciones_alternativas.clicked.connect(self.abrir_direccion_alternativa_desde_tabla)

        # Desactivo campos que no deben editarse
        # self.vista.pais.setReadOnly(True)
        self.vista.id_pais.setVisible(False)
        self.vista.id_pais_alternativo.setVisible(False)
        self.vista.id_agente.setVisible(False)
        self.vista.id_transportista.setVisible(False)
        self.vista.id_forma_pago.setVisible(False)
        self.vista.id_idioma_documentos.setVisible(False)

        # Desactivar campos dirección alternativa
        self.vista.descripcion_direccion_alternativa.setReadOnly(False)
        self.vista.cp_alternativa.setReadOnly(False)
        self.vista.poblacion_alternativa.setReadOnly(False)
        self.vista.direccion_alternativa1.setReadOnly(False)
        self.vista.direccion_alternativa2.setReadOnly(False) 
        self.vista.provincia_alternativa.setReadOnly(False)
        self.vista.email_alternativa.setReadOnly(False)
        self.vista.pais_alternativo.setReadOnly(False)
        self.vista.comentarios_alternativa.setReadOnly(False)
        self.cargar_tabla_principal()
        self.vista.stackedWidget.setCurrentIndex(1)


    """--------------------------------------------
    BLOQUEAMOS O DESBLOQUEAMOS CAMPOS DE EDICIÓN
    --------------------------------------------"""
    def set_edicion_bloqueada(self, bloquear=True):
        """
        Bloquea o desbloquea todos los campos de entrada de la ficha.
        """
        from PySide6.QtWidgets import QComboBox, QDateEdit, QLineEdit, QTextEdit

        widgets_a_bloquear = [QLineEdit, QTextEdit, QComboBox, QDateEdit]

        # Obtenemos la página 0 del stackedWidget
        pagina_edicion = self.vista.stackedWidget.widget(0)

        for tipo in widgets_a_bloquear:
            for widget in pagina_edicion.findChildren(tipo):
                # QLineEdit, QTextEdit y QDateEdit tienen setReadOnly
                if hasattr(widget, "setReadOnly"):
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
        self.vista.tabla_busquedas.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Ajuste visual rápido: expandir columnas
        header = self.vista.tabla_busquedas.horizontalHeader()
        # Oculta la columna 0 (que suele ser la del ID)
        self.vista.tabla_busquedas.setColumnHidden(0, True)
        # Primero ponemos el modo en manual/fijo para esas columnas
        header.setStretchLastSection(False)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)

        # Luego definimos el ancho en píxeles

        self.vista.tabla_busquedas.setColumnWidth(3, 300)  # Email
        self.vista.tabla_busquedas.setColumnWidth(4, 200)  # teléfono
        self.vista.tabla_busquedas.setColumnWidth(5, 200)  # Poblacion

    def mostrar_busqueda(self):
        self.vista.stackedWidget.setCurrentIndex(1)
        self.vista.txtBuscar_cliente.setFocus()

    """--------------------------------------------
    ACTIVAMOS CAMPOS SEGUN PAIS DE  LA EMPRESA
    -------------------------------------------"""

    def activar_campos_segun_pais(self):
        # campos que dependen del pais seleccionado
        if self.vista.pais.text() == "España":
            self.vista.provincia_region.setVisible(True)
            self.vista.lblProvincia.setVisible(True)
            self.vista.label_cif_siren.setText("CIF:")
            self.vista.label_siret.setVisible(False)
            self.vista.siret.setVisible(False)
            self.vista.irpf.setVisible(True)
            self.vista.recargo_equivalencia.setVisible(True)
            self.vista.lblSegundoApellido.setVisible(True)
            self.vista.apellido2.setVisible(True)

        else:
            self.vista.provincia_region.setVisible(False)
            self.vista.lblProvincia.setVisible(False)
            self.vista.label_cif_siren.setText("SIREN:")
            self.vista.label_siret.setVisible(True)
            self.vista.siret.setVisible(True)
            self.vista.irpf.setVisible(False)
            self.vista.recargo_equivalencia.setVisible(False)
            self.vista.lblSegundoApellido.setVisible(False)
            self.vista.apellido2.setVisible(False)

    """------------------------------------
        CARGAMOS DATOS AUXILIARES EN COMBOS
    ------------------------------------"""

    def cargar_datos_auxiliares(self):
        """Carga todos los combos de la ficha de una sola vez."""

        # Definimos qué combo va con qué tabla
        configuracion = [
            (self.vista.id_divisa, "divisas", "id,nombre_divisa"),
            (self.vista.id_idioma_documentos, "idiomas", "id,idioma"),
            (self.vista.id_tarifa, "codigotarifa", "id,descripcion"),
            (self.vista.id_forma_pago, "formpago", "id,forma_pago"),
            (self.vista.grupo_iva, "tiposiva", "id,descripcion_tipo_iva"),
        ]

        for combo, tabla, campo_nombre in configuracion:
            try:
                combo.clear()
                combo.addItem("--- Seleccione ---", None)

                datos = self.modelo.obtener_datos_tabla_auxiliar(tabla, campo_nombre)
                
                # 'campos' es algo como "id,nombre_divisa"
                # Separamos para saber los nombres de las llaves del diccionario
                lista_campos = campo_nombre.split(",") 
                id_key = lista_campos[0].strip()   # "id"
                nombre_key = lista_campos[1].strip() # "nombre_a_mostrar"

                for fila in datos:
                    # Ahora accedemos al diccionario por sus llaves
                    nombre_valor = fila.get(nombre_key)
                    id_valor = fila.get(id_key)
                    
                    combo.addItem(str(nombre_valor), id_valor)

            except Exception as e:
                print(f"Error cargando combo de {tabla}: {e}")

        print("✓ Todos los datos auxiliares cargados.")

    """--------------------------------------------------------------
    Cargamos los datos de un cliente al hacer doble clic en la tabla
    --------------------------------------------------------------"""
    def abrir_cliente_desde_tabla(self, index):
        """Abre un cliente para edición cuando se hace doble clic en la tabla de búsqueda."""
        try:
            # 1. Accedemos directamente al modelo que tiene la tabla ahora mismo
            # self.tabla_model es el QSqlQueryModel que asignamos en refrescar_tabla
            model = self.vista.tabla_busquedas.model()

            # 2. Obtenemos el ID (columna 0 de la fila donde se hizo doble clic)
            id_cliente = model.data(model.index(index.row(), 0))

            if id_cliente is not None:
                print(f"Editando cliente con ID: {id_cliente}")

                # 3. Cargamos los datos y cambiamos de pestaña
                self.cargar_datos_auxiliares()
                self.cargar_datos(id_cliente)
                self.activar_campos_segun_pais()
                self.vista.stackedWidget.setCurrentIndex(0)

        except Exception as e:
            print(f"Error al intentar editar: {e}")

    def abrir_direccion_alternativa_desde_tabla(self, index):
        try:
            # 1. Accedemos directamente al modelo que tiene la tabla ahora mismo
            # self.tabla_model es el QSqlQueryModel que asignamos en refrescar_tabla
            model = self.vista.tbDirecciones_alternativas.model()

            # 2. Obtenemos el ID (columna 0 de la fila donde se hizo doble clic)
            id = model.data(model.index(index.row(), 0))

            if id is not None:
                
                # Cargamos los datos de la dirección alternativa
               
                self.cargar_datos_direccion_alternativa(id)
                
        except Exception as e:
            print(f"Error al cargar dirección alternativa: {e}")

    #----------------------------------------------------------------------------
    # Carga los datos de una dirección alternativa en los campos correspondientes
    #----------------------------------------------------------------------------
    def cargar_datos_direccion_alternativa(self, id):
        registro = self.modelo.get_datos_direccion_alternativa(id)

        if not registro:
            return

        # Mapeamos los datos a los campos correspondientes
        """Rellena la vista usando los datos de la fila de la BD."""
        if not registro: return

        datos = registro
        #for nombre_col, valor in datos.items():
        self.vista.poblacion_alternativa.setText(str(datos.get("poblacion", "")))

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
            self.activar_campos_segun_pais()

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
            self.activar_campos_segun_pais()

    """-----------------------------------------
    CARGAMOS LOS DATOS DE UN CLIENTE EN PANTALLA
    -----------------------------------------"""
    def cargar_datos(self, id_cliente=None):
        # 1. Obtenemos los datos del modelo (el ID viene del __init__)
        # El modelo debe devolver: (la_fila_de_datos, lista_nombres_columnas)
        if id_cliente is None:
            id_cliente = int(self.vista.id.text())
        fila, columnas = self.modelo.get_datos_cliente(id_cliente)

        if not fila:
            # Aquí puedes usar tu nuevo sistema de traducción
            ctx = "ClientesController"
            titulo = QtCore.QCoreApplication.translate(ctx, "Error de carga")
            msg = QtCore.QCoreApplication.translate(
                ctx, f"No se encontró el cliente con ID: {id_cliente}"
            )

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
        self.vista.lbl_nombre_fiscal.setText(self.vista.nombre_fiscal.text().upper())

        # 3. Guardamos las columnas para cuando toque capturar los datos al guardar
        self.columnas_actuales = columnas

        #-------------------------------------------------------
        # Verificamos si hay datos de direcciones alternativas.
        #-------------------------------------------------------
        fila, columnas = self.modelo.get_direcciones_alternativas_cliente(id_cliente)
        """Rellena la vista usando los datos de la fila de la BD."""
        if not fila:
            return

        # QTableView usa modelo: obtener o crear QStandardItemModel y rellenarlo
        table_view = self.vista.tbDirecciones_alternativas
        model = table_view.model()
        if not isinstance(model, QStandardItemModel):
            model = QStandardItemModel(table_view)
            table_view.setModel(model)
            # Conectar señal para navegación con teclado (flechas) solo la primera vez
            if not self._direcciones_tabla_connected:
                table_view.selectionModel().currentChanged.connect(self.abrir_direccion_alternativa_desde_tabla)
                self._direcciones_tabla_connected = True
        
        # Limpiar modelo
        model.removeRows(0, model.rowCount())
        model.setColumnCount(0)
        
        # Configurar encabezados
        if columnas:
            model.setHorizontalHeaderLabels(columnas)

        if fila and columnas and "id" in columnas and "descripcion" in columnas:
            # Si retorna una lista de filas, procesar todas
            if isinstance(fila[0], (list, tuple)):
                for una_fila in fila:
                    items = [QStandardItem(str(valor) if valor is not None else "") for valor in una_fila]
                    model.appendRow(items)
            else:
                # Única dirección alternativa
                items = [QStandardItem(str(valor) if valor is not None else "") for valor in fila]
                model.appendRow(items)
        
        # Ocultar la primera columna (id) y ajustar el ancho de las demás
        table_view.setColumnHidden(0, True)
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.setSelectionBehavior(table_view.SelectionBehavior.SelectRows)
        table_view.setSelectionMode(table_view.SelectionMode.SingleSelection)

    #------------------------------
    #    AÑADIR NUEVO CLIENTE
    #------------------------------
    def nuevo_cliente(self):
        # Lista de campos a limpiar (columnas de la tabla clientes)
        campos_cliente = [
            'codigo_cliente', 'id_divisa', 'id_empresa', 'id_idioma_documentos',
            'nombre', 'apellido1', 'apellido2', 'nombre_fiscal', 'nombre_comercial', 
            'persona_contacto', 'cif_nif_siret', 'cif_vies', 'direccion1', 'direccion2',
            'cp', 'poblacion', 'provincia_region', 'id_pais', 'telefono1', 'telefono2',
            'movil', 'email', 'web', 'id_tipo_cliente', 'id_tarifa', 'id_forma_pago',
            'dia_pago1', 'dia_pago2', 'porc_dto_cliente', 'recargo_equivalencia', 'irpf',
            'grupo_iva', 'iban', 'bic_swift', 'acumulado_ventas', 'ventas_ejercicio',
            'riesgo_maximo', 'deuda_actual', 'importe_a_cuenta', 'importe_pendiente',
            'id_agente', 'id_transportista', 'bloqueado', 'comentario_bloqueo',
            'fecha_alta', 'fecha_ultima_compra', 'fecha_nacimiento', 'acceso_web',
            'password_web', 'id_web', 'comentarios', 'observaciones'
        ]
        
        # Limpiamos la vista usando MapeoCampos
        MapeoCampos.limpiar_formulario(self.vista, campos_cliente)

        # Cargamos datos auxiliares en combos
        self.cargar_datos_auxiliares()

        # Ponemos el foco en el primer campo editable
        self.vista.pais.setFocus()

        # Pasamos a modo edición directamente
        self.editar_cliente()   

    #------------------------------------
    #            FILTRAR CLIENTES
    #------------------------------------

    def filtrar_clientes(self, texto):
        # Filtramos la tabla según el texto y el criterio seleccionado
        result = self.modelo.get_lista_clientes(
            self.vista.cboBuscarPor.currentText, texto
        )
        self.vista.tabla_busquedas.setModel(result)

    
    """------------------------------------
    GUARDAMOS LOS DATOS DEL CLIENTE EDITADO
    ------------------------------------"""

    def guardar_datos(self):
        contexto = "ClientesController"
        id_cliente = int(
            self.vista.id.text()
        )  # Asumimos que la primera columna es el ID
        # 1. Validar
        valido, campos_faltantes = MapeoCampos.validar_campos(self.vista)

        if not valido:
            msg = QtCore.QCoreApplication.translate(
                contexto, "Los siguientes campos son obligatorios:\n\n- "
            ) + "\n- ".join(campos_faltantes)
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
            mensaje = QtCore.QCoreApplication.translate(
                contexto, "Cliente actualizado correctamente"
            )

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "information")
            msg_box.exec()
            self.modo_no_edicion()
        else:
            titulo = QtCore.QCoreApplication.translate(contexto, "Error")
            mensaje = QtCore.QCoreApplication.translate(
                contexto, "No se pudieron guardar los datos en la base de datos."
            )

            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "critical")
            msg_box.exec()

    """------------------------------------
    DESHACEMOS LOS CAMBIOS REALIZADOS
    ------------------------------------"""

    def deshacer_cambios(self):
        id_cliente = int(self.vista.id.text())
        self.cargar_datos(id_cliente)
        self.modo_no_edicion()

    """------------------------------------
    BORRAMOS EL CLIENTE
    ------------------------------------"""

    def borrar_cliente(self):
        if (
            QMessageBox.question(
                self.vista,
                "Confirmar borrado",
                "¿Está seguro de que desea borrar este cliente?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            == QMessageBox.StandardButton.Yes
        ):
            id_cliente = int(self.vista.id.text())
            if (
                QMessageBox.warning(
                    self.vista,
                    "Confirmar borrado de cliente",
                    "¡Esta acción es irreversible!. ¿Desea continuar?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                )
                == QMessageBox.StandardButton.Yes
            ):
                if self.modelo.borrar_cliente(id_cliente):
                    QMessageBox.information(
                        self.vista,
                        "Cliente borrado",
                        "El cliente ha sido borrado correctamente.",
                    )
                    self.anterior_nombre()

                else:
                    QMessageBox.critical(
                        self.vista, "Error al borrar", "No se pudo borrar el cliente."
                    )
            else:
                QMessageBox.information(
                    self.vista, "Borrado cancelado", "Operación anulada."
                )

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
        self.vista.btnAnadir.setEnabled(False)
        self.vista.btnEditar.setEnabled(False)
        self.vista.btnBorrar.setEnabled(False)

        # Activo botones de direcciones alternativas
        self.vista.btnAnadirdireccion.setEnabled(True)
        self.vista.btnBorrardireccion.setEnabled(True)
        self.vista.btnEditardireccionAlternativa.setEnabled(True)
     
        # Desactivo campos no editables
        self.vista.codigo_cliente.setReadOnly(True)

        # Desactivar campos dirección alternativa
        self.vista.descripcion_direccion_alternativa.setReadOnly(False)
        self.vista.cp_alternativa.setReadOnly(False)
        self.vista.poblacion_alternativa.setReadOnly(False)
        self.vista.direccion_alternativa1.setReadOnly(False)
        self.vista.direccion_alternativa2.setReadOnly(False) 
        self.vista.provincia_alternativa.setReadOnly(False)
        self.vista.email_alternativa.setReadOnly(False)
        self.vista.pais_alternativo.setReadOnly(False)
        self.vista.comentarios_alternativa.setReadOnly(False)

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
        self.vista.btnEditar.setEnabled(True)
        self.vista.btnAnadir.setEnabled(False)
        self.vista.btnBorrar.setEnabled(False)
        self.vista.btnAnadirdireccion.setEnabled(False)
        self.vista.btnBorrardireccion.setEnabled(False)
        self.vista.btnEditardireccionAlternativa.setEnabled(False)
        self.vista.btnDeshacerdireccionAlternativa.setEnabled(False)

        # Desactivo campos no editables
        self.vista.codigo_cliente.setReadOnly(True)

    """------------------------------------
        ABRIMOS EL SELECTOR DE PAÍSES
    ------------------------------------"""

    def abrir_selector_paises(self):
        """
        Abre el selector de países usando db_maestros.
        """
        # Usamos db_maestros para paises
        db = self.modelo.db_maestros.db

        if not db or not db.isOpen():
            QMessageBox.critical(
                self.vista, "Error de conexión", "La base de datos maestros no está abierta"
            )
            return

        # Instanciamos el buscador genérico
        buscador = DBConsultaView(db)

        # Lo configuramos igual que hacías en C++
        buscador.set_config(
            titulo="Seleccione País",
            sql_base="SELECT id, pais, country_code FROM paises",
            campos_busqueda=["pais", "country_code"],
            headers=["ID", "País", "Código País"],
        )
        buscador.set_tamano_columnas([0, 600, 80])

        if buscador.exec():
            # Recuperamos el ID y el nombre
            id_pais = buscador.id_seleccionado
            nombre_pais = buscador.registro.value("pais")

            # Actualizamos la vista de empresas
            self.vista.pais.setText(nombre_pais)
            self.vista.id_pais.setText(str(id_pais))
            
    """---------------------------------------------------------
        ABRIMOS EL SELECTOR DE PAÍSES ALTERNATIVOS PARA DIRECCIONES
    --------------------------------------------------"""

    def abrir_selector_paises_alternativo(self):
        """
        Abre el selector de países usando db_maestros.
        """
        # Usamos db_maestros para paises
        db = self.modelo.db_maestros.db
        if not db or not db.isOpen():
            QMessageBox.critical(
                self.vista, "Error de conexión", "La base de datos maestros no está abierta"
            )
            return

        # Instanciamos el buscador genérico
        buscador = DBConsultaView(db)

        # Lo configuramos igual que hacías en C++
        buscador.set_config(
            titulo="Seleccione País para dirección alternativa",
            sql_base="SELECT id, pais, country_code FROM paises",
            campos_busqueda=["pais", "country_code"],
            headers=["ID", "País", "Código País"],
        )
        buscador.set_tamano_columnas([0, 600, 80])

        if buscador.exec():
            # Recuperamos el ID y el nombre
            id_pais = buscador.id_seleccionado
            nombre_pais = buscador.registro.value("pais")

            # Actualizamos la vista de empresas
            self.vista.pais_alternativo.setText(nombre_pais)
            self.vista.id_pais_alternativo.setText(str(id_pais))
            
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
        Busca población por código postal usando el modelo.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 1
        elif pais_text == "Francia":
            id_pais = 2
        else:
            print("⚠️ País no reconocido, no se puede buscar población")
            return

        # Llamamos al método del modelo (respetando MVC)
        poblaciones = self.modelo.buscar_poblaciones_por_cp(id_pais, texto_busqueda)

        print(f"🔍 Búsqueda CP '{texto_busqueda}' en país {id_pais}: {len(poblaciones)} resultados")

        # Sin resultados
        if len(poblaciones) == 0:
            return

        # 1 resultado: rellenar directamente
        if len(poblaciones) == 1:
            fila = poblaciones[0]
            self.vista.poblacion.setText(str(fila["poblacion"] or ""))
            self.vista.cp.setText(str(fila["cp"] or ""))

            if pais_text == "España":
                self.vista.provincia_region.setText(str(fila["provincia_region"] or ""))
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
        Busca población por nombre de población usando el modelo.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 1
        else:
            id_pais = 2

        # Llamamos al método del modelo (respetando MVC)
        filas = self.modelo.buscar_poblaciones_por_nombre(id_pais, texto_busqueda)

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
                self.vista.provincia_region.setText(str(fila["provincia_region"] or ""))
            return

        # Múltiples resultados: abrir selector
        self.abrir_selector_poblaciones(texto_busqueda)

    """--------------------------------------------------------
    ABRIMOS EL SELECTOR DE LAS POBLACIONES DE UN  CÓDIGO POSTAL
    --------------------------------------------------------"""

    def abrir_selector_poblaciones_CP(self, sql_filtro=""):
        # Usamos db_maestros para poblaciones
        buscador = DBConsultaView(self.modelo.db_maestros.db)

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
            headers=["ID", "C.P.", "Población", "Provincia/Región"],
        )

        # Ajustamos tamaños: ID oculto, CP pequeño, Población grande, Código región pequeño
        buscador.set_tamano_columnas([0, 80, 250, 200])

        if buscador.exec():
            # Actualizamos la vista de empresas
            self.vista.poblacion.setText(buscador.registro.value("poblacion"))
            if self.vista.pais.text() == "España":
                self.vista.provincia_region.setText(
                    buscador.registro.value("provincia_region")
                )

    """------------------------------------
    ABRIMOS EL SELECTOR DE POBLACIONES
    ------------------------------------"""

    def abrir_selector_poblaciones(self, sql_filtro=""):
        # Usamos db_maestros para poblaciones
        buscador = DBConsultaView(self.modelo.db_maestros.db)

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
            headers=["ID", "C.P.", "Población", "Provincia/Región"],
        )

        # Ajustamos tamaños: ID oculto, CP pequeño, Población grande, Código región pequeño
        buscador.set_tamano_columnas([0, 80, 250, 200])

        if buscador.exec():
            # Actualizamos la vista de empresas
            self.vista.cp.setText(buscador.registro.value("cp"))
            self.vista.poblacion.setText(buscador.registro.value("poblacion"))
            if self.vista.pais.text() == "España":
                self.vista.provincia_region.setText(
                    buscador.registro.value("provincia_region")
                )

    """--------------------------------------------
    HANDLER PARA BUSCAR POBLACIÓN ALTERNATIVA POR CÓDIGO POSTAL
    --------------------------------------------"""

    def buscar_poblacion_cp_alternativa_handler(self):
        """Handler para editingFinished que obtiene el texto del campo cp"""
        cp = self.vista.cp_alternativa.text().strip()
        poblacion = self.vista.poblacion_alternativa.text().strip()
        if cp and not poblacion:  # Solo buscar si hay algo escrito
            self.buscar_poblacion_cp_alternativa(cp)

    """------------------------------------
    BUSCAMOS POBLACIÓN ALTERNATIVA POR CÓDIGO POSTAL
    ------------------------------------"""

    def buscar_poblacion_cp_alternativa(self, texto_busqueda):
        """
        Busca población por código postal usando el modelo.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais_alternativo.text()

        if pais_text == "España":
            id_pais = 1
        elif pais_text == "Francia":
            id_pais = 2
        else:
            print("⚠️ País no reconocido, no se puede buscar población")
            return

        # Llamamos al método del modelo (respetando MVC)
        poblaciones = self.modelo.buscar_poblaciones_por_cp(id_pais, texto_busqueda)

        print(f"🔍 Búsqueda CP '{texto_busqueda}' en país {id_pais}: {len(poblaciones)} resultados")

        # Sin resultados
        if len(poblaciones) == 0:
            return

        # 1 resultado: rellenar directamente
        if len(poblaciones) == 1:
            fila = poblaciones[0]
            self.vista.poblacion_alternativa.setText(str(fila["poblacion"] or ""))
            self.vista.cp_alternativa.setText(str(fila["cp"] or ""))

            if pais_text == "España":
                self.vista.provincia_region.setText(str(fila["provincia_region"] or ""))
            return

        # Múltiples resultados: abrir selector
        self.abrir_selector_poblaciones_CP_alternativa(texto_busqueda)

    """-------------------------------------
    HANDLER PARA BUSCAR POBLACIÓN POR NOMBRE
    -------------------------------------"""

    def buscar_poblacion_alternativa_handler(self):
        """Handler para editingFinished que obtiene el texto del campo POBLACION"""
        cp = self.vista.cp_alternativa.text().strip()
        poblacion = self.vista.poblacion_alternativa.text().strip()
        if not cp and poblacion:  # Solo buscar si hay algo escrito
            self.buscar_poblacion_alternativa(poblacion)

    """------------------------------------
    BUSCAMOS POBLACIÓN POR NOMBRE
    ------------------------------------"""

    def buscar_poblacion_alternativa(self, texto_busqueda):
        """
        Busca población por nombre de población usando el modelo.
        """
        # Obtenemos el texto del widget pais correctamente
        pais_text = self.vista.pais.text()

        if pais_text == "España":
            id_pais = 1
        else:
            id_pais = 2

        # Llamamos al método del modelo (respetando MVC)
        filas = self.modelo.buscar_poblaciones_por_nombre(id_pais, texto_busqueda)

        print(f"🔍 Búsqueda Población '{texto_busqueda}' en país {id_pais}: {len(filas)} resultados")

        # Sin resultados
        if len(filas) == 0:
            return

        # 1 resultado: rellenar directamente
        if len(filas) == 1:
            fila = filas[0]
            self.vista.poblacion_alternativa.setText(str(fila["poblacion"] or ""))
            self.vista.cp.setText(str(fila["cp"] or ""))

            if pais_text == "España":
                self.vista.provincia_region_alternativa.setText(str(fila["provincia_region"] or ""))
            return

        # Múltiples resultados: abrir selector
        self.abrir_selector_poblaciones_alternativa(texto_busqueda)


    """----------------------------------------------------------------------
    ABRIMOS EL SELECTOR DE LAS POBLACIONES ALTERNATIVAS DE UN  CÓDIGO POSTAL
    ----------------------------------------------------------------------"""
    def abrir_selector_poblaciones_CP_alternativa(self, sql_filtro=""):
        # Usamos db_maestros para poblaciones
        buscador = DBConsultaView(self.modelo.db_maestros.db)

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
            headers=["ID", "C.P.", "Población", "Provincia/Región"],
        )

        # Ajustamos tamaños: ID oculto, CP pequeño, Población grande, Código región pequeño
        buscador.set_tamano_columnas([0, 80, 250, 200])

        if buscador.exec():
            # Actualizamos la vista de empresas
            self.vista.poblacion_alternativa.setText(buscador.registro.value("poblacion"))
            if self.vista.pais.text() == "España":
                self.vista.provincia_region_alternativa.setText(
                    buscador.registro.value("provincia_region")
                )

    """---------------------------------------------
    ABRIMOS EL SELECTOR DE POBLACIONES ALTERNATIVA      
    ---------------------------------------------"""

    def abrir_selector_poblaciones_alternativa(self, sql_filtro=""):
        # Usamos db_maestros para poblaciones
        buscador = DBConsultaView(self.modelo.db_maestros.db)

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
            headers=["ID", "C.P.", "Población", "Provincia/Región"],
        )

        # Ajustamos tamaños: ID oculto, CP pequeño, Población grande, Código región pequeño
        buscador.set_tamano_columnas([0, 80, 250, 200])

        if buscador.exec():
            # Actualizamos la vista de empresas
            self.vista.cp_alternativa.setText(buscador.registro.value("cp"))
            self.vista.poblacion_alternativa.setText(buscador.registro.value("poblacion"))
            if self.vista.pais.text() == "España":
                self.vista.provincia_region_alternativa.setText(
                    buscador.registro.value("provincia_region")
                )

    """------------------------------------
    VALIDAMOS CIF/NIF/SIREN SEGÚN PAÍS
    ------------------------------------"""

    def validar_codigo_identificacion(self):
        # Evitar validaciones en cascada
        if self._validando:
            return

        pais_text = self.vista.pais.text()

        if pais_text == "España":
            identificador = self.vista.cif_nif_siren.text().strip()

            # No validar si está vacío (evita errores al cargar datos)
            if not identificador:
                return

            es_valido = self.validador.validar_identidad_espana(identificador)
            if not es_valido:
                self._validando = True  # Bloquear otras validaciones
                titulo = QtCore.QCoreApplication.translate(
                    "EmpresaController", "Identificador no válido"
                )
                mensaje = QtCore.QCoreApplication.translate(
                    "EmpresaController",
                    "El CIF introducido no es válido según las reglas de España.",
                )

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
                titulo = QtCore.QCoreApplication.translate(
                    "EmpresaController", "Identificador no válido"
                )
                mensaje = QtCore.QCoreApplication.translate(
                    "EmpresaController",
                    "El SIREN introducido no es válido según las reglas de Francia.",
                )

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
    AÑADIMOS DIRECCIÓN ALTERNATIVA
    ------------------------------------"""
    def anadir_direccion_alternativa(self):
        # Habilitamos los campos de dirección alternativa
        self.vista.descripcion_direccion_alternativa.setReadOnly(False)
        self.vista.cp_alternativa.setReadOnly(False)
        self.vista.poblacion_alternativa.setReadOnly(False)
        self.vista.direccion_alternativa1.setReadOnly(False)
        self.vista.direccion_alternativa2.setReadOnly(False) 
        self.vista.provincia_alternativa.setReadOnly(False)
        self.vista.email_alternativa.setReadOnly(False)
        self.vista.pais_alternativo.setReadOnly(False)
        self.vista.comentarios_alternativa.setReadOnly(False)

        # Limpiamos los campos
        self.vista.descripcion_direccion_alternativa.clear()
        self.vista.cp_alternativa.clear()
        self.vista.poblacion_alternativa.clear()
        self.vista.direccion_alternativa1.clear()
        self.vista.direccion_alternativa2.clear()   
        self.vista.provincia_alternativa.clear()
        self.vista.email_alternativa.clear()
        self.vista.pais_alternativo.clear()
        self.vista.comentarios_alternativa.clear()
        

        #Deshabilitamos los botones de  añadir, editar y borrar dirección alternativa
        self.vista.btnAnadirdireccion.setEnabled(False)
        self.vista.btnEditardireccionAlternativa.setEnabled(False)
        self.vista.btnBorrardireccion.setEnabled(False)     

        # Habilitamos los botones relacionados
        self.vista.btnGuardardireccionAlternativa.setEnabled(True)
        self.vista.btnDeshacerdireccionAlternativa.setEnabled(True)


        #impedimos que se guarde el cliente mientras se edita la dirección alternativa
        self.vista.btnGuardar.setEnabled(False)
        self.vista.btnDeshacer.setEnabled(False)

        # Ponemos el foco en el primer campo de dirección alternativa
        self.vista.descripcion_direccion_alternativa.setFocus()


    """------------------------------------
    GUARDAMOS LA DIRECCIÓN ALTERNATIVA
    ------------------------------------"""
    def guardar_direccion_alternativa(self):
        self.vista.descripcion_direccion_alternativa.setReadOnly(True)
        self.vista.cp_alternativa.setReadOnly(True)
        self.vista.poblacion_alternativa.setReadOnly(True)
        self.vista.direccion_alternativa1.setReadOnly(True)
        self.vista.direccion_alternativa2.setReadOnly(True) 
        self.vista.provincia_alternativa.setReadOnly(True)
        self.vista.email_alternativa.setReadOnly(True)
        self.vista.pais_alternativo.setReadOnly(True)
        self.vista.comentarios_alternativa.setReadOnly(True)

        # Habilitamos los botones de añadir, editar y borrar dirección alternativa
        self.vista.btnAnadirdireccion.setEnabled(True)
        self.vista.btnEditardireccionAlternativa.setEnabled(True)
        self.vista.btnBorrardireccion.setEnabled(True)     

        # Deshabilitamos los botones relacionados
        self.vista.btnGuardardireccionAlternativa.setEnabled(False)
        self.vista.btnDeshacerdireccionAlternativa.setEnabled(False)

        # Permitimos que se guarde el cliente nuevamente
        self.vista.btnGuardar.setEnabled(True)
        self.vista.btnDeshacer.setEnabled(True)

        DireccionAlternativa = {
            "id_cliente": int(self.vista.id.text().strip()),
            "descripcion": self.vista.descripcion_direccion_alternativa.text().strip(),
            "cp": self.vista.cp_alternativa.text().strip(),
            "poblacion": self.vista.poblacion_alternativa.text().strip(),
            "direccion1": self.vista.direccion_alternativa1.text().strip(),
            "direccion2": self.vista.direccion_alternativa2.text().strip(),
            "provincia_region": self.vista.provincia_alternativa.text().strip(),
            "id_pais": int(self.vista.id_pais_alternativo.text().strip()),
            "email": self.vista.email_alternativa.text().strip(),
            "comentarios": self.vista.comentarios_alternativa.toPlainText().strip(),
        }     
        if self.modelo.guardar_direccion_alternativa(DireccionAlternativa,nuevo_cliente=True):
            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Info)
            titulo = "DIRECCIONES ALTERNATIVAS"
            mensaje = "LA DIRECCIÓN SE HA GUARDADO CORRECTAMENTE"
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "warning")
            msg_box.exec()

        else:
            msg_box = QMessageBox(self.vista)
            msg_box.setIcon(QMessageBox.Warning)
            titulo = "DIRECCIONES ALTERNATIVAS"
            mensaje = "LA DIRECCIÓN NO SE HA PODIDO GIARDAR"
            msg_box.setWindowTitle(titulo)
            msg_box.setText(mensaje)
            aplicar_estilo_messagebox(msg_box, "warning")
            msg_box.exec()


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
                titulo = QtCore.QCoreApplication.translate(
                    "EmpresaController", "Identificador no válido"
                )
                mensaje = QtCore.QCoreApplication.translate(
                    "EmpresaController",
                    "El SIRET introducido no es válido según las reglas de Francia.",
                )

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
