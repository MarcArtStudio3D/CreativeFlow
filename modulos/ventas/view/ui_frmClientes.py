# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmClientes.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableView, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
from modulos import designer_rc

class Ui_frmClientes(object):
    def setupUi(self, frmClientes):
        if not frmClientes.objectName():
            frmClientes.setObjectName(u"frmClientes")
        frmClientes.setWindowModality(Qt.WindowModality.WindowModal)
        frmClientes.resize(1073, 732)
        frmClientes.setBaseSize(QSize(1024, 500))
        frmClientes.setModal(True)
        self.gridLayout_3 = QGridLayout(frmClientes)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textoTitulo = QLabel(frmClientes)
        self.textoTitulo.setObjectName(u"textoTitulo")
        self.textoTitulo.setMinimumSize(QSize(464, 27))
        self.textoTitulo.setMaximumSize(QSize(16777215, 40))
        self.textoTitulo.setStyleSheet(u"background: #304163;\n"
"color: rgb(255,255,255);\n"
"font: 14pt \"Sans Serif\";")
        self.textoTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.textoTitulo, 0, 0, 1, 5)

        self.stackedWidget = QStackedWidget(frmClientes)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.paginaedicion = QWidget()
        self.paginaedicion.setObjectName(u"paginaedicion")
        self.gridLayout_27 = QGridLayout(self.paginaedicion)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(-1, -1, 20, -1)
        self.label_40 = QLabel(self.paginaedicion)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_27.addWidget(self.label_40, 0, 0, 1, 1)

        self.lbl_nombre_fiscal = QLabel(self.paginaedicion)
        self.lbl_nombre_fiscal.setObjectName(u"lbl_nombre_fiscal")

        self.gridLayout_27.addWidget(self.lbl_nombre_fiscal, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.paginaedicion)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(135, 374))
        self.frame_8.setMaximumSize(QSize(110, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.btnEditar = QPushButton(self.frame_8)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setMinimumSize(QSize(0, 45))
        icon = QIcon()
        icon.addFile(u":/PNG/resources/icons/png/Edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditar.setIcon(icon)
        self.btnEditar.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnEditar, 4, 0, 1, 1)

        self.btnBuscar = QPushButton(self.frame_8)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setMinimumSize(QSize(0, 45))
        icon1 = QIcon()
        icon1.addFile(u":/PNG/resources/icons/png/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBuscar.setIcon(icon1)
        self.btnBuscar.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnBuscar, 3, 0, 1, 1)

        self.btnAnadir = QPushButton(self.frame_8)
        self.btnAnadir.setObjectName(u"btnAnadir")
        self.btnAnadir.setMinimumSize(QSize(0, 45))
        icon2 = QIcon()
        icon2.addFile(u":/PNG/resources/icons/png/Add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAnadir.setIcon(icon2)
        self.btnAnadir.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnAnadir, 0, 0, 1, 1)

        self.btnSiguiente = QPushButton(self.frame_8)
        self.btnSiguiente.setObjectName(u"btnSiguiente")
        self.btnSiguiente.setMinimumSize(QSize(0, 45))
        icon3 = QIcon()
        icon3.addFile(u":/PNG/resources/icons/png/Next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSiguiente.setIcon(icon3)
        self.btnSiguiente.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnSiguiente, 1, 0, 1, 1)

        self.btnDeshacer = QPushButton(self.frame_8)
        self.btnDeshacer.setObjectName(u"btnDeshacer")
        self.btnDeshacer.setEnabled(False)
        self.btnDeshacer.setMinimumSize(QSize(0, 45))
        icon4 = QIcon()
        icon4.addFile(u":/PNG/resources/icons/png/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDeshacer.setIcon(icon4)
        self.btnDeshacer.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnDeshacer, 6, 0, 1, 1)

        self.btnGuardar = QPushButton(self.frame_8)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setEnabled(False)
        self.btnGuardar.setMinimumSize(QSize(0, 45))
        icon5 = QIcon()
        icon5.addFile(u":/PNG/resources/icons/png/Save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardar.setIcon(icon5)
        self.btnGuardar.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnGuardar, 5, 0, 1, 1)

        self.btnBorrar = QPushButton(self.frame_8)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setMinimumSize(QSize(0, 45))
        icon6 = QIcon()
        icon6.addFile(u":/PNG/resources/icons/png/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBorrar.setIcon(icon6)
        self.btnBorrar.setIconSize(QSize(18, 18))

        self.gridLayout_7.addWidget(self.btnBorrar, 8, 0, 1, 1)

        self.btnAnterior = QPushButton(self.frame_8)
        self.btnAnterior.setObjectName(u"btnAnterior")
        self.btnAnterior.setMinimumSize(QSize(0, 45))
        icon7 = QIcon()
        icon7.addFile(u":/PNG/resources/icons/png/Previous.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAnterior.setIcon(icon7)
        self.btnAnterior.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btnAnterior, 2, 0, 1, 1)

        self.btnCerrar = QPushButton(self.frame_8)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setMinimumSize(QSize(0, 45))
        icon8 = QIcon()
        icon8.addFile(u":/PNG/resources/icons/png/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCerrar.setIcon(icon8)

        self.gridLayout_7.addWidget(self.btnCerrar, 9, 0, 1, 1)


        self.gridLayout_27.addWidget(self.frame_8, 1, 0, 1, 1)

        self.tabwidget = QTabWidget(self.paginaedicion)
        self.tabwidget.setObjectName(u"tabwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabwidget.sizePolicy().hasHeightForWidth())
        self.tabwidget.setSizePolicy(sizePolicy1)
        self.tabwidget.setAutoFillBackground(False)
        self.tab_datos = QWidget()
        self.tab_datos.setObjectName(u"tab_datos")
        self.tab_datos.setStyleSheet(u"")
        self.gridLayout_25 = QGridLayout(self.tab_datos)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.blink_stack = QStackedWidget(self.tab_datos)
        self.blink_stack.setObjectName(u"blink_stack")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.blink_stack.sizePolicy().hasHeightForWidth())
        self.blink_stack.setSizePolicy(sizePolicy2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnVer_OtrosContactos = QPushButton(self.page)
        self.btnVer_OtrosContactos.setObjectName(u"btnVer_OtrosContactos")
        self.btnVer_OtrosContactos.setEnabled(False)
        self.btnVer_OtrosContactos.setMinimumSize(QSize(145, 0))
        self.btnVer_OtrosContactos.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/PNG/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnVer_OtrosContactos.setIcon(icon9)
        self.btnVer_OtrosContactos.setIconSize(QSize(15, 15))

        self.gridLayout_2.addWidget(self.btnVer_OtrosContactos, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_46 = QLabel(self.frame_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 20))
        self.label_46.setStyleSheet(u"")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_46, 0, 0, 1, 1)

        self.btnEdita_tipoCliente = QPushButton(self.frame_2)
        self.btnEdita_tipoCliente.setObjectName(u"btnEdita_tipoCliente")

        self.gridLayout_5.addWidget(self.btnEdita_tipoCliente, 3, 0, 1, 1)

        self.lista_tipos = QTreeWidget(self.frame_2)
        self.lista_tipos.setObjectName(u"lista_tipos")
        self.lista_tipos.setFrameShape(QFrame.Shape.StyledPanel)
        self.lista_tipos.setProperty(u"showDropIndicator", True)
        self.lista_tipos.setRootIsDecorated(True)
        self.lista_tipos.header().setVisible(False)

        self.gridLayout_5.addWidget(self.lista_tipos, 1, 0, 2, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.blink_stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_17 = QGridLayout(self.page_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.blink_stack.addWidget(self.page_2)

        self.gridLayout_25.addWidget(self.blink_stack, 0, 1, 2, 1)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.btnValidarVIES = QPushButton(self.tab_datos)
        self.btnValidarVIES.setObjectName(u"btnValidarVIES")

        self.gridLayout_30.addWidget(self.btnValidarVIES, 0, 7, 1, 1)

        self.cif_nif_siret = QLineEdit(self.tab_datos)
        self.cif_nif_siret.setObjectName(u"cif_nif_siret")
        self.cif_nif_siret.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.cif_nif_siret, 1, 1, 1, 3)

        self.siret = QLineEdit(self.tab_datos)
        self.siret.setObjectName(u"siret")

        self.gridLayout_30.addWidget(self.siret, 1, 5, 1, 2)

        self.label_12 = QLabel(self.tab_datos)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_12, 9, 0, 1, 1)

        self.apellido1 = QLineEdit(self.tab_datos)
        self.apellido1.setObjectName(u"apellido1")
        self.apellido1.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.apellido1, 4, 1, 1, 7)

        self.lblSegundoApellido = QLabel(self.tab_datos)
        self.lblSegundoApellido.setObjectName(u"lblSegundoApellido")
        self.lblSegundoApellido.setMinimumSize(QSize(0, 0))
        self.lblSegundoApellido.setMaximumSize(QSize(16777214, 16777215))

        self.gridLayout_30.addWidget(self.lblSegundoApellido, 5, 0, 1, 1)

        self.telefono2 = QLineEdit(self.tab_datos)
        self.telefono2.setObjectName(u"telefono2")
        self.telefono2.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.telefono2, 17, 5, 1, 1)

        self.label_25 = QLabel(self.tab_datos)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_25, 22, 4, 1, 1)

        self.nombre_comercial = QLineEdit(self.tab_datos)
        self.nombre_comercial.setObjectName(u"nombre_comercial")
        self.nombre_comercial.setMaximumSize(QSize(774, 16777215))
        self.nombre_comercial.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.nombre_comercial, 9, 1, 1, 7)

        self.label_3 = QLabel(self.tab_datos)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_30.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_18 = QLabel(self.tab_datos)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_30.addWidget(self.label_18, 10, 0, 1, 1)

        self.label_20 = QLabel(self.tab_datos)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_20, 17, 4, 1, 1)

        self.direccion1 = QLineEdit(self.tab_datos)
        self.direccion1.setObjectName(u"direccion1")
        self.direccion1.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.direccion1, 11, 1, 1, 7)

        self.apellido2 = QLineEdit(self.tab_datos)
        self.apellido2.setObjectName(u"apellido2")
        self.apellido2.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.apellido2, 5, 1, 1, 7)

        self.cif_vies = QLineEdit(self.tab_datos)
        self.cif_vies.setObjectName(u"cif_vies")
        self.cif_vies.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.cif_vies, 0, 5, 1, 2)

        self.label_4 = QLabel(self.tab_datos)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_30.addWidget(self.label_4, 4, 0, 1, 1)

        self.cp = QLineEdit(self.tab_datos)
        self.cp.setObjectName(u"cp")
        self.cp.setMaximumSize(QSize(100, 16777215))
        self.cp.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.cp, 13, 1, 1, 1)

        self.telefono1 = QLineEdit(self.tab_datos)
        self.telefono1.setObjectName(u"telefono1")
        self.telefono1.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.telefono1, 17, 1, 1, 3)

        self.lblCIF_IVA_UE = QLabel(self.tab_datos)
        self.lblCIF_IVA_UE.setObjectName(u"lblCIF_IVA_UE")

        self.gridLayout_30.addWidget(self.lblCIF_IVA_UE, 0, 4, 1, 1)

        self.provincia = QLineEdit(self.tab_datos)
        self.provincia.setObjectName(u"provincia")
        self.provincia.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.provincia, 16, 1, 1, 3)

        self.LblSIRET = QLabel(self.tab_datos)
        self.LblSIRET.setObjectName(u"LblSIRET")

        self.gridLayout_30.addWidget(self.LblSIRET, 1, 4, 1, 1)

        self.pais = QLineEdit(self.tab_datos)
        self.pais.setObjectName(u"pais")

        self.gridLayout_30.addWidget(self.pais, 10, 1, 1, 2)

        self.label_2 = QLabel(self.tab_datos)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_30.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_13 = QLabel(self.tab_datos)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_13, 11, 0, 1, 1)

        self.label_23 = QLabel(self.tab_datos)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_23, 22, 0, 1, 1)

        self.movil = QLineEdit(self.tab_datos)
        self.movil.setObjectName(u"movil")
        self.movil.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.movil, 17, 7, 1, 1)

        self.web = QLineEdit(self.tab_datos)
        self.web.setObjectName(u"web")
        self.web.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.web, 22, 1, 1, 3)

        self.label_11 = QLabel(self.tab_datos)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_11, 8, 0, 1, 1)

        self.label_22 = QLabel(self.tab_datos)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_22, 17, 6, 1, 1)

        self.label_15 = QLabel(self.tab_datos)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_15, 13, 0, 1, 1)

        self.poblacion = QLineEdit(self.tab_datos)
        self.poblacion.setObjectName(u"poblacion")
        self.poblacion.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.poblacion, 13, 3, 1, 5)

        self.label = QLabel(self.tab_datos)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(49, 16777215))
        self.label.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.label, 0, 0, 1, 1)

        self.nombre = QLineEdit(self.tab_datos)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setStyleSheet(u"")
        self.nombre.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridLayout_30.addWidget(self.nombre, 3, 1, 1, 7)

        self.label_16 = QLabel(self.tab_datos)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_30.addWidget(self.label_16, 13, 2, 1, 1)

        self.codigo_cliente = QLineEdit(self.tab_datos)
        self.codigo_cliente.setObjectName(u"codigo_cliente")
        self.codigo_cliente.setStyleSheet(u"")
        self.codigo_cliente.setReadOnly(False)

        self.gridLayout_30.addWidget(self.codigo_cliente, 0, 1, 1, 3)

        self.nombre_fiscal = QLineEdit(self.tab_datos)
        self.nombre_fiscal.setObjectName(u"nombre_fiscal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nombre_fiscal.sizePolicy().hasHeightForWidth())
        self.nombre_fiscal.setSizePolicy(sizePolicy3)
        self.nombre_fiscal.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.nombre_fiscal, 8, 1, 1, 7)

        self.label_24 = QLabel(self.tab_datos)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_30.addWidget(self.label_24, 21, 0, 1, 1)

        self.lblProvincia = QLabel(self.tab_datos)
        self.lblProvincia.setObjectName(u"lblProvincia")
        sizePolicy2.setHeightForWidth(self.lblProvincia.sizePolicy().hasHeightForWidth())
        self.lblProvincia.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.lblProvincia, 16, 0, 1, 1)

        self.label_19 = QLabel(self.tab_datos)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_30.addWidget(self.label_19, 17, 0, 1, 1)

        self.label_14 = QLabel(self.tab_datos)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.gridLayout_30.addWidget(self.label_14, 12, 0, 1, 1)

        self.direccion2 = QLineEdit(self.tab_datos)
        self.direccion2.setObjectName(u"direccion2")
        self.direccion2.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.direccion2, 12, 1, 1, 7)

        self.email = QLineEdit(self.tab_datos)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.email, 21, 1, 1, 7)

        self.observaciones = QLineEdit(self.tab_datos)
        self.observaciones.setObjectName(u"observaciones")
        self.observaciones.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.observaciones, 22, 5, 1, 3)


        self.gridLayout_25.addLayout(self.gridLayout_30, 0, 0, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.tabwidget.addTab(self.tab_datos, "")
        self.tab_direcciones = QWidget()
        self.tab_direcciones.setObjectName(u"tab_direcciones")
        self.tab_direcciones.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.tab_direcciones)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.tab_direcciones)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 27))
        self.label_7.setStyleSheet(u"background: #304163;\n"
"color: rgb(255,255,255);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_6 = QLabel(self.tab_direcciones)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.descripcion_direccion = QLineEdit(self.tab_direcciones)
        self.descripcion_direccion.setObjectName(u"descripcion_direccion")

        self.gridLayout.addWidget(self.descripcion_direccion, 0, 2, 1, 1)

        self.lista_direccionesAlternativas = QListView(self.tab_direcciones)
        self.lista_direccionesAlternativas.setObjectName(u"lista_direccionesAlternativas")
        self.lista_direccionesAlternativas.setMaximumSize(QSize(200, 16777215))
        self.lista_direccionesAlternativas.setAlternatingRowColors(True)
        self.lista_direccionesAlternativas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.lista_direccionesAlternativas.setViewMode(QListView.ViewMode.ListMode)
        self.lista_direccionesAlternativas.setModelColumn(0)

        self.gridLayout.addWidget(self.lista_direccionesAlternativas, 1, 0, 8, 1)

        self.label_29 = QLabel(self.tab_direcciones)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 1, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.poblacion_alternativa = QLineEdit(self.tab_direcciones)
        self.poblacion_alternativa.setObjectName(u"poblacion_alternativa")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.poblacion_alternativa.sizePolicy().hasHeightForWidth())
        self.poblacion_alternativa.setSizePolicy(sizePolicy4)

        self.horizontalLayout_13.addWidget(self.poblacion_alternativa)

        self.label_66 = QLabel(self.tab_direcciones)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_13.addWidget(self.label_66)

        self.txtpoblacionAlternativa = QLineEdit(self.tab_direcciones)
        self.txtpoblacionAlternativa.setObjectName(u"txtpoblacionAlternativa")

        self.horizontalLayout_13.addWidget(self.txtpoblacionAlternativa)


        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 2, 1, 1)

        self.label_27 = QLabel(self.tab_direcciones)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 2, 1, 1, 1)

        self.txtdireccion1Alternativa1 = QLineEdit(self.tab_direcciones)
        self.txtdireccion1Alternativa1.setObjectName(u"txtdireccion1Alternativa1")

        self.gridLayout.addWidget(self.txtdireccion1Alternativa1, 2, 2, 1, 1)

        self.label_28 = QLabel(self.tab_direcciones)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 3, 1, 1, 1)

        self.txtdireccion1Alternativa2 = QLineEdit(self.tab_direcciones)
        self.txtdireccion1Alternativa2.setObjectName(u"txtdireccion1Alternativa2")

        self.gridLayout.addWidget(self.txtdireccion1Alternativa2, 3, 2, 1, 1)

        self.lblProvinciaAlternativa = QLabel(self.tab_direcciones)
        self.lblProvinciaAlternativa.setObjectName(u"lblProvinciaAlternativa")

        self.gridLayout.addWidget(self.lblProvinciaAlternativa, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtprovinciaAlternativa = QLineEdit(self.tab_direcciones)
        self.txtprovinciaAlternativa.setObjectName(u"txtprovinciaAlternativa")

        self.horizontalLayout.addWidget(self.txtprovinciaAlternativa)

        self.label_31 = QLabel(self.tab_direcciones)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout.addWidget(self.label_31)

        self.cbopaisAlternativa = QComboBox(self.tab_direcciones)
        self.cbopaisAlternativa.setObjectName(u"cbopaisAlternativa")
        self.cbopaisAlternativa.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.cbopaisAlternativa)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)

        self.label_64 = QLabel(self.tab_direcciones)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout.addWidget(self.label_64, 5, 1, 1, 1)

        self.txtemail_alternativa = QLineEdit(self.tab_direcciones)
        self.txtemail_alternativa.setObjectName(u"txtemail_alternativa")

        self.gridLayout.addWidget(self.txtemail_alternativa, 5, 2, 1, 1)

        self.label_86 = QLabel(self.tab_direcciones)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout.addWidget(self.label_86, 6, 1, 1, 1)

        self.txtcomentarios_alternativa = QTextEdit(self.tab_direcciones)
        self.txtcomentarios_alternativa.setObjectName(u"txtcomentarios_alternativa")

        self.gridLayout.addWidget(self.txtcomentarios_alternativa, 6, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAnadirdireccion = QPushButton(self.tab_direcciones)
        self.btnAnadirdireccion.setObjectName(u"btnAnadirdireccion")
        self.btnAnadirdireccion.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u":/PNG/Add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAnadirdireccion.setIcon(icon10)
        self.btnAnadirdireccion.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.btnAnadirdireccion)

        self.btnEditardireccionAlternativa = QPushButton(self.tab_direcciones)
        self.btnEditardireccionAlternativa.setObjectName(u"btnEditardireccionAlternativa")
        self.btnEditardireccionAlternativa.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(u":/PNG/Edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditardireccionAlternativa.setIcon(icon11)

        self.horizontalLayout_2.addWidget(self.btnEditardireccionAlternativa)

        self.btnBorrardireccion = QPushButton(self.tab_direcciones)
        self.btnBorrardireccion.setObjectName(u"btnBorrardireccion")
        self.btnBorrardireccion.setEnabled(False)
        icon12 = QIcon()
        icon12.addFile(u":/PNG/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBorrardireccion.setIcon(icon12)
        self.btnBorrardireccion.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.btnBorrardireccion)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnGuardardireccionAlternativa = QPushButton(self.tab_direcciones)
        self.btnGuardardireccionAlternativa.setObjectName(u"btnGuardardireccionAlternativa")
        self.btnGuardardireccionAlternativa.setEnabled(False)
        icon13 = QIcon()
        icon13.addFile(u":/PNG/Save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGuardardireccionAlternativa.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.btnGuardardireccionAlternativa)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnDeshacerdireccionAlternativa = QPushButton(self.tab_direcciones)
        self.btnDeshacerdireccionAlternativa.setObjectName(u"btnDeshacerdireccionAlternativa")
        self.btnDeshacerdireccionAlternativa.setEnabled(False)
        icon14 = QIcon()
        icon14.addFile(u":/PNG/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDeshacerdireccionAlternativa.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.btnDeshacerdireccionAlternativa)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 2, 1, 1)

        self.tabwidget.addTab(self.tab_direcciones, "")
        self.tab_Datos_bancarios_financieros = QWidget()
        self.tab_Datos_bancarios_financieros.setObjectName(u"tab_Datos_bancarios_financieros")
        self.tab_Datos_bancarios_financieros.setStyleSheet(u"")
        self.gridLayout_16 = QGridLayout(self.tab_Datos_bancarios_financieros)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_9 = QFrame(self.tab_Datos_bancarios_financieros)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_5 = QFormLayout(self.frame_9)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.id_tarifa = QComboBox(self.frame_9)
        self.id_tarifa.setObjectName(u"id_tarifa")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_tarifa)

        self.label_65 = QLabel(self.frame_9)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_65)

        self.id_divisa = QComboBox(self.frame_9)
        self.id_divisa.setObjectName(u"id_divisa")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.id_divisa)

        self.label_67 = QLabel(self.frame_9)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_67)

        self.id_forma_pago = QComboBox(self.frame_9)
        self.id_forma_pago.setObjectName(u"id_forma_pago")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.id_forma_pago)

        self.label_68 = QLabel(self.frame_9)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_68)

        self.dia_pago1 = QSpinBox(self.frame_9)
        self.dia_pago1.setObjectName(u"dia_pago1")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dia_pago1)

        self.label_69 = QLabel(self.frame_9)
        self.label_69.setObjectName(u"label_69")

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_69)

        self.dia_pago2 = QSpinBox(self.frame_9)
        self.dia_pago2.setObjectName(u"dia_pago2")

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dia_pago2)

        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_5.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_32)

        self.porc_dto_cliente = QLineEdit(self.frame_9)
        self.porc_dto_cliente.setObjectName(u"porc_dto_cliente")
        self.porc_dto_cliente.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_5.setWidget(5, QFormLayout.ItemRole.FieldRole, self.porc_dto_cliente)


        self.gridLayout_16.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.tab_Datos_bancarios_financieros)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.btnVerAsientosCliente = QPushButton(self.frame_6)
        self.btnVerAsientosCliente.setObjectName(u"btnVerAsientosCliente")
        self.btnVerAsientosCliente.setMinimumSize(QSize(0, 27))

        self.gridLayout_15.addWidget(self.btnVerAsientosCliente, 1, 0, 1, 2)

        self.label_72 = QLabel(self.frame_6)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_15.addWidget(self.label_72, 3, 0, 1, 1)

        self.cuenta_iva_repercutido = QLineEdit(self.frame_6)
        self.cuenta_iva_repercutido.setObjectName(u"cuenta_iva_repercutido")

        self.gridLayout_15.addWidget(self.cuenta_iva_repercutido, 3, 1, 1, 1)

        self.label_74 = QLabel(self.frame_6)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_15.addWidget(self.label_74, 5, 0, 1, 1)

        self.label_70 = QLabel(self.frame_6)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_15.addWidget(self.label_70, 0, 0, 1, 1)

        self.cuenta_deudas = QLineEdit(self.frame_6)
        self.cuenta_deudas.setObjectName(u"cuenta_deudas")

        self.gridLayout_15.addWidget(self.cuenta_deudas, 4, 1, 1, 1)

        self.cuenta_contable = QLineEdit(self.frame_6)
        self.cuenta_contable.setObjectName(u"cuenta_contable")

        self.gridLayout_15.addWidget(self.cuenta_contable, 2, 1, 1, 1)

        self.label_73 = QLabel(self.frame_6)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_15.addWidget(self.label_73, 4, 0, 1, 1)

        self.label_71 = QLabel(self.frame_6)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_15.addWidget(self.label_71, 2, 0, 1, 1)

        self.cuenta_cobros = QLineEdit(self.frame_6)
        self.cuenta_cobros.setObjectName(u"cuenta_cobros")

        self.gridLayout_15.addWidget(self.cuenta_cobros, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_2, 6, 1, 1, 1)


        self.gridLayout_16.addWidget(self.frame_6, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.tab_Datos_bancarios_financieros)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_75 = QLabel(self.frame_7)
        self.label_75.setObjectName(u"label_75")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy5)

        self.gridLayout_14.addWidget(self.label_75, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.irpf = QCheckBox(self.frame_7)
        self.irpf.setObjectName(u"irpf")

        self.horizontalLayout_3.addWidget(self.irpf)

        self.recargo_equivalencia = QCheckBox(self.frame_7)
        self.recargo_equivalencia.setObjectName(u"recargo_equivalencia")

        self.horizontalLayout_3.addWidget(self.recargo_equivalencia)


        self.gridLayout_14.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.iban = QLineEdit(self.frame_7)
        self.iban.setObjectName(u"iban")
        self.iban.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_31.addWidget(self.iban, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_31.addWidget(self.label_5, 8, 0, 1, 1)

        self.importe_a_cuenta = QLineEdit(self.frame_7)
        self.importe_a_cuenta.setObjectName(u"importe_a_cuenta")
        self.importe_a_cuenta.setEnabled(False)
        self.importe_a_cuenta.setMaximumSize(QSize(150, 16777215))
        self.importe_a_cuenta.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.importe_a_cuenta.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_31.addWidget(self.importe_a_cuenta, 3, 1, 1, 1)

        self.label_76 = QLabel(self.frame_7)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_31.addWidget(self.label_76, 3, 0, 1, 1)

        self.label_78 = QLabel(self.frame_7)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_31.addWidget(self.label_78, 4, 0, 1, 1)

        self.bic_swift = QLineEdit(self.frame_7)
        self.bic_swift.setObjectName(u"bic_swift")
        self.bic_swift.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_31.addWidget(self.bic_swift, 8, 1, 1, 1)

        self.lblCuentavalida = QLabel(self.frame_7)
        self.lblCuentavalida.setObjectName(u"lblCuentavalida")

        self.gridLayout_31.addWidget(self.lblCuentavalida, 4, 3, 1, 1)

        self.grupo_iva = QComboBox(self.frame_7)
        self.grupo_iva.setObjectName(u"grupo_iva")

        self.gridLayout_31.addWidget(self.grupo_iva, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_31.addWidget(self.label_8, 2, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_31, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_7, 1, 0, 1, 2)

        self.tabwidget.addTab(self.tab_Datos_bancarios_financieros, "")
        self.tab_estadistica = QWidget()
        self.tab_estadistica.setObjectName(u"tab_estadistica")
        self.tab_estadistica.setStyleSheet(u"")
        self.gridLayout_24 = QGridLayout(self.tab_estadistica)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_66 = QGridLayout()
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_66.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.deuda_actual = QLineEdit(self.tab_estadistica)
        self.deuda_actual.setObjectName(u"deuda_actual")
        self.deuda_actual.setEnabled(True)
        self.deuda_actual.setMaximumSize(QSize(100, 16777215))
        self.deuda_actual.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.deuda_actual.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.deuda_actual.setReadOnly(True)

        self.gridLayout_66.addWidget(self.deuda_actual, 2, 1, 1, 1)

        self.ventas_ejercicio = QLineEdit(self.tab_estadistica)
        self.ventas_ejercicio.setObjectName(u"ventas_ejercicio")
        self.ventas_ejercicio.setEnabled(True)
        self.ventas_ejercicio.setMaximumSize(QSize(100, 16777215))
        self.ventas_ejercicio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ventas_ejercicio.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ventas_ejercicio.setReadOnly(True)

        self.gridLayout_66.addWidget(self.ventas_ejercicio, 3, 1, 1, 1)

        self.acumulado_ventas = QLineEdit(self.tab_estadistica)
        self.acumulado_ventas.setObjectName(u"acumulado_ventas")
        self.acumulado_ventas.setEnabled(True)
        self.acumulado_ventas.setMaximumSize(QSize(100, 16777215))
        self.acumulado_ventas.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.acumulado_ventas.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.acumulado_ventas.setReadOnly(True)

        self.gridLayout_66.addWidget(self.acumulado_ventas, 0, 1, 1, 1)

        self.label_37 = QLabel(self.tab_estadistica)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_66.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_38 = QLabel(self.tab_estadistica)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_66.addWidget(self.label_38, 2, 0, 1, 1)

        self.label_39 = QLabel(self.tab_estadistica)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_66.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_36 = QLabel(self.tab_estadistica)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_66.addWidget(self.label_36, 0, 0, 1, 1)

        self.fecha_ultima_compra = QLineEdit(self.tab_estadistica)
        self.fecha_ultima_compra.setObjectName(u"fecha_ultima_compra")
        self.fecha_ultima_compra.setMaximumSize(QSize(100, 16777215))
        self.fecha_ultima_compra.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_66.addWidget(self.fecha_ultima_compra, 1, 1, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_66, 0, 1, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.septiembre = QLineEdit(self.tab_estadistica)
        self.septiembre.setObjectName(u"septiembre")
        self.septiembre.setEnabled(True)
        self.septiembre.setMaximumSize(QSize(120, 16777215))
        self.septiembre.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.septiembre.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.septiembre.setReadOnly(True)

        self.gridLayout_23.addWidget(self.septiembre, 2, 3, 1, 1)

        self.label_56 = QLabel(self.tab_estadistica)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_56, 5, 2, 1, 1)

        self.label_57 = QLabel(self.tab_estadistica)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_57, 3, 2, 1, 1)

        self.label_55 = QLabel(self.tab_estadistica)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_55, 1, 2, 1, 1)

        self.label_54 = QLabel(self.tab_estadistica)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_54, 0, 2, 1, 1)

        self.agosto = QLineEdit(self.tab_estadistica)
        self.agosto.setObjectName(u"agosto")
        self.agosto.setEnabled(True)
        self.agosto.setMaximumSize(QSize(120, 16777215))
        self.agosto.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.agosto.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.agosto.setReadOnly(True)

        self.gridLayout_23.addWidget(self.agosto, 1, 3, 1, 1)

        self.label_53 = QLabel(self.tab_estadistica)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_53, 4, 2, 1, 1)

        self.marzo = QLineEdit(self.tab_estadistica)
        self.marzo.setObjectName(u"marzo")
        self.marzo.setEnabled(True)
        self.marzo.setMaximumSize(QSize(120, 16777215))
        self.marzo.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.marzo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.marzo.setReadOnly(True)

        self.gridLayout_23.addWidget(self.marzo, 2, 1, 1, 1)

        self.enero = QLineEdit(self.tab_estadistica)
        self.enero.setObjectName(u"enero")
        self.enero.setEnabled(True)
        self.enero.setMaximumSize(QSize(120, 16777215))
        self.enero.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.enero.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.enero.setReadOnly(True)

        self.gridLayout_23.addWidget(self.enero, 0, 1, 1, 1)

        self.label_51 = QLabel(self.tab_estadistica)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_51, 4, 0, 1, 1)

        self.febrero = QLineEdit(self.tab_estadistica)
        self.febrero.setObjectName(u"febrero")
        self.febrero.setEnabled(True)
        self.febrero.setMaximumSize(QSize(120, 16777215))
        self.febrero.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.febrero.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.febrero.setReadOnly(True)

        self.gridLayout_23.addWidget(self.febrero, 1, 1, 1, 1)

        self.label_48 = QLabel(self.tab_estadistica)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_48, 1, 0, 1, 1)

        self.label_58 = QLabel(self.tab_estadistica)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_58, 2, 2, 1, 1)

        self.junio = QLineEdit(self.tab_estadistica)
        self.junio.setObjectName(u"junio")
        self.junio.setEnabled(True)
        self.junio.setMaximumSize(QSize(120, 16777215))
        self.junio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.junio.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.junio.setReadOnly(True)

        self.gridLayout_23.addWidget(self.junio, 5, 1, 1, 1)

        self.label_50 = QLabel(self.tab_estadistica)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_50, 3, 0, 1, 1)

        self.noviembre = QLineEdit(self.tab_estadistica)
        self.noviembre.setObjectName(u"noviembre")
        self.noviembre.setEnabled(True)
        self.noviembre.setMaximumSize(QSize(120, 16777215))
        self.noviembre.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.noviembre.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.noviembre.setReadOnly(True)

        self.gridLayout_23.addWidget(self.noviembre, 4, 3, 1, 1)

        self.octubre = QLineEdit(self.tab_estadistica)
        self.octubre.setObjectName(u"octubre")
        self.octubre.setEnabled(True)
        self.octubre.setMaximumSize(QSize(120, 16777215))
        self.octubre.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.octubre.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.octubre.setReadOnly(True)

        self.gridLayout_23.addWidget(self.octubre, 3, 3, 1, 1)

        self.julio = QLineEdit(self.tab_estadistica)
        self.julio.setObjectName(u"julio")
        self.julio.setEnabled(True)
        self.julio.setMaximumSize(QSize(120, 16777215))
        self.julio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.julio.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.julio.setReadOnly(True)

        self.gridLayout_23.addWidget(self.julio, 0, 3, 1, 1)

        self.label_52 = QLabel(self.tab_estadistica)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_52, 5, 0, 1, 1)

        self.label_49 = QLabel(self.tab_estadistica)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_49, 2, 0, 1, 1)

        self.abril = QLineEdit(self.tab_estadistica)
        self.abril.setObjectName(u"abril")
        self.abril.setEnabled(True)
        self.abril.setMaximumSize(QSize(120, 16777215))
        self.abril.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.abril.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.abril.setReadOnly(True)

        self.gridLayout_23.addWidget(self.abril, 3, 1, 1, 1)

        self.label_47 = QLabel(self.tab_estadistica)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_47, 0, 0, 1, 1)

        self.mayo = QLineEdit(self.tab_estadistica)
        self.mayo.setObjectName(u"mayo")
        self.mayo.setEnabled(True)
        self.mayo.setMaximumSize(QSize(120, 16777215))
        self.mayo.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mayo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.mayo.setReadOnly(True)

        self.gridLayout_23.addWidget(self.mayo, 4, 1, 1, 1)

        self.diciembre = QLineEdit(self.tab_estadistica)
        self.diciembre.setObjectName(u"diciembre")
        self.diciembre.setEnabled(True)
        self.diciembre.setMaximumSize(QSize(120, 16777215))
        self.diciembre.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.diciembre.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.diciembre.setReadOnly(True)

        self.gridLayout_23.addWidget(self.diciembre, 5, 3, 1, 1)

        self.ChartWidget = QWidget(self.tab_estadistica)
        self.ChartWidget.setObjectName(u"ChartWidget")

        self.gridLayout_23.addWidget(self.ChartWidget, 6, 0, 1, 4)


        self.gridLayout_24.addLayout(self.gridLayout_23, 0, 0, 1, 1)

        self.tabwidget.addTab(self.tab_estadistica, "")
        self.tab_deudas = QWidget()
        self.tab_deudas.setObjectName(u"tab_deudas")
        self.tab_deudas.setStyleSheet(u"")
        self.gridLayout_20 = QGridLayout(self.tab_deudas)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.btnCobroTotal = QPushButton(self.tab_deudas)
        self.btnCobroTotal.setObjectName(u"btnCobroTotal")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/PNG/Fp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCobroTotal.setIcon(icon15)
        self.btnCobroTotal.setIconSize(QSize(34, 34))

        self.gridLayout_20.addWidget(self.btnCobroTotal, 3, 1, 1, 1)

        self.label_83 = QLabel(self.tab_deudas)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"background: #304163;\n"
