import os
import sys
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QFrame, QLabel,
                               QLineEdit, QComboBox, QPushButton, QApplication)
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QFont, QColor
from colores import *


class LoginView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("CREATIVE FLOW - Login")
        self.setFixedSize(500, 650)
        self.setStyleSheet(f"background-color: {COLOR_NEGRO};")

        # Layout principal para centrar el frame
        self.main_layout = QVBoxLayout(self)

        # EL CONTENEDOR CENTRAL (QFrame)
        self.login_card = QFrame()
        self.login_card.setFixedSize(400, 550)
        # Aplicamos el estilo tipo "Card"
        self.login_card.setStyleSheet(f"""
            QFrame {{
                background-color: {COLOR_FONDO_CONTENEDORES};
                border: 1px solid {COLOR_LINEAS};
                border-radius: 10px;
            }}
            QLabel {{ border: none; background: transparent; }}
        """)

        # Centramos el frame en la ventana
        self.main_layout.addWidget(self.login_card, alignment=Qt.AlignCenter)

        # Layout interno del Frame
        self.card_layout = QVBoxLayout(self.login_card)
        self.card_layout.setContentsMargins(30, 40, 30, 40)
        self.card_layout.setSpacing(10)

        # TÍTULOS
        self.lbl_titulo = QLabel("CREATIVE FLOW")
        self.lbl_titulo.setStyleSheet(f"color: {COLOR_NARANJA}; font-size: 24px; font-weight: bold; border: none;")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.card_layout.addWidget(self.lbl_titulo)

        self.lbl_sub = QLabel("PROJECTS PIPELINE SYSTEM")
        self.lbl_sub.setStyleSheet(f"color: {COLOR_GRIS_TECNICO}; font-size: 10px; font-weight: bold; border: none;")
        self.lbl_sub.setAlignment(Qt.AlignCenter)
        self.card_layout.addWidget(self.lbl_sub)
        self.card_layout.addSpacing(20)

        # COMBOBOX EMPRESA
        self.combo_empresa = QComboBox()
        self.combo_empresa.addItems(["ARTSTUDIO3D", "OTRA_EMPRESA"])
        self.combo_empresa.setFixedHeight(40)
        self.card_layout.addWidget(self.combo_empresa)
        ruta_chevron = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "images", "chevron-down.svg"))
        self.combo_empresa.setStyleSheet(f"""
            QComboBox {{
                background-color: #333333;
                color: white;
                border: 1px solid #444444;
                border-radius: 8px;
                padding: 5px 15px;
                min-height: 35px;
                font-size: 12px;
            }}

            QComboBox:hover {{
                border: 1px solid {COLOR_NARANJA};
            }}

            /* Contenedor del botón de desplegar */
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 35px;
                border-left: none;
            }}

            /* Uso de tu archivo SVG */
            QComboBox::down-arrow {{
                image: url({ruta_chevron});
                width: 14px;  /* Ajusta el tamaño a tu gusto */
                height: 14px;
                padding-right: 10px; /* Margen derecho para que no pegue al borde */
            }}

            /* Estilo del menú desplegable (la lista) */
            QComboBox QAbstractItemView {{
                background-color: #222222;
                color: #CCCCCC;
                selection-background-color: {COLOR_NARANJA};
                selection-color: black;
                border: 1px solid #444444;
                border-radius: 8px;
                outline: none;
                padding: 5px;
            }}
        """)

        # INPUTS (Usuario y Password)
        self.card_layout.addWidget(self.crear_label_campo("USUARIO"))
        self.ent_user = self.crear_input_campo()
        self.card_layout.addWidget(self.ent_user)

        self.card_layout.addWidget(self.crear_label_campo("CONTRASEÑA"))
        self.ent_pass = self.crear_input_campo()
        self.ent_pass.setEchoMode(QLineEdit.Password)
        self.card_layout.addWidget(self.ent_pass)

        self.card_layout.addSpacing(20)

        # BOTONES
        self.btn_conectar = self.crear_boton_naranja("CONECTAR AL PIPELINE", COLOR_NARANJA)
        self.btn_conectar.clicked.connect(self.controller.handle_login)
        # En Qt, el botón con foco acepta 'Enter' automáticamente si es default
        self.btn_conectar.setDefault(True)
        self.card_layout.addWidget(self.btn_conectar)

        self.btn_salir = self.crear_boton_naranja("SALIR", "#E67E22")
        self.btn_salir.clicked.connect(self.close)
        self.card_layout.addWidget(self.btn_salir)

        # BOTÓN ADMIN (Oculto inicialmente)
        self.btn_admin = self.crear_boton_naranja("ADMIN", COLOR_ROJO_ERROR)
        self.btn_admin.clicked.connect(self.controller.handle_admin)
        self.btn_admin.hide()
        self.card_layout.addWidget(self.btn_admin)

    # --- MÉTODOS AUXILIARES DE ESTILO ---
    def crear_label_campo(self, texto):
        lbl = QLabel(texto)
        lbl.setStyleSheet(f"color: {COLOR_BLANCO}; font-size: 10px; font-weight: bold;")
        return lbl

    def crear_input_campo(self):
        ent = QLineEdit()
        ent.setFixedHeight(40)
        ent.setStyleSheet(f"""
            QLineEdit {{
                background-color: {COLOR_FILA_CEBRA};
                border: 1px solid {COLOR_BORDE_NORMAL};
                color: white;
                padding-left: 10px;
                border-radius: 5px;
            }}
            QLineEdit:focus {{ border: 1px solid {COLOR_NARANJA}; }}
        """)
        return ent

    def crear_boton_naranja(self, texto, color):
        btn = QPushButton(texto)
        btn.setFixedHeight(45)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-weight: bold;
                border-radius: 5px;
            }}
            QPushButton:hover {{ background-color: {COLOR_BOTONES_HOVER}; }}
            QPushButton:focus {{ border: 2px solid white; }}
        """)
        return btn

    def get_credentials(self):
        return {
            "empresa": self.combo_empresa.currentText(),
            "usuario": self.ent_user.text(),
            "pass": self.ent_pass.text()
        }

    def agregar_boton_admin(self):
        self.btn_admin.show()
        # Qt ajusta el layout automáticamente al mostrarlo