from PySide6.QtWidgets import QLineEdit, QTextEdit, QCheckBox, QComboBox

class EmpresaController:
    def __init__(self, vista, modelo, id_empresa):
        self.vista = vista
        self.modelo = modelo
        self.id_empresa = id_empresa

        # Solo cargamos datos si hay un id_empresa válido (no modo admin)
        if self.id_empresa and self.id_empresa > 0:
            self.cargar_datos()

    def cargar_datos(self):
        fila, columnas = self.modelo.get_datos_empresa(self.id_empresa)
        if not fila:
            print(f"No se encontraron datos para la empresa ID {self.id_empresa}")
            return

        # Recorremos todas las columnas de la base de datos
        for i, nombre_columna in enumerate(columnas):
            valor = fila[i]

            # Buscamos si existe un widget con el nombre de la columna
            # Si usaste prefijos en Designer, cambia a: getattr(self.vista, f"ent_{nombre_columna}", None)
            widget = getattr(self.vista, nombre_columna, None)

            if widget:
                self.set_widget_value(widget, valor)

    def set_widget_value(self, widget, valor):
        texto = str(valor) if valor is not None else ""

        if isinstance(widget, QLineEdit):
            widget.setText(texto)
        elif isinstance(widget, QTextEdit):
            widget.setPlainText(texto)
        elif isinstance(widget, QCheckBox):
            widget.setChecked(bool(valor))
        elif isinstance(widget, QComboBox):
            index = widget.findText(texto)
            if index >= 0: widget.setCurrentIndex(index)