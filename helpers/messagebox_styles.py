"""
Sistema de estilos automáticos para QMessageBox.
Aplica colores diferenciados según el tipo de mensaje sin necesidad de modificar cada controller.
"""

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QEvent, QObject


class MessageBoxStyler(QObject):
    """
    Event filter que intercepta y aplica estilos a todos los QMessageBox automáticamente.
    """

    ESTILOS = {
        QMessageBox.Warning: {
            "bg": "#4d1f1f",  # Rojo oscuro
            "text": "#ffdddd",
            "btn_bg": "#8b0000",
            "btn_border": "#aa0000",
            "btn_hover": "#a00000",
            "btn_pressed": "#660000"
        },
        QMessageBox.Critical: {
            "bg": "#5d0f0f",  # Rojo más intenso
            "text": "#ffcccc",
            "btn_bg": "#990000",
            "btn_border": "#bb0000",
            "btn_hover": "#b00000",
            "btn_pressed": "#770000"
        },
        QMessageBox.Information: {
            "bg": "#1f2d4d",  # Azul oscuro
            "text": "#ddeeff",
            "btn_bg": "#0d6efd",
            "btn_border": "#0a58ca",
            "btn_hover": "#0b5ed7",
            "btn_pressed": "#0a4fb8"
        },
        QMessageBox.Question: {
            "bg": "#4d3d1f",  # Amarillo/naranja oscuro
            "text": "#ffeecc",
            "btn_bg": "#cc8800",
            "btn_border": "#dd9900",
            "btn_hover": "#dd9900",
            "btn_pressed": "#aa7700"
        }
    }

    def eventFilter(self, obj, event):
        """Intercepta eventos de QMessageBox para aplicar estilos."""
        if isinstance(obj, QMessageBox) and event.type() == QEvent.Show:
            self.aplicar_estilo(obj)
        return super().eventFilter(obj, event)

    def aplicar_estilo(self, msg_box):
        """Aplica el estilo correspondiente según el icono del QMessageBox."""
        icon = msg_box.icon()
        estilo = self.ESTILOS.get(icon, self.ESTILOS[QMessageBox.Warning])

        msg_box.setStyleSheet(f"""
            QMessageBox {{
                background-color: {estilo['bg']};
            }}
            QLabel {{
                color: {estilo['text']};
                background-color: {estilo['bg']};
                padding: 10px;
            }}
            QPushButton {{
                background-color: {estilo['btn_bg']};
                border: 1px solid {estilo['btn_border']};
                color: white;
                min-width: 70px;
                padding: 6px 12px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: {estilo['btn_hover']};
            }}
            QPushButton:pressed {{
                background-color: {estilo['btn_pressed']};
            }}
        """)


def aplicar_estilo_messagebox(msg_box, tipo="warning"):
    """
    Función de compatibilidad para aplicar estilos manualmente (legacy).
    Se mantiene para no romper código existente.

    Args:
        msg_box: Instancia de QMessageBox
        tipo: "warning", "critical", "information", "question" (string)
    """
    tipo_map = {
        "warning": QMessageBox.Warning,
        "critical": QMessageBox.Critical,
        "information": QMessageBox.Information,
        "question": QMessageBox.Question
    }

    icon = tipo_map.get(tipo, QMessageBox.Warning)
    estilo = MessageBoxStyler.ESTILOS.get(icon, MessageBoxStyler.ESTILOS[QMessageBox.Warning])

    msg_box.setStyleSheet(f"""
        QMessageBox {{
            background-color: {estilo['bg']};
        }}
        QLabel {{
            color: {estilo['text']};
            background-color: {estilo['bg']};
            padding: 10px;
        }}
        QPushButton {{
            background-color: {estilo['btn_bg']};
            border: 1px solid {estilo['btn_border']};
            color: white;
            min-width: 70px;
            padding: 6px 12px;
            border-radius: 4px;
        }}
        QPushButton:hover {{
            background-color: {estilo['btn_hover']};
        }}
        QPushButton:pressed {{
            background-color: {estilo['btn_pressed']};
        }}
    """)

