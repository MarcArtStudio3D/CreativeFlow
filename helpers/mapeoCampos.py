from PySide6.QtWidgets import (QLineEdit, QTextEdit, QCheckBox, QComboBox,
                               QSpinBox, QDoubleSpinBox, QWidget)


class MapeoCampos:
    @staticmethod
    def mapear_datos_a_vista(vista, columnas, fila):
        """Rellena la vista usando los datos de la fila de la BD."""
        if not fila: return

        datos = dict(zip(columnas, fila))
        for nombre_col, valor in datos.items():
            widget = getattr(vista, nombre_col, None)
            if widget:
                MapeoCampos.set_widget_value(widget, valor)

    @staticmethod
    def set_widget_value(widget, valor):
        if valor is None:
            valor = 0 if isinstance(widget, (QSpinBox, QDoubleSpinBox)) else ""

        if isinstance(widget, QLineEdit):
            widget.setText(str(valor))
        elif isinstance(widget, QTextEdit):
            widget.setPlainText(str(valor))
        elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
            widget.setValue(float(valor))
        elif isinstance(widget, QCheckBox):
            widget.setChecked(bool(valor))
        elif isinstance(widget, QComboBox):
            index = widget.findText(str(valor))
            if index >= 0: widget.setCurrentIndex(index)
        elif hasattr(widget, 'setDate') and valor:
            widget.setDate(valor)

    @staticmethod
    def capturar_datos_vista(vista, columnas_db):
        """Extrae los datos de la vista para enviarlos a la BD."""
        payload = {}
        for col in columnas_db:
            widget = getattr(vista, col, None)
            if not widget: continue

            if isinstance(widget, QLineEdit):
                payload[col] = widget.text()
            elif isinstance(widget, QTextEdit):
                payload[col] = widget.toPlainText()
            elif isinstance(widget, QCheckBox):
                payload[col] = 1 if widget.isChecked() else 0
            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                payload[col] = widget.value()
            elif isinstance(widget, QComboBox):
                payload[col] = widget.currentText()
            elif hasattr(widget, 'date'):
                payload[col] = widget.date().toPython()
        return payload

    @staticmethod
    def validar_campos(vista):
        faltantes = []
        tipos_interesantes = (QLineEdit, QTextEdit, QComboBox, QSpinBox)

        # Buscamos todos los hijos que sean QWidget
        todos_los_widgets = vista.findChildren(QWidget)

        for widget in todos_los_widgets:
            # Comprobamos si el widget es de uno de los tipos que queremos validar
            if isinstance(widget, tipos_interesantes):
                # Aquí va tu lógica de validación (ejemplo: si está vacío y es obligatorio)
                nombre = widget.objectName()
                # Si el nombre empieza por 'txt_' o 'cmb_' y está vacío...
                if hasattr(widget, 'text') and not widget.text().strip():
                    if nombre.startswith("txt_"):  # O la lógica que uses para obligatorios
                        faltantes.append(nombre)

        return len(faltantes) == 0, faltantes