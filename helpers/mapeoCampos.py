from PySide6.QtWidgets import (QLineEdit, QTextEdit, QCheckBox, QComboBox,
                               QSpinBox, QDoubleSpinBox, QWidget, QDateEdit)
from PySide6.QtCore import QDate, QDateTime


class MapeoCampos:
    @staticmethod
    def mapear_datos_a_vista(vista, columnas, fila):
        """Rellena la vista usando los datos de la fila de la BD."""
        if not fila: return

        datos = dict(zip(columnas, fila))
        for nombre_col, valor in datos.items():
            # Intentamos buscar el widget directamente o en .ui
            widget = getattr(vista, nombre_col, None)
            if not widget and hasattr(vista, 'ui'):
                widget = getattr(vista.ui, nombre_col, None)

            if widget:
                MapeoCampos.set_widget_value(widget, valor)

    @staticmethod
    def set_widget_value(widget, valor):
        """Establece el valor en el widget según su tipo, con formato visual de fecha."""
        # 1. Gestión de Nulos
        if valor is None:
            if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                widget.setValue(0)
            elif hasattr(widget, 'setDate'):
                widget.setDate(QDate.currentDate())
            else:
                if hasattr(widget, 'clear'): widget.clear()
            return

        # 2. Identificación de Fechas
        es_fecha_qt = isinstance(valor, (QDate, QDateTime))

        # 3. Asignación por tipo de Widget
        if isinstance(widget, QLineEdit):
            if es_fecha_qt:
                # FORMATO VISUAL: El usuario ve dd/MM/yyyy
                widget.setText(valor.toString("dd/MM/yyyy"))
            else:
                # Si no es fecha, string normal
                widget.setText(str(valor))

        elif isinstance(widget, QTextEdit):
            widget.setPlainText(str(valor))

        elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
            try:
                widget.setValue(float(valor))
            except (ValueError, TypeError):
                widget.setValue(0)

        elif isinstance(widget, QCheckBox):
            widget.setChecked(bool(valor))

        elif isinstance(widget, QComboBox):
            # Busca primero por ID (Data) y luego por Texto
            index = widget.findData(valor)
            if index < 0:
                index = widget.findText(str(valor))
            widget.setCurrentIndex(index if index >= 0 else 0)

        elif hasattr(widget, 'setDate'):  # Para QDateEdit o similares
            if es_fecha_qt:
                widget.setDate(valor)
            elif isinstance(valor, str) and valor:
                # Intentamos parsear tanto formato ISO como Español por seguridad
                fecha_temp = QDate.fromString(valor, "yyyy-MM-dd")
                if not fecha_temp.isValid():
                    fecha_temp = QDate.fromString(valor, "dd/MM/yyyy")

                if fecha_temp.isValid():
                    widget.setDate(fecha_temp)

    @staticmethod
    def capturar_datos_vista(vista, columnas_db):
        """Extrae los datos de la vista para enviarlos a la BD."""
        payload = {}
        for col in columnas_db:
            # Intentamos buscar el widget directamente o en .ui
            widget = getattr(vista, col, None)
            if not widget and hasattr(vista, 'ui'):
                widget = getattr(vista.ui, col, None)

            if not widget: continue

            if isinstance(widget, QLineEdit):
                texto = widget.text().strip()

                # 1. Limpieza radical de la máscara vacía
                # Eliminamos barras y espacios para ver si queda algo real
                solo_numeros = texto.replace("/", "").replace("_", "").strip()

                if not solo_numeros:
                    # Si no hay números, el campo está vacío para la BD
                    payload[col] = None
                    continue

                # 2. Si hay algo, procedemos con la conversión a ISO
                if "/" in texto:
                    fecha_qt = QDate.fromString(texto, "dd/MM/yyyy")
                    if fecha_qt.isValid():
                        payload[col] = fecha_qt.toString("yyyy-MM-dd")
                    else:
                        # Si el usuario dejó la fecha a medias (ej: 12/  /    )
                        payload[col] = None
                else:
                    payload[col] = texto if texto else None

            elif isinstance(widget, QTextEdit):
                payload[col] = widget.toPlainText().strip()

            elif isinstance(widget, QCheckBox):
                payload[col] = 1 if widget.isChecked() else 0

            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                payload[col] = widget.value()

            elif isinstance(widget, QComboBox):
                valor_data = widget.currentData()
                # Si el valor es el del placeholder (índice 0), forzamos el ID 1
                # para evitar el error de NOT NULL en campos como id_divisa
                if valor_data is None or widget.currentIndex() == 0:
                    payload[col] = 1
                else:
                    payload[col] = valor_data

            elif hasattr(widget, 'date'):
                # Para QDateEdit, convertimos a string ISO directamente
                payload[col] = widget.date().toString("yyyy-MM-dd")

        return payload

    @staticmethod
    def validar_campos(vista):
        """Valida campos obligatorios basándose en objectName."""
        faltantes = []
        tipos_interesantes = (QLineEdit, QTextEdit, QComboBox, QSpinBox)
        todos_los_widgets = vista.findChildren(QWidget)

        for widget in todos_los_widgets:
            if isinstance(widget, tipos_interesantes):
                nombre = widget.objectName()
                # Lógica: si el nombre empieza por 'txt_' y está vacío
                if hasattr(widget, 'text') and not widget.text().strip():
                    if nombre.startswith("txt_"):
                        faltantes.append(nombre)
        return len(faltantes) == 0, faltantes


    """----------------------------------------------------------------------------
    Limpia los campos del formulario basándose en columnas DB para un nuevo cliente
    ----------------------------------------------------------------------------"""
    @staticmethod
    def limpiar_formulario(vista, columnas_db):
        """Pone todos los widgets vinculados a las columnas en blanco o a 0."""
        for col in columnas_db:
            # Buscamos el widget igual que en la captura
            widget = getattr(vista, col, None)
            if not widget and hasattr(vista, 'ui'):
                widget = getattr(vista.ui, col, None)

            if not widget: continue

            # Reset por tipo de widget
            if isinstance(widget, (QLineEdit, QTextEdit)):
                widget.clear()
                # Si tiene máscara (como la fecha), al hacer clear() se queda el "  /  /  "
                # pero el cursor vuelve al inicio.

            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                widget.setValue(0)

            elif isinstance(widget, QCheckBox):
                widget.setChecked(False)

            elif isinstance(widget, QComboBox):
                # Volver al "--- Seleccione ---" (índice 0)
                widget.setCurrentIndex(0)

            elif hasattr(widget, 'setDate'):
                # Para QDateEdit, ponemos la fecha de hoy
                widget.setDate(QDate.currentDate())