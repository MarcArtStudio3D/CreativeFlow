from PySide6 import QtCore
from PySide6.QtWidgets import QLineEdit, QTextEdit, QCheckBox, QComboBox, QSpinBox, QDoubleSpinBox, QMessageBox

from helpers.mapeoCampos import MapeoCampos
from modulos.empresas.view.EmpresaConfigView import EmpresaConfigView
from modulos.comun.view.DBConsultaView import DBConsultaView



class EmpresaController:
    def __init__(self, vista: EmpresaConfigView, modelo, id_empresa):
        self.vista = vista
        self.modelo = modelo
        self.id_empresa = id_empresa
        self.columnas_actuales = []


        #conecto botones
        self.vista.btn_guardar_nuevo.clicked.connect(self.guardar_datos)
        self.vista.btn_deshacer.clicked.connect(self.cargar_datos)
        self.vista.btn_salir.clicked.connect(self.vista.close)
        self.vista.btnBuscarPais.clicked.connect(self.abrir_selector_paises)

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
            QMessageBox.critical(self.vista, titulo, msg)
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
            QMessageBox.warning(self.vista,tit, msg)
            return

        # 2. Capturar (usando tu lógica espejo)
        datos = MapeoCampos.capturar_datos_vista(self.vista, self.columnas_actuales)

        # 3. Mandar al modelo
        if self.modelo.actualizar_empresa(self.id_empresa, datos):
            titulo = QtCore.QCoreApplication.translate(contexto, "Éxito")
            mensaje = QtCore.QCoreApplication.translate(contexto, "Empresa actualizada correctamente")
            QMessageBox.information(self.vista,titulo, mensaje)
        else:
            titulo = QtCore.QCoreApplication.translate(contexto, "Error")
            mensaje = QtCore.QCoreApplication.translate(contexto, "No se pudieron guardar los datos en la base de datos.")
            QMessageBox.critical(self.vista, titulo, mensaje)

    def abrir_selector_paises(self):

        #conectamos a la base de datos:
        from PySide6.QtSql import QSqlDatabase

        # Esto se hace una sola vez al arrancar
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("creativeflow.db")
        db.open()
        # Instanciamos el buscador genérico
        buscador = DBConsultaView(db)

        # Lo configuramos igual que hacías en C++
        buscador.set_config(
            titulo="Seleccione País",
            sql_base="SELECT id, nombre, iso FROM paises",
            campos_busqueda=["nombre", "iso"],
            headers=["ID", "País", "Código ISO"]
        )

        if buscador.exec():
            # Recuperamos el ID y el nombre
            id_pais = buscador.id_seleccionado
            nombre_pais = buscador.registro.value("nombre")

            # Actualizamos la vista de empresas
            self.vista.pais.setText(nombre_pais)
            # Guardamos el ID en alguna parte para el UPDATE