"color: rgb(255,255,255);")
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_83, 0, 0, 1, 1)

        self.frame = QFrame(self.tab_deudas)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radPendientes = QRadioButton(self.frame)
        self.radPendientes.setObjectName(u"radPendientes")
        self.radPendientes.setChecked(True)

        self.verticalLayout.addWidget(self.radPendientes)

        self.radPagadas = QRadioButton(self.frame)
        self.radPagadas.setObjectName(u"radPagadas")

        self.verticalLayout.addWidget(self.radPagadas)


        self.gridLayout_20.addWidget(self.frame, 1, 1, 1, 1)

        self.TablaDeudas = QTableView(self.tab_deudas)
        self.TablaDeudas.setObjectName(u"TablaDeudas")
        self.TablaDeudas.setAlternatingRowColors(True)
        self.TablaDeudas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TablaDeudas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TablaDeudas.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_20.addWidget(self.TablaDeudas, 1, 0, 4, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.label_84 = QLabel(self.tab_deudas)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"background: #304163;\n"
"color: rgb(255,255,255);")
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_84, 5, 0, 1, 2)

        self.tablahistorial_deudas = QTableView(self.tab_deudas)
        self.tablahistorial_deudas.setObjectName(u"tablahistorial_deudas")

        self.gridLayout_20.addWidget(self.tablahistorial_deudas, 6, 0, 1, 2)

        self.tabwidget.addTab(self.tab_deudas, "")
        self.tab_coments = QWidget()
        self.tab_coments.setObjectName(u"tab_coments")
        self.tab_coments.setStyleSheet(u"")
        self.gridLayout_18 = QGridLayout(self.tab_coments)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_5 = QFrame(self.tab_coments)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_62 = QLabel(self.frame_5)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_8.addWidget(self.label_62, 2, 0, 1, 1)

        self.riesgo_maximo = QLineEdit(self.frame_5)
        self.riesgo_maximo.setObjectName(u"riesgo_maximo")
        self.riesgo_maximo.setEnabled(True)
        self.riesgo_maximo.setMaximumSize(QSize(100, 16777215))
        self.riesgo_maximo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.riesgo_maximo, 1, 2, 1, 1)

        self.label_34 = QLabel(self.frame_5)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_8.addWidget(self.label_34, 0, 0, 1, 1)

        self.label_63 = QLabel(self.frame_5)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_8.addWidget(self.label_63, 0, 3, 1, 1)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_8.addWidget(self.label_35, 1, 0, 1, 1)

        self.id_transportista = QComboBox(self.frame_5)
        self.id_transportista.setObjectName(u"id_transportista")

        self.gridLayout_8.addWidget(self.id_transportista, 2, 2, 1, 4)

        self.id_agente = QComboBox(self.frame_5)
        self.id_agente.setObjectName(u"id_agente")
        self.id_agente.setMinimumSize(QSize(200, 0))

        self.gridLayout_8.addWidget(self.id_agente, 0, 4, 1, 2)

        self.fecha_alta = QLineEdit(self.frame_5)
        self.fecha_alta.setObjectName(u"fecha_alta")

        self.gridLayout_8.addWidget(self.fecha_alta, 0, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)


        self.gridLayout_18.addWidget(self.frame_5, 3, 0, 1, 4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.bloqueado = QCheckBox(self.tab_coments)
        self.bloqueado.setObjectName(u"bloqueado")

        self.verticalLayout_6.addWidget(self.bloqueado)

        self.comentario_bloqueo = QTextEdit(self.tab_coments)
        self.comentario_bloqueo.setObjectName(u"comentario_bloqueo")
        self.comentario_bloqueo.setEnabled(True)
        self.comentario_bloqueo.setUndoRedoEnabled(True)
        self.comentario_bloqueo.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.comentario_bloqueo)

        self.label_43 = QLabel(self.tab_coments)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_6.addWidget(self.label_43)

        self.acceso_web = QLineEdit(self.tab_coments)
        self.acceso_web.setObjectName(u"acceso_web")

        self.verticalLayout_6.addWidget(self.acceso_web)

        self.label_44 = QLabel(self.tab_coments)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_6.addWidget(self.label_44)

        self.password_web = QLineEdit(self.tab_coments)
        self.password_web.setObjectName(u"password_web")

        self.verticalLayout_6.addWidget(self.password_web)


        self.gridLayout_18.addLayout(self.verticalLayout_6, 0, 0, 3, 1)

        self.label_82 = QLabel(self.tab_coments)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(16777215, 21))

        self.gridLayout_18.addWidget(self.label_82, 0, 1, 1, 2)

        self.id_idioma_documentos = QComboBox(self.tab_coments)
        self.id_idioma_documentos.setObjectName(u"id_idioma_documentos")

        self.gridLayout_18.addWidget(self.id_idioma_documentos, 2, 3, 1, 1)

        self.label_9 = QLabel(self.tab_coments)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_18.addWidget(self.label_9, 2, 2, 1, 1)

        self.txtcomentarios = QTextEdit(self.tab_coments)
        self.txtcomentarios.setObjectName(u"txtcomentarios")

        self.gridLayout_18.addWidget(self.txtcomentarios, 1, 1, 1, 3)

        self.tabwidget.addTab(self.tab_coments, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_22 = QGridLayout(self.tab_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(250, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget_2 = QTabWidget(self.frame_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget_2.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget_2.setMovable(True)
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_19 = QGridLayout(self.tab_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.tablaPresupuestos = QTableView(self.tab_13)
        self.tablaPresupuestos.setObjectName(u"tablaPresupuestos")
        self.tablaPresupuestos.setAlternatingRowColors(True)
        self.tablaPresupuestos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaPresupuestos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaPresupuestos.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_19.addWidget(self.tablaPresupuestos, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_26 = QGridLayout(self.tab_9)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.tablaPedidos = QTableView(self.tab_9)
        self.tablaPedidos.setObjectName(u"tablaPedidos")
        self.tablaPedidos.setAlternatingRowColors(True)
        self.tablaPedidos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaPedidos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaPedidos.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_26.addWidget(self.tablaPedidos, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_6 = QGridLayout(self.tab_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.TablaAlbaranes = QTableView(self.tab_7)
        self.TablaAlbaranes.setObjectName(u"TablaAlbaranes")
        self.TablaAlbaranes.setAlternatingRowColors(True)
        self.TablaAlbaranes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TablaAlbaranes.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.TablaAlbaranes, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_Facturas = QWidget()
        self.tab_Facturas.setObjectName(u"tab_Facturas")
        self.gridLayout_11 = QGridLayout(self.tab_Facturas)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tablaFacturas = QTableView(self.tab_Facturas)
        self.tablaFacturas.setObjectName(u"tablaFacturas")
        self.tablaFacturas.setAlternatingRowColors(True)
        self.tablaFacturas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaFacturas.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_11.addWidget(self.tablaFacturas, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_Facturas, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_13 = QGridLayout(self.tab_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.tablaProyectos = QTableView(self.tab_12)
        self.tablaProyectos.setObjectName(u"tablaProyectos")
        self.tablaProyectos.setAlternatingRowColors(True)
        self.tablaProyectos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaProyectos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaProyectos.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_13.addWidget(self.tablaProyectos, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")

        self.horizontalLayout_5.addWidget(self.tabWidget_2)

        self.frameConta = QFrame(self.frame_3)
        self.frameConta.setObjectName(u"frameConta")
        self.frameConta.setMinimumSize(QSize(0, 0))
        self.frameConta.setMaximumSize(QSize(373, 16777215))
        self.frameConta.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameConta.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frameConta)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tablaAsientos = QTableView(self.frameConta)
        self.tablaAsientos.setObjectName(u"tablaAsientos")

        self.gridLayout_21.addWidget(self.tablaAsientos, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frameConta)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background: #304163;\n"
"color: rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_10, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frameConta)


        self.gridLayout_22.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tabwidget.addTab(self.tab_3, "")

        self.gridLayout_27.addWidget(self.tabwidget, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.paginaedicion)
        self.paginaBisquedas = QWidget()
        self.paginaBisquedas.setObjectName(u"paginaBisquedas")
        self.gridLayout_28 = QGridLayout(self.paginaBisquedas)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(-1, -1, 20, -1)
        self.tabla_busquedas = QTableView(self.paginaBisquedas)
        self.tabla_busquedas.setObjectName(u"tabla_busquedas")
        self.tabla_busquedas.setAutoFillBackground(True)
        self.tabla_busquedas.setAlternatingRowColors(True)
        self.tabla_busquedas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla_busquedas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_busquedas.setGridStyle(Qt.PenStyle.DotLine)
        self.tabla_busquedas.setSortingEnabled(True)
        self.tabla_busquedas.setCornerButtonEnabled(False)
        self.tabla_busquedas.horizontalHeader().setStretchLastSection(True)
        self.tabla_busquedas.verticalHeader().setVisible(False)

        self.gridLayout_28.addWidget(self.tabla_busquedas, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.paginaBisquedas)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 5)

        QWidget.setTabOrder(self.btnAnadir, self.btnSiguiente)
        QWidget.setTabOrder(self.btnSiguiente, self.btnAnterior)
        QWidget.setTabOrder(self.btnAnterior, self.btnBuscar)
        QWidget.setTabOrder(self.btnBuscar, self.btnEditar)
        QWidget.setTabOrder(self.btnEditar, self.btnGuardar)
        QWidget.setTabOrder(self.btnGuardar, self.btnDeshacer)
        QWidget.setTabOrder(self.btnDeshacer, self.btnBorrar)
        QWidget.setTabOrder(self.btnBorrar, self.codigo_cliente)
        QWidget.setTabOrder(self.codigo_cliente, self.cif_vies)
        QWidget.setTabOrder(self.cif_vies, self.cif_nif_siret)
        QWidget.setTabOrder(self.cif_nif_siret, self.nombre)
        QWidget.setTabOrder(self.nombre, self.apellido1)
        QWidget.setTabOrder(self.apellido1, self.apellido2)
        QWidget.setTabOrder(self.apellido2, self.nombre_fiscal)
        QWidget.setTabOrder(self.nombre_fiscal, self.nombre_comercial)
        QWidget.setTabOrder(self.nombre_comercial, self.cp)
        QWidget.setTabOrder(self.cp, self.poblacion)
        QWidget.setTabOrder(self.poblacion, self.provincia)
        QWidget.setTabOrder(self.provincia, self.telefono1)
        QWidget.setTabOrder(self.telefono1, self.telefono2)
        QWidget.setTabOrder(self.telefono2, self.email)
        QWidget.setTabOrder(self.email, self.web)
        QWidget.setTabOrder(self.web, self.observaciones)
        QWidget.setTabOrder(self.observaciones, self.btnVer_OtrosContactos)
        QWidget.setTabOrder(self.btnVer_OtrosContactos, self.lista_tipos)
        QWidget.setTabOrder(self.lista_tipos, self.btnEdita_tipoCliente)
        QWidget.setTabOrder(self.btnEdita_tipoCliente, self.tabwidget)
        QWidget.setTabOrder(self.tabwidget, self.lista_direccionesAlternativas)
        QWidget.setTabOrder(self.lista_direccionesAlternativas, self.descripcion_direccion)
        QWidget.setTabOrder(self.descripcion_direccion, self.poblacion_alternativa)
        QWidget.setTabOrder(self.poblacion_alternativa, self.txtpoblacionAlternativa)
        QWidget.setTabOrder(self.txtpoblacionAlternativa, self.txtdireccion1Alternativa1)
        QWidget.setTabOrder(self.txtdireccion1Alternativa1, self.txtdireccion1Alternativa2)
        QWidget.setTabOrder(self.txtdireccion1Alternativa2, self.txtprovinciaAlternativa)
        QWidget.setTabOrder(self.txtprovinciaAlternativa, self.cbopaisAlternativa)
        QWidget.setTabOrder(self.cbopaisAlternativa, self.txtemail_alternativa)
        QWidget.setTabOrder(self.txtemail_alternativa, self.txtcomentarios_alternativa)
        QWidget.setTabOrder(self.txtcomentarios_alternativa, self.btnAnadirdireccion)
        QWidget.setTabOrder(self.btnAnadirdireccion, self.btnEditardireccionAlternativa)
        QWidget.setTabOrder(self.btnEditardireccionAlternativa, self.btnBorrardireccion)
        QWidget.setTabOrder(self.btnBorrardireccion, self.btnGuardardireccionAlternativa)
        QWidget.setTabOrder(self.btnGuardardireccionAlternativa, self.btnDeshacerdireccionAlternativa)
        QWidget.setTabOrder(self.btnDeshacerdireccionAlternativa, self.id_tarifa)
        QWidget.setTabOrder(self.id_tarifa, self.id_divisa)
        QWidget.setTabOrder(self.id_divisa, self.id_forma_pago)
        QWidget.setTabOrder(self.id_forma_pago, self.dia_pago1)
        QWidget.setTabOrder(self.dia_pago1, self.dia_pago2)
        QWidget.setTabOrder(self.dia_pago2, self.porc_dto_cliente)
        QWidget.setTabOrder(self.porc_dto_cliente, self.btnVerAsientosCliente)
        QWidget.setTabOrder(self.btnVerAsientosCliente, self.cuenta_contable)
        QWidget.setTabOrder(self.cuenta_contable, self.cuenta_iva_repercutido)
        QWidget.setTabOrder(self.cuenta_iva_repercutido, self.cuenta_deudas)
        QWidget.setTabOrder(self.cuenta_deudas, self.cuenta_cobros)
        QWidget.setTabOrder(self.cuenta_cobros, self.irpf)
        QWidget.setTabOrder(self.irpf, self.recargo_equivalencia)
        QWidget.setTabOrder(self.recargo_equivalencia, self.TablaDeudas)
        QWidget.setTabOrder(self.TablaDeudas, self.radPendientes)
        QWidget.setTabOrder(self.radPendientes, self.radPagadas)
        QWidget.setTabOrder(self.radPagadas, self.btnCobroTotal)
        QWidget.setTabOrder(self.btnCobroTotal, self.tablahistorial_deudas)
        QWidget.setTabOrder(self.tablahistorial_deudas, self.bloqueado)
        QWidget.setTabOrder(self.bloqueado, self.comentario_bloqueo)
        QWidget.setTabOrder(self.comentario_bloqueo, self.acceso_web)
        QWidget.setTabOrder(self.acceso_web, self.password_web)
        QWidget.setTabOrder(self.password_web, self.id_agente)
        QWidget.setTabOrder(self.id_agente, self.riesgo_maximo)
        QWidget.setTabOrder(self.riesgo_maximo, self.id_transportista)
        QWidget.setTabOrder(self.id_transportista, self.txtcomentarios)
        QWidget.setTabOrder(self.txtcomentarios, self.id_idioma_documentos)
        QWidget.setTabOrder(self.id_idioma_documentos, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.tablaPresupuestos)
        QWidget.setTabOrder(self.tablaPresupuestos, self.tablaAsientos)
        QWidget.setTabOrder(self.tablaAsientos, self.tablaPedidos)
        QWidget.setTabOrder(self.tablaPedidos, self.TablaAlbaranes)
        QWidget.setTabOrder(self.TablaAlbaranes, self.tablaFacturas)
        QWidget.setTabOrder(self.tablaFacturas, self.tablaProyectos)
        QWidget.setTabOrder(self.tablaProyectos, self.tabla_busquedas)

        self.retranslateUi(frmClientes)

        self.stackedWidget.setCurrentIndex(0)
        self.tabwidget.setCurrentIndex(0)
        self.blink_stack.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frmClientes)
    # setupUi

    def retranslateUi(self, frmClientes):
        frmClientes.setWindowTitle(QCoreApplication.translate("frmClientes", u"Gestion de clientes", None))
        self.textoTitulo.setText(QCoreApplication.translate("frmClientes", u"Gesti\u00f3n de Clientes - Datos administrativos", None))
        self.label_40.setText(QCoreApplication.translate("frmClientes", u"Cliente:", None))
        self.lbl_nombre_fiscal.setText(QCoreApplication.translate("frmClientes", u"NOMBRE FISCAL CLIENTE", None))
        self.btnEditar.setText(QCoreApplication.translate("frmClientes", u"&Editar", None))
        self.btnBuscar.setText(QCoreApplication.translate("frmClientes", u"&Buscar", None))
        self.btnAnadir.setText(QCoreApplication.translate("frmClientes", u"&Nuevo", None))
        self.btnSiguiente.setText(QCoreApplication.translate("frmClientes", u"&Siguiente", None))
        self.btnDeshacer.setText(QCoreApplication.translate("frmClientes", u"&Deshacer", None))
        self.btnGuardar.setText(QCoreApplication.translate("frmClientes", u"&Guardar", None))
        self.btnBorrar.setText(QCoreApplication.translate("frmClientes", u"B&orrar", None))
        self.btnAnterior.setText(QCoreApplication.translate("frmClientes", u"&Anterior", None))
        self.btnCerrar.setText(QCoreApplication.translate("frmClientes", u"Cerrar", None))
#if QT_CONFIG(tooltip)
        self.btnVer_OtrosContactos.setToolTip(QCoreApplication.translate("frmClientes", u"Otras personas de contacto", None))
#endif // QT_CONFIG(tooltip)
        self.btnVer_OtrosContactos.setText(QCoreApplication.translate("frmClientes", u"Personas de contacto", None))
        self.label_46.setText(QCoreApplication.translate("frmClientes", u"TIPO CLIENTE", None))
        self.btnEdita_tipoCliente.setText(QCoreApplication.translate("frmClientes", u"Editar tipo de cliente", None))
        ___qtreewidgetitem = self.lista_tipos.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("frmClientes", u"Tipo", None));
        self.lista_tipos.setStyleSheet("")
        self.btnValidarVIES.setStyleSheet("")
        self.btnValidarVIES.setText(QCoreApplication.translate("frmClientes", u"Validar VIES", None))
        self.label_12.setStyleSheet("")
        self.label_12.setText(QCoreApplication.translate("frmClientes", u"Nombre Comercial:", None))
        self.lblSegundoApellido.setStyleSheet("")
        self.lblSegundoApellido.setText(QCoreApplication.translate("frmClientes", u"Segundo Apellido:", None))
        self.label_25.setStyleSheet("")
        self.label_25.setText(QCoreApplication.translate("frmClientes", u"Observaciones:", None))
        self.label_3.setStyleSheet("")
        self.label_3.setText(QCoreApplication.translate("frmClientes", u"Nombre", None))
        self.label_18.setStyleSheet("")
        self.label_18.setText(QCoreApplication.translate("frmClientes", u"Pais:", None))
        self.label_20.setStyleSheet("")
        self.label_20.setText(QCoreApplication.translate("frmClientes", u"Tel\u00e9fono 2:", None))
        self.label_4.setStyleSheet("")
        self.label_4.setText(QCoreApplication.translate("frmClientes", u"Primer Apellido:", None))
        self.lblCIF_IVA_UE.setStyleSheet("")
        self.lblCIF_IVA_UE.setText(QCoreApplication.translate("frmClientes", u"CIF IVA UE:", None))
        self.LblSIRET.setText(QCoreApplication.translate("frmClientes", u"SIRET", None))
        self.label_2.setStyleSheet("")
        self.label_2.setText(QCoreApplication.translate("frmClientes", u"Cif/Nif:", None))
        self.label_13.setStyleSheet("")
        self.label_13.setText(QCoreApplication.translate("frmClientes", u"Direcci\u00f3n:", None))
        self.label_23.setStyleSheet("")
        self.label_23.setText(QCoreApplication.translate("frmClientes", u"web:", None))
        self.label_11.setStyleSheet("")
        self.label_11.setText(QCoreApplication.translate("frmClientes", u"Nombre Fiscal:", None))
        self.label_22.setStyleSheet("")
        self.label_22.setText(QCoreApplication.translate("frmClientes", u"M\u00f3vil:", None))
        self.label_15.setStyleSheet("")
        self.label_15.setText(QCoreApplication.translate("frmClientes", u"CP:", None))
        self.label.setText(QCoreApplication.translate("frmClientes", u"C\u00f3digo:                        ", None))
        self.label_16.setStyleSheet("")
        self.label_16.setText(QCoreApplication.translate("frmClientes", u"Poblaci\u00f3n:", None))
        self.label_24.setStyleSheet("")
        self.label_24.setText(QCoreApplication.translate("frmClientes", u"Mail:", None))
        self.lblProvincia.setStyleSheet("")
        self.lblProvincia.setText(QCoreApplication.translate("frmClientes", u"Provincia:", None))
        self.label_19.setStyleSheet("")
        self.label_19.setText(QCoreApplication.translate("frmClientes", u"Tel\u00e9fono1:", None))
        self.label_14.setStyleSheet("")
        self.label_14.setText(QCoreApplication.translate("frmClientes", u"Direccion 2:", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_datos), QCoreApplication.translate("frmClientes", u"Cliente", None))
        self.label_7.setText(QCoreApplication.translate("frmClientes", u"DIRECCIONES", None))
        self.label_6.setText(QCoreApplication.translate("frmClientes", u"Descripci\u00f3n:", None))
        self.label_29.setText(QCoreApplication.translate("frmClientes", u"C.P.:", None))
        self.label_66.setText(QCoreApplication.translate("frmClientes", u"Poblaci\u00f3n", None))
        self.label_27.setText(QCoreApplication.translate("frmClientes", u"Direcci\u00f3n:", None))
        self.label_28.setText(QCoreApplication.translate("frmClientes", u"Direcci\u00f3n 2:", None))
        self.lblProvinciaAlternativa.setText(QCoreApplication.translate("frmClientes", u"Provincia:", None))
        self.label_31.setText(QCoreApplication.translate("frmClientes", u"Pais:", None))
        self.label_64.setText(QCoreApplication.translate("frmClientes", u"email:", None))
        self.label_86.setText(QCoreApplication.translate("frmClientes", u"Comentarios:", None))
#if QT_CONFIG(tooltip)
        self.btnAnadirdireccion.setToolTip(QCoreApplication.translate("frmClientes", u"A\u00f1adir nueva direcci\u00f3n alternativa", None))
#endif // QT_CONFIG(tooltip)
        self.btnAnadirdireccion.setText(QCoreApplication.translate("frmClientes", u"A\u00f1adir", None))
        self.btnEditardireccionAlternativa.setText(QCoreApplication.translate("frmClientes", u"Editar", None))
#if QT_CONFIG(tooltip)
        self.btnBorrardireccion.setToolTip(QCoreApplication.translate("frmClientes", u"Borrar una direcci\u00f3n alternativa", None))
#endif // QT_CONFIG(tooltip)
        self.btnBorrardireccion.setText(QCoreApplication.translate("frmClientes", u"Borrar", None))
        self.btnGuardardireccionAlternativa.setText(QCoreApplication.translate("frmClientes", u"Guardar", None))
        self.btnDeshacerdireccionAlternativa.setText(QCoreApplication.translate("frmClientes", u"Deshacer", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_direcciones), QCoreApplication.translate("frmClientes", u"Direcciones alternativas", None))
        self.label_33.setText(QCoreApplication.translate("frmClientes", u"Tarifa Cliente:", None))
        self.label_65.setText(QCoreApplication.translate("frmClientes", u"Divisa:", None))
        self.label_67.setText(QCoreApplication.translate("frmClientes", u"Forma de Pago:", None))
        self.label_68.setText(QCoreApplication.translate("frmClientes", u"D\u00eda de pago 1:", None))
        self.label_69.setText(QCoreApplication.translate("frmClientes", u"D\u00eda de pago 2:", None))
        self.label_32.setText(QCoreApplication.translate("frmClientes", u"Porcentaje DTO Fijo:", None))
        self.porc_dto_cliente.setText(QCoreApplication.translate("frmClientes", u"0", None))
        self.btnVerAsientosCliente.setText(QCoreApplication.translate("frmClientes", u"Ver Asientos Cliente", None))
        self.label_72.setText(QCoreApplication.translate("frmClientes", u"Cuenta IVA Repercutido:", None))
        self.label_74.setText(QCoreApplication.translate("frmClientes", u"Cuenta Cobros:", None))
        self.label_70.setText(QCoreApplication.translate("frmClientes", u"<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#ff0000;\">Contabilidad (P.G.C):</span></p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("frmClientes", u"Cuenta deudas:", None))
        self.label_71.setText(QCoreApplication.translate("frmClientes", u"Cuenta contable:", None))
        self.label_75.setText(QCoreApplication.translate("frmClientes", u"<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#ff0000;\">Datos financieros:</span></p></body></html>", None))
        self.irpf.setText(QCoreApplication.translate("frmClientes", u"Cliente Empresa (Aplicar IRPF)", None))
        self.recargo_equivalencia.setText(QCoreApplication.translate("frmClientes", u"Recargo Equivalencia", None))
        self.label_5.setText(QCoreApplication.translate("frmClientes", u"BIC/SWIFT:", None))
        self.importe_a_cuenta.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_76.setText(QCoreApplication.translate("frmClientes", u"Entregado a cuenta:", None))
        self.label_78.setText(QCoreApplication.translate("frmClientes", u"IBAN:", None))
        self.lblCuentavalida.setText(QCoreApplication.translate("frmClientes", u"Cuenta Valida", None))
        self.label_8.setText(QCoreApplication.translate("frmClientes", u"Grupo IVA:", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_Datos_bancarios_financieros), QCoreApplication.translate("frmClientes", u"Datos Bancarios y Financieros", None))
        self.deuda_actual.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.ventas_ejercicio.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.acumulado_ventas.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_37.setText(QCoreApplication.translate("frmClientes", u"Fecha ultima compra:", None))
        self.label_38.setText(QCoreApplication.translate("frmClientes", u"Deuda Actual:", None))
        self.label_39.setText(QCoreApplication.translate("frmClientes", u"Ventas Ejercicio:", None))
        self.label_36.setText(QCoreApplication.translate("frmClientes", u"Importe Acumulado:", None))
        self.fecha_ultima_compra.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.septiembre.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_56.setText(QCoreApplication.translate("frmClientes", u"Diciembre:", None))
        self.label_57.setText(QCoreApplication.translate("frmClientes", u"Octubre:", None))
        self.label_55.setText(QCoreApplication.translate("frmClientes", u"Agosto:", None))
        self.label_54.setText(QCoreApplication.translate("frmClientes", u"Julio:", None))
        self.agosto.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_53.setText(QCoreApplication.translate("frmClientes", u"Noviembre:", None))
        self.marzo.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.enero.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_51.setText(QCoreApplication.translate("frmClientes", u"Mayo:", None))
        self.febrero.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_48.setText(QCoreApplication.translate("frmClientes", u"Febrero:", None))
        self.label_58.setText(QCoreApplication.translate("frmClientes", u"Septiembre:", None))
        self.junio.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_50.setText(QCoreApplication.translate("frmClientes", u"Abril:", None))
        self.noviembre.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.octubre.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.julio.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_52.setText(QCoreApplication.translate("frmClientes", u"Junio:", None))
        self.label_49.setText(QCoreApplication.translate("frmClientes", u"Marzo", None))
        self.abril.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_47.setText(QCoreApplication.translate("frmClientes", u"Enero:", None))
        self.mayo.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.diciembre.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_estadistica), QCoreApplication.translate("frmClientes", u"Estadistica", None))
        self.btnCobroTotal.setText(QCoreApplication.translate("frmClientes", u"Cobro ", None))
        self.label_83.setText(QCoreApplication.translate("frmClientes", u"Deudas", None))
        self.radPendientes.setText(QCoreApplication.translate("frmClientes", u"Pendientes", None))
        self.radPagadas.setText(QCoreApplication.translate("frmClientes", u"Pagadas", None))
        self.label_84.setText(QCoreApplication.translate("frmClientes", u"Historial de deuda", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_deudas), QCoreApplication.translate("frmClientes", u"Gesti\u00f3n deuda cliente", None))
        self.label_62.setText(QCoreApplication.translate("frmClientes", u"Transportista:", None))
        self.riesgo_maximo.setText(QCoreApplication.translate("frmClientes", u"0,00", None))
        self.label_34.setText(QCoreApplication.translate("frmClientes", u"Fecha de Alta:", None))
        self.label_63.setText(QCoreApplication.translate("frmClientes", u"Agente: ", None))
        self.label_35.setText(QCoreApplication.translate("frmClientes", u"Riesgo permitido:", None))
        self.bloqueado.setText(QCoreApplication.translate("frmClientes", u"Activar Bloqueo cliente", None))
        self.label_43.setText(QCoreApplication.translate("frmClientes", u"Usuario Acceso Web:", None))
        self.label_44.setText(QCoreApplication.translate("frmClientes", u"Password Acceso web:", None))
        self.label_82.setText(QCoreApplication.translate("frmClientes", u"Comentarios generales sobre el cliente:", None))
        self.label_9.setText(QCoreApplication.translate("frmClientes", u"idioma Documentos:", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_coments), QCoreApplication.translate("frmClientes", u"Comentarios y Otros", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), QCoreApplication.translate("frmClientes", u"Presupuestos", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("frmClientes", u"Pedidos", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("frmClientes", u"Albaranes", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_Facturas), QCoreApplication.translate("frmClientes", u"Facturas", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("frmClientes", u"Proyectos", None))
        self.label_10.setText(QCoreApplication.translate("frmClientes", u"Asientos Contables", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_3), QCoreApplication.translate("frmClientes", u"Historial", None))
    # retranslateUi

