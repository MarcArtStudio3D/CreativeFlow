# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmempresas.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QTableView, QTextEdit,
    QVBoxLayout, QWidget)
from modulos import designer_rc

class Ui_FrmEmpresas(object):
    def setupUi(self, FrmEmpresas):
        if not FrmEmpresas.objectName():
            FrmEmpresas.setObjectName(u"FrmEmpresas")
        FrmEmpresas.resize(1261, 751)
        icon = QIcon()
        icon.addFile(u":/PNG/resources/icons/png/LogoIcono.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        FrmEmpresas.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(FrmEmpresas)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(FrmEmpresas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.create_page_empresa = QWidget()
        self.create_page_empresa.setObjectName(u"create_page_empresa")
        self.gridLayout_14 = QGridLayout(self.create_page_empresa)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.btn_guardar_nuevo = QPushButton(self.create_page_empresa)
        self.btn_guardar_nuevo.setObjectName(u"btn_guardar_nuevo")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/PNG/Save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_guardar_nuevo.setIcon(icon1)

        self.gridLayout_14.addWidget(self.btn_guardar_nuevo, 4, 0, 1, 1)

        self.btn_deshacer = QPushButton(self.create_page_empresa)
        self.btn_deshacer.setObjectName(u"btn_deshacer")

        self.gridLayout_14.addWidget(self.btn_deshacer, 5, 0, 1, 1)

        self.btn_salir = QPushButton(self.create_page_empresa)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_14.addWidget(self.btn_salir, 6, 0, 1, 1)

        self.tabWidget = QTabWidget(self.create_page_empresa)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(1216, 16777215))
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout_12 = QGridLayout(self.tabWidgetPage1)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_n_rm = QLabel(self.tabWidgetPage1)
        self.label_n_rm.setObjectName(u"label_n_rm")

        self.gridLayout_6.addWidget(self.label_n_rm, 9, 8, 1, 1)

        self.label_74 = QLabel(self.tabWidgetPage1)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_6.addWidget(self.label_74, 0, 1, 1, 1)

        self.label_cif_siren = QLabel(self.tabWidgetPage1)
        self.label_cif_siren.setObjectName(u"label_cif_siren")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cif_siren.sizePolicy().hasHeightForWidth())
        self.label_cif_siren.setSizePolicy(sizePolicy)
        self.label_cif_siren.setMinimumSize(QSize(66, 0))

        self.gridLayout_6.addWidget(self.label_cif_siren, 8, 1, 1, 1)

        self.siret = QLineEdit(self.tabWidgetPage1)
        self.siret.setObjectName(u"siret")

        self.gridLayout_6.addWidget(self.siret, 8, 7, 1, 1)

        self.label_21 = QLabel(self.tabWidgetPage1)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(80, 0))

        self.gridLayout_6.addWidget(self.label_21, 12, 8, 1, 1)

        self.label_20 = QLabel(self.tabWidgetPage1)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(80, 0))

        self.gridLayout_6.addWidget(self.label_20, 12, 1, 1, 1)

        self.forma_juridica = QComboBox(self.tabWidgetPage1)
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.addItem("")
        self.forma_juridica.setObjectName(u"forma_juridica")
        self.forma_juridica.setMaximumSize(QSize(205, 16777215))
        self.forma_juridica.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.forma_juridica.setMinimumContentsLength(150)

        self.gridLayout_6.addWidget(self.forma_juridica, 0, 10, 1, 1)

        self.label_50 = QLabel(self.tabWidgetPage1)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_6.addWidget(self.label_50, 4, 4, 1, 1)

        self.registro_mercantil = QLineEdit(self.tabWidgetPage1)
        self.registro_mercantil.setObjectName(u"registro_mercantil")

        self.gridLayout_6.addWidget(self.registro_mercantil, 9, 9, 1, 3)

        self.label_18 = QLabel(self.tabWidgetPage1)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(80, 0))

        self.gridLayout_6.addWidget(self.label_18, 11, 4, 1, 1)

        self.ape_naf = QLineEdit(self.tabWidgetPage1)
        self.ape_naf.setObjectName(u"ape_naf")

        self.gridLayout_6.addWidget(self.ape_naf, 8, 9, 1, 3)

        self.label_N_RCS = QLabel(self.tabWidgetPage1)
        self.label_N_RCS.setObjectName(u"label_N_RCS")

        self.gridLayout_6.addWidget(self.label_N_RCS, 9, 1, 1, 1)

        self.label_19 = QLabel(self.tabWidgetPage1)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(80, 0))

        self.gridLayout_6.addWidget(self.label_19, 11, 8, 1, 1)

        self.label_16 = QLabel(self.tabWidgetPage1)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_16, 2, 1, 1, 1)

        self.label_17 = QLabel(self.tabWidgetPage1)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(80, 0))

        self.gridLayout_6.addWidget(self.label_17, 11, 1, 1, 1)

        self.label_13 = QLabel(self.tabWidgetPage1)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_13, 3, 1, 1, 1)

        self.label_siret = QLabel(self.tabWidgetPage1)
        self.label_siret.setObjectName(u"label_siret")

        self.gridLayout_6.addWidget(self.label_siret, 8, 6, 1, 1)

        self.ciudad_rcs = QLineEdit(self.tabWidgetPage1)
        self.ciudad_rcs.setObjectName(u"ciudad_rcs")

        self.gridLayout_6.addWidget(self.ciudad_rcs, 9, 7, 1, 1)

        self.label_APE_NAF = QLabel(self.tabWidgetPage1)
        self.label_APE_NAF.setObjectName(u"label_APE_NAF")

        self.gridLayout_6.addWidget(self.label_APE_NAF, 8, 8, 1, 1)

        self.movil = QLineEdit(self.tabWidgetPage1)
        self.movil.setObjectName(u"movil")
        self.movil.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.movil, 11, 9, 1, 1)

        self.label_23 = QLabel(self.tabWidgetPage1)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_23, 10, 1, 1, 1)

        self.label_forma_juridica = QLabel(self.tabWidgetPage1)
        self.label_forma_juridica.setObjectName(u"label_forma_juridica")

        self.gridLayout_6.addWidget(self.label_forma_juridica, 0, 9, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 13, 3, 1, 1)

        self.web = QLineEdit(self.tabWidgetPage1)
        self.web.setObjectName(u"web")

        self.gridLayout_6.addWidget(self.web, 12, 9, 1, 3)

        self.telefono2 = QLineEdit(self.tabWidgetPage1)
        self.telefono2.setObjectName(u"telefono2")
        self.telefono2.setMaximumSize(QSize(16777215, 16777215))
        self.telefono2.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.telefono2, 11, 6, 1, 1)

        self.label_ciudad_rcs = QLabel(self.tabWidgetPage1)
        self.label_ciudad_rcs.setObjectName(u"label_ciudad_rcs")

        self.gridLayout_6.addWidget(self.label_ciudad_rcs, 9, 6, 1, 1)

        self.label_14 = QLabel(self.tabWidgetPage1)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_14, 4, 1, 1, 1)

        self.cp = QLineEdit(self.tabWidgetPage1)
        self.cp.setObjectName(u"cp")
        self.cp.setMaximumSize(QSize(100, 16777215))
        self.cp.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.cp, 4, 2, 1, 1)

        self.cif_siren = QLineEdit(self.tabWidgetPage1)
        self.cif_siren.setObjectName(u"cif_siren")
        self.cif_siren.setMaximumSize(QSize(16777215, 16777215))
        self.cif_siren.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.cif_siren, 8, 2, 1, 2)

        self.rcs = QLineEdit(self.tabWidgetPage1)
        self.rcs.setObjectName(u"rcs")

        self.gridLayout_6.addWidget(self.rcs, 9, 2, 1, 1)

        self.inscripcion = QLineEdit(self.tabWidgetPage1)
        self.inscripcion.setObjectName(u"inscripcion")
        self.inscripcion.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.inscripcion, 10, 2, 1, 6)

        self.telefono1 = QLineEdit(self.tabWidgetPage1)
        self.telefono1.setObjectName(u"telefono1")
        self.telefono1.setMaximumSize(QSize(150, 16777215))
        self.telefono1.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.telefono1, 11, 2, 1, 2)

        self.email = QLineEdit(self.tabWidgetPage1)
        self.email.setObjectName(u"email")

        self.gridLayout_6.addWidget(self.email, 12, 2, 1, 5)

        self.btnBuscarPais = QPushButton(self.tabWidgetPage1)
        self.btnBuscarPais.setObjectName(u"btnBuscarPais")
        self.btnBuscarPais.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/modules/images/find.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBuscarPais.setIcon(icon2)
        self.btnBuscarPais.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.btnBuscarPais, 2, 6, 1, 1)

        self.pais = QLineEdit(self.tabWidgetPage1)
        self.pais.setObjectName(u"pais")

        self.gridLayout_6.addWidget(self.pais, 2, 2, 1, 3)

        self.codigoempresa = QLineEdit(self.tabWidgetPage1)
        self.codigoempresa.setObjectName(u"codigoempresa")
        self.codigoempresa.setMaximumSize(QSize(100, 16777215))
        self.codigoempresa.setReadOnly(False)
        self.codigoempresa.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.codigoempresa, 0, 2, 1, 1)

        self.label_43 = QLabel(self.tabWidgetPage1)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_6.addWidget(self.label_43, 0, 3, 1, 1)

        self.label_75 = QLabel(self.tabWidgetPage1)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_6.addWidget(self.label_75, 1, 3, 1, 1)

        self.nombre_fiscal = QLineEdit(self.tabWidgetPage1)
        self.nombre_fiscal.setObjectName(u"nombre_fiscal")
        self.nombre_fiscal.setMinimumSize(QSize(332, 0))
        self.nombre_fiscal.setMaximumSize(QSize(16777215, 16777215))
        self.nombre_fiscal.setReadOnly(False)
        self.nombre_fiscal.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.nombre_fiscal, 1, 4, 1, 5)

        self.nombre_comercial = QLineEdit(self.tabWidgetPage1)
        self.nombre_comercial.setObjectName(u"nombre_comercial")

        self.gridLayout_6.addWidget(self.nombre_comercial, 0, 4, 1, 5)

        self.non_tva = QCheckBox(self.tabWidgetPage1)
        self.non_tva.setObjectName(u"non_tva")

        self.gridLayout_6.addWidget(self.non_tva, 1, 10, 1, 1)

        self.direccion = QLineEdit(self.tabWidgetPage1)
        self.direccion.setObjectName(u"direccion")
        self.direccion.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.direccion, 3, 2, 1, 9)

        self.poblacion = QLineEdit(self.tabWidgetPage1)
        self.poblacion.setObjectName(u"poblacion")
        self.poblacion.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.poblacion, 4, 5, 1, 4)

        self.label_provincia = QLabel(self.tabWidgetPage1)
        self.label_provincia.setObjectName(u"label_provincia")
        sizePolicy.setHeightForWidth(self.label_provincia.sizePolicy().hasHeightForWidth())
        self.label_provincia.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.label_provincia, 4, 9, 1, 1)

        self.provincia = QLineEdit(self.tabWidgetPage1)
        self.provincia.setObjectName(u"provincia")
        self.provincia.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.provincia, 4, 10, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_6, 2, 0, 1, 4)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_24 = QGridLayout(self.tab)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setMinimumSize(QSize(0, 0))
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_21 = QGridLayout(self.tab_12)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.groupBox_14 = QGroupBox(self.tab_12)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy1)
        self.gridLayout_16 = QGridLayout(self.groupBox_14)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.id_divisa = QComboBox(self.groupBox_14)
        self.id_divisa.setObjectName(u"id_divisa")

        self.gridLayout_16.addWidget(self.id_divisa, 1, 1, 1, 1)

        self.actualizar_divisas = QCheckBox(self.groupBox_14)
        self.actualizar_divisas.setObjectName(u"actualizar_divisas")

        self.gridLayout_16.addWidget(self.actualizar_divisas, 0, 0, 1, 2)

        self.label_42 = QLabel(self.groupBox_14)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)

        self.gridLayout_16.addWidget(self.label_42, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_14, 2, 1, 1, 1)

        self.groupBox_IRPF = QGroupBox(self.tab_12)
        self.groupBox_IRPF.setObjectName(u"groupBox_IRPF")
        self.gridLayout_17 = QGridLayout(self.groupBox_IRPF)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.irpf = QCheckBox(self.groupBox_IRPF)
        self.irpf.setObjectName(u"irpf")
        self.irpf.setMaximumSize(QSize(135, 16777215))

        self.gridLayout_17.addWidget(self.irpf, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_71 = QLabel(self.groupBox_IRPF)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_5.addWidget(self.label_71)

        self.porcentaje_irpf = QDoubleSpinBox(self.groupBox_IRPF)
        self.porcentaje_irpf.setObjectName(u"porcentaje_irpf")
        self.porcentaje_irpf.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.porcentaje_irpf.setMinimum(-999999.000000000000000)
        self.porcentaje_irpf.setMaximum(9999999.000000000000000)

        self.horizontalLayout_5.addWidget(self.porcentaje_irpf)


        self.gridLayout_17.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_IRPF, 3, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_12)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_7 = QGridLayout(self.groupBox_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_222 = QLabel(self.groupBox_12)
        self.label_222.setObjectName(u"label_222")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_222.sizePolicy().hasHeightForWidth())
        self.label_222.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.label_222, 0, 0, 1, 1)

        self.decimales_en_calculos = QSpinBox(self.groupBox_12)
        self.decimales_en_calculos.setObjectName(u"decimales_en_calculos")
        self.decimales_en_calculos.setValue(2)

        self.gridLayout_7.addWidget(self.decimales_en_calculos, 0, 1, 1, 2)

        self.label_85 = QLabel(self.groupBox_12)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_7.addWidget(self.label_85, 1, 0, 1, 1)

        self.decimales_precios = QSpinBox(self.groupBox_12)
        self.decimales_precios.setObjectName(u"decimales_precios")
        self.decimales_precios.setValue(2)

        self.gridLayout_7.addWidget(self.decimales_precios, 1, 1, 1, 2)


        self.gridLayout_21.addWidget(self.groupBox_12, 0, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_12)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_11.addWidget(self.label_25, 0, 0, 1, 1)

        self.digitos_factura = QSpinBox(self.groupBox_3)
        self.digitos_factura.setObjectName(u"digitos_factura")
        self.digitos_factura.setMaximum(45)
        self.digitos_factura.setValue(7)

        self.gridLayout_11.addWidget(self.digitos_factura, 0, 1, 1, 1)

        self.serie_factura = QComboBox(self.groupBox_3)
        self.serie_factura.setObjectName(u"serie_factura")

        self.gridLayout_11.addWidget(self.serie_factura, 1, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_11.addWidget(self.label_26, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_3, 3, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_68 = QLabel(self.tab_12)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_8.addWidget(self.label_68)

        self.dia_cierre_ejercicio = QSpinBox(self.tab_12)
        self.dia_cierre_ejercicio.setObjectName(u"dia_cierre_ejercicio")
        self.dia_cierre_ejercicio.setMinimum(1)
        self.dia_cierre_ejercicio.setMaximum(31)
        self.dia_cierre_ejercicio.setValue(31)

        self.horizontalLayout_8.addWidget(self.dia_cierre_ejercicio)

        self.mes_cierre_ejercicio = QSpinBox(self.tab_12)
        self.mes_cierre_ejercicio.setObjectName(u"mes_cierre_ejercicio")
        self.mes_cierre_ejercicio.setMinimum(1)
        self.mes_cierre_ejercicio.setMaximum(12)
        self.mes_cierre_ejercicio.setValue(12)

        self.horizontalLayout_8.addWidget(self.mes_cierre_ejercicio)


        self.gridLayout_21.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_12)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.enlace_web = QCheckBox(self.groupBox_5)
        self.enlace_web.setObjectName(u"enlace_web")
        self.enlace_web.setGeometry(QRect(0, 50, 307, 22))
        self.gestion_internacional = QCheckBox(self.groupBox_5)
        self.gestion_internacional.setObjectName(u"gestion_internacional")
        self.gestion_internacional.setGeometry(QRect(0, 80, 307, 22))

        self.gridLayout_21.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_12)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_10 = QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.autocodificar_nuevos_articulos = QCheckBox(self.groupBox_2)
        self.autocodificar_nuevos_articulos.setObjectName(u"autocodificar_nuevos_articulos")
        self.autocodificar_nuevos_articulos.setChecked(True)

        self.gridLayout_10.addWidget(self.autocodificar_nuevos_articulos, 0, 0, 1, 1)

        self.tamano_codigo_articulo = QSpinBox(self.groupBox_2)
        self.tamano_codigo_articulo.setObjectName(u"tamano_codigo_articulo")
        self.tamano_codigo_articulo.setMaximumSize(QSize(60, 16777215))
        self.tamano_codigo_articulo.setValue(15)

        self.gridLayout_10.addWidget(self.tamano_codigo_articulo, 1, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_2)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_41, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_12)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.margen_articulos = QDoubleSpinBox(self.groupBox)
        self.margen_articulos.setObjectName(u"margen_articulos")

        self.gridLayout_9.addWidget(self.margen_articulos, 1, 3, 1, 1)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_9.addWidget(self.label_33, 2, 1, 1, 1)

        self.id_tarifa = QComboBox(self.groupBox)
        self.id_tarifa.setObjectName(u"id_tarifa")

        self.gridLayout_9.addWidget(self.id_tarifa, 0, 3, 1, 1)

        self.label_31 = QLabel(self.groupBox)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_9.addWidget(self.label_31, 1, 1, 1, 1)

        self.margen_minimo_articulos = QDoubleSpinBox(self.groupBox)
        self.margen_minimo_articulos.setObjectName(u"margen_minimo_articulos")

        self.gridLayout_9.addWidget(self.margen_minimo_articulos, 2, 3, 1, 1)

        self.label_58 = QLabel(self.groupBox)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_9.addWidget(self.label_58, 0, 1, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox, 0, 1, 2, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnDeleteLogo = QPushButton(self.tab_12)
        self.btnDeleteLogo.setObjectName(u"btnDeleteLogo")

        self.gridLayout.addWidget(self.btnDeleteLogo, 2, 0, 1, 1)

        self.btnAddLogo = QPushButton(self.tab_12)
        self.btnAddLogo.setObjectName(u"btnAddLogo")

        self.gridLayout.addWidget(self.btnAddLogo, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout, 4, 2, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_12)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.imgLogo = QLabel(self.groupBox_6)
        self.imgLogo.setObjectName(u"imgLogo")
        self.imgLogo.setGeometry(QRect(20, 40, 431, 221))
        self.imgLogo.setMaximumSize(QSize(1211, 348))
        self.imgLogo.setPixmap(QPixmap(u":/PNG/resources/icons/png/LogoIcono.png"))
        self.imgLogo.setScaledContents(False)
        self.imgLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.groupBox_6, 1, 2, 3, 1)

        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_5 = QVBoxLayout(self.tab_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_36 = QLabel(self.tab_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_36)

        self.cometarios_albaran = QTextEdit(self.tab_6)
        self.cometarios_albaran.setObjectName(u"cometarios_albaran")

        self.verticalLayout_5.addWidget(self.cometarios_albaran)

        self.label_35 = QLabel(self.tab_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_35)

        self.comentarios_facturas = QTextEdit(self.tab_6)
        self.comentarios_facturas.setObjectName(u"comentarios_facturas")

        self.verticalLayout_5.addWidget(self.comentarios_facturas)

        self.label_5 = QLabel(self.tab_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.comentarios_contrato_servicio = QTextEdit(self.tab_6)
        self.comentarios_contrato_servicio.setObjectName(u"comentarios_contrato_servicio")

        self.verticalLayout_5.addWidget(self.comentarios_contrato_servicio)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_15 = QGridLayout(self.tab_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horarios_sabado = QLineEdit(self.tab_8)
        self.horarios_sabado.setObjectName(u"horarios_sabado")

        self.gridLayout_15.addWidget(self.horarios_sabado, 5, 1, 1, 1)

        self.label_47 = QLabel(self.tab_8)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_15.addWidget(self.label_47, 1, 0, 1, 1)

        self.horarios_jueves = QLineEdit(self.tab_8)
        self.horarios_jueves.setObjectName(u"horarios_jueves")

        self.gridLayout_15.addWidget(self.horarios_jueves, 3, 1, 1, 1)

        self.horarios_lunes = QLineEdit(self.tab_8)
        self.horarios_lunes.setObjectName(u"horarios_lunes")
        self.horarios_lunes.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.horarios_lunes, 0, 1, 1, 1)

        self.label_46 = QLabel(self.tab_8)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_15.addWidget(self.label_46, 0, 0, 1, 1)

        self.label_45 = QLabel(self.tab_8)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_15.addWidget(self.label_45, 4, 0, 1, 1)

        self.label_70 = QLabel(self.tab_8)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_15.addWidget(self.label_70, 6, 0, 1, 1)

        self.label_44 = QLabel(self.tab_8)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_15.addWidget(self.label_44, 3, 0, 1, 1)

        self.horarios_martes = QLineEdit(self.tab_8)
        self.horarios_martes.setObjectName(u"horarios_martes")
        self.horarios_martes.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.horarios_martes, 1, 1, 1, 1)

        self.label_69 = QLabel(self.tab_8)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_15.addWidget(self.label_69, 5, 0, 1, 1)

        self.horarios_miercoles = QLineEdit(self.tab_8)
        self.horarios_miercoles.setObjectName(u"horarios_miercoles")
        self.horarios_miercoles.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.horarios_miercoles, 2, 1, 1, 1)

        self.label_48 = QLabel(self.tab_8)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_15.addWidget(self.label_48, 2, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab_8)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.google_id = QLineEdit(self.groupBox_7)
        self.google_id.setObjectName(u"google_id")
        self.google_id.setGeometry(QRect(190, 40, 341, 32))
        self.google_acces_token = QLineEdit(self.groupBox_7)
        self.google_acces_token.setObjectName(u"google_acces_token")
        self.google_acces_token.setGeometry(QRect(190, 80, 341, 32))
        self.google_refresh_token = QLineEdit(self.groupBox_7)
        self.google_refresh_token.setObjectName(u"google_refresh_token")
        self.google_refresh_token.setGeometry(QRect(190, 120, 341, 32))
        self.googletoken_expires_at = QLineEdit(self.groupBox_7)
        self.googletoken_expires_at.setObjectName(u"googletoken_expires_at")
        self.googletoken_expires_at.setGeometry(QRect(190, 160, 341, 32))
        self.label_72 = QLabel(self.groupBox_7)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(20, 50, 161, 18))
        self.label_73 = QLabel(self.groupBox_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(20, 90, 161, 18))
        self.label_76 = QLabel(self.groupBox_7)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(20, 130, 161, 18))
        self.label_77 = QLabel(self.groupBox_7)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(20, 170, 161, 18))
        self.google_email = QLineEdit(self.groupBox_7)
        self.google_email.setObjectName(u"google_email")
        self.google_email.setGeometry(QRect(730, 40, 291, 32))
        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(560, 50, 161, 18))

        self.gridLayout_15.addWidget(self.groupBox_7, 7, 1, 1, 1)

        self.horarios_domingo = QLineEdit(self.tab_8)
        self.horarios_domingo.setObjectName(u"horarios_domingo")

        self.gridLayout_15.addWidget(self.horarios_domingo, 6, 1, 1, 1)

        self.horarios_viernes = QLineEdit(self.tab_8)
        self.horarios_viernes.setObjectName(u"horarios_viernes")

        self.gridLayout_15.addWidget(self.horarios_viernes, 4, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout = QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.activar_contabilidad = QCheckBox(self.tab_5)
        self.activar_contabilidad.setObjectName(u"activar_contabilidad")
        self.activar_contabilidad.setChecked(True)

        self.verticalLayout.addWidget(self.activar_contabilidad)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cuenta_venta_servicios = QLineEdit(self.tab_5)
        self.cuenta_venta_servicios.setObjectName(u"cuenta_venta_servicios")
        self.cuenta_venta_servicios.setMaximumSize(QSize(200, 16777215))
        self.cuenta_venta_servicios.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.cuenta_venta_servicios, 5, 1, 1, 1)

        self.cuenta_venta_mercaderias = QLineEdit(self.tab_5)
        self.cuenta_venta_mercaderias.setObjectName(u"cuenta_venta_mercaderias")
        self.cuenta_venta_mercaderias.setMaximumSize(QSize(200, 16777215))
        self.cuenta_venta_mercaderias.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.cuenta_venta_mercaderias, 4, 1, 1, 1)

        self.cuenta_acreedores = QLineEdit(self.tab_5)
        self.cuenta_acreedores.setObjectName(u"cuenta_acreedores")
        self.cuenta_acreedores.setMaximumSize(QSize(200, 16777215))
        self.cuenta_acreedores.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.cuenta_acreedores, 3, 1, 1, 1)

        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_37 = QLabel(self.tab_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_37, 5, 0, 1, 1)

        self.label_28 = QLabel(self.tab_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_28, 2, 0, 1, 1)

        self.cuenta_proveedores = QLineEdit(self.tab_5)
        self.cuenta_proveedores.setObjectName(u"cuenta_proveedores")
        self.cuenta_proveedores.setMaximumSize(QSize(200, 16777215))
        self.cuenta_proveedores.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.cuenta_proveedores, 2, 1, 1, 1)

        self.digitos_cuentas = QSpinBox(self.tab_5)
        self.digitos_cuentas.setObjectName(u"digitos_cuentas")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.digitos_cuentas.sizePolicy().hasHeightForWidth())
        self.digitos_cuentas.setSizePolicy(sizePolicy3)
        self.digitos_cuentas.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.digitos_cuentas.setMaximum(20)
        self.digitos_cuentas.setValue(8)

        self.gridLayout_8.addWidget(self.digitos_cuentas, 0, 1, 1, 1)

        self.cuenta_clientes = QLineEdit(self.tab_5)
        self.cuenta_clientes.setObjectName(u"cuenta_clientes")
        self.cuenta_clientes.setMaximumSize(QSize(200, 16777215))
        self.cuenta_clientes.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.cuenta_clientes, 1, 1, 1, 1)

        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_27 = QLabel(self.tab_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_27, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_8)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.cuenta_iva_repercutido_re_n = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_re_n.setObjectName(u"cuenta_iva_repercutido_re_n")
        self.cuenta_iva_repercutido_re_n.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_re_n, 1, 5, 1, 1)

        self.cuenta_iva_repercutido_sr = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_sr.setObjectName(u"cuenta_iva_repercutido_sr")
        self.cuenta_iva_repercutido_sr.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_sr, 3, 4, 1, 1)

        self.label_65 = QLabel(self.tab_5)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_13.addWidget(self.label_65, 4, 3, 1, 1)

        self.cuenta_iva_soportado_e = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_e.setObjectName(u"cuenta_iva_soportado_e")
        self.cuenta_iva_soportado_e.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_e, 4, 1, 1, 1)

        self.label_59 = QLabel(self.tab_5)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_13.addWidget(self.label_59, 2, 0, 1, 1)

        self.cuenta_iva_soportado_r = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_r.setObjectName(u"cuenta_iva_soportado_r")
        self.cuenta_iva_soportado_r.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_r, 2, 1, 1, 1)

        self.label_63 = QLabel(self.tab_5)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_13.addWidget(self.label_63, 2, 3, 1, 1)

        self.label_38 = QLabel(self.tab_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777214, 15))
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_13.addWidget(self.label_38, 0, 1, 1, 1)

        self.cuenta_iva_soportado_re_e = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_re_e.setObjectName(u"cuenta_iva_soportado_re_e")
        self.cuenta_iva_soportado_re_e.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_re_e, 4, 2, 1, 1)

        self.cuenta_iva_soportado_re_sr = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_re_sr.setObjectName(u"cuenta_iva_soportado_re_sr")
        self.cuenta_iva_soportado_re_sr.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_re_sr, 3, 2, 1, 1)

        self.label_39 = QLabel(self.tab_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777214, 15))
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_13.addWidget(self.label_39, 0, 4, 1, 1)

        self.label_40 = QLabel(self.tab_5)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_13.addWidget(self.label_40, 1, 0, 1, 1)

        self.label_62 = QLabel(self.tab_5)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_13.addWidget(self.label_62, 1, 3, 1, 1)

        self.cuenta_iva_soportado_n = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_n.setObjectName(u"cuenta_iva_soportado_n")
        self.cuenta_iva_soportado_n.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_n, 1, 1, 1, 1)

        self.cuenta_iva_repercutido_n = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_n.setObjectName(u"cuenta_iva_repercutido_n")
        self.cuenta_iva_repercutido_n.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_n, 1, 4, 1, 1)

        self.cuenta_iva_repercutido_e = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_e.setObjectName(u"cuenta_iva_repercutido_e")
        self.cuenta_iva_repercutido_e.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_e, 4, 4, 1, 1)

        self.cuenta_iva_repercutido_r = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_r.setObjectName(u"cuenta_iva_repercutido_r")
        self.cuenta_iva_repercutido_r.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_r, 2, 4, 1, 1)

        self.label_60 = QLabel(self.tab_5)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_13.addWidget(self.label_60, 3, 0, 1, 1)

        self.cuenta_iva_soportado_sr = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_sr.setObjectName(u"cuenta_iva_soportado_sr")
        self.cuenta_iva_soportado_sr.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_sr, 3, 1, 1, 1)

        self.label_64 = QLabel(self.tab_5)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_13.addWidget(self.label_64, 3, 3, 1, 1)

        self.label_61 = QLabel(self.tab_5)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_13.addWidget(self.label_61, 4, 0, 1, 1)

        self.cuenta_iva_soportado_re_n = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_re_n.setObjectName(u"cuenta_iva_soportado_re_n")
        self.cuenta_iva_soportado_re_n.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_re_n, 1, 2, 1, 1)

        self.cuenta_iva_soportado_re_r = QLineEdit(self.tab_5)
        self.cuenta_iva_soportado_re_r.setObjectName(u"cuenta_iva_soportado_re_r")
        self.cuenta_iva_soportado_re_r.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_soportado_re_r, 2, 2, 1, 1)

        self.label_66 = QLabel(self.tab_5)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777214, 15))

        self.gridLayout_13.addWidget(self.label_66, 0, 2, 1, 1)

        self.label_67 = QLabel(self.tab_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(16777214, 15))

        self.gridLayout_13.addWidget(self.label_67, 0, 5, 1, 1)

        self.cuenta_iva_repercutido_re_sr = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_re_sr.setObjectName(u"cuenta_iva_repercutido_re_sr")
        self.cuenta_iva_repercutido_re_sr.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_re_sr, 3, 5, 1, 1)

        self.cuenta_iva_repercutido_re_r = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_re_r.setObjectName(u"cuenta_iva_repercutido_re_r")
        self.cuenta_iva_repercutido_re_r.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_re_r, 2, 5, 1, 1)

        self.cuenta_iva_repercutido_re_e = QLineEdit(self.tab_5)
        self.cuenta_iva_repercutido_re_e.setObjectName(u"cuenta_iva_repercutido_re_e")
        self.cuenta_iva_repercutido_re_e.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.cuenta_iva_repercutido_re_e, 4, 5, 1, 1)

        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 5, 1, 1, 1)

        self.cuenta_cobros = QLineEdit(self.tab_5)
        self.cuenta_cobros.setObjectName(u"cuenta_cobros")

        self.gridLayout_13.addWidget(self.cuenta_cobros, 5, 2, 1, 1)

        self.label_10 = QLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 5, 4, 1, 1)

        self.cuenta_pagos = QLineEdit(self.tab_5)
        self.cuenta_pagos.setObjectName(u"cuenta_pagos")

        self.gridLayout_13.addWidget(self.cuenta_pagos, 5, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.gridLayout_24.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.gridLayout_5 = QGridLayout(self.tabWidgetPage2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.tabWidgetPage2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.mysql_frame = QFrame(self.tabWidgetPage2)
        self.mysql_frame.setObjectName(u"mysql_frame")
        self.mysql_frame.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mysql_frame.sizePolicy().hasHeightForWidth())
        self.mysql_frame.setSizePolicy(sizePolicy4)
        self.mysql_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mysql_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.mysql_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout_5.addWidget(self.mysql_frame, 6, 0, 1, 5)

        self.groupBox_8 = QGroupBox(self.tabWidgetPage2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayoutWidget_2 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(100, 40, 373, 201))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.gridLayoutWidget_2)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_19.addWidget(self.label_82, 1, 0, 1, 2)

        self.mariadb_user = QLineEdit(self.gridLayoutWidget_2)
        self.mariadb_user.setObjectName(u"mariadb_user")

        self.gridLayout_19.addWidget(self.mariadb_user, 2, 3, 1, 2)

        self.mariadb_port = QLineEdit(self.gridLayoutWidget_2)
        self.mariadb_port.setObjectName(u"mariadb_port")

        self.gridLayout_19.addWidget(self.mariadb_port, 0, 4, 1, 1)

        self.mariadb_password = QLineEdit(self.gridLayoutWidget_2)
        self.mariadb_password.setObjectName(u"mariadb_password")

        self.gridLayout_19.addWidget(self.mariadb_password, 3, 3, 1, 2)

        self.label_87 = QLabel(self.gridLayoutWidget_2)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_19.addWidget(self.label_87, 2, 0, 1, 2)

        self.mariadb_name = QLineEdit(self.gridLayoutWidget_2)
        self.mariadb_name.setObjectName(u"mariadb_name")

        self.gridLayout_19.addWidget(self.mariadb_name, 1, 3, 1, 2)

        self.label_86 = QLabel(self.gridLayoutWidget_2)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_19.addWidget(self.label_86, 0, 0, 1, 1)

        self.mariadb_host = QLineEdit(self.gridLayoutWidget_2)
        self.mariadb_host.setObjectName(u"mariadb_host")

        self.gridLayout_19.addWidget(self.mariadb_host, 0, 1, 1, 1)

        self.label_84 = QLabel(self.gridLayoutWidget_2)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_19.addWidget(self.label_84, 0, 3, 1, 1)

        self.label_83 = QLabel(self.gridLayoutWidget_2)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_19.addWidget(self.label_83, 3, 0, 1, 2)

        self.btnTestBDMariaDB = QPushButton(self.gridLayoutWidget_2)
        self.btnTestBDMariaDB.setObjectName(u"btnTestBDMariaDB")

        self.gridLayout_19.addWidget(self.btnTestBDMariaDB, 5, 3, 1, 2)

        self.btnCrearDBMariaDb = QPushButton(self.gridLayoutWidget_2)
        self.btnCrearDBMariaDb.setObjectName(u"btnCrearDBMariaDb")

        self.gridLayout_19.addWidget(self.btnCrearDBMariaDb, 5, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_8, 2, 0, 4, 1)

        self.motordb = QComboBox(self.tabWidgetPage2)
        self.motordb.addItem("")
        self.motordb.addItem("")
        self.motordb.addItem("")
        self.motordb.addItem("")
        self.motordb.setObjectName(u"motordb")

        self.gridLayout_5.addWidget(self.motordb, 0, 1, 1, 2)

        self.sqlite_frame = QFrame(self.tabWidgetPage2)
        self.sqlite_frame.setObjectName(u"sqlite_frame")
        self.sqlite_frame.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.sqlite_frame.sizePolicy().hasHeightForWidth())
        self.sqlite_frame.setSizePolicy(sizePolicy4)
        self.sqlite_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sqlite_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.sqlite_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.sqlite_frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)

        self.btnSelecionarBDSQLite = QPushButton(self.sqlite_frame)
        self.btnSelecionarBDSQLite.setObjectName(u"btnSelecionarBDSQLite")
        self.btnSelecionarBDSQLite.setMaximumSize(QSize(35, 35))
        self.btnSelecionarBDSQLite.setIcon(icon2)
        self.btnSelecionarBDSQLite.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.btnSelecionarBDSQLite, 1, 2, 1, 1)

        self.label_3 = QLabel(self.sqlite_frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.archivo_sqlite = QLineEdit(self.sqlite_frame)
        self.archivo_sqlite.setObjectName(u"archivo_sqlite")
        self.archivo_sqlite.setEnabled(False)
        self.archivo_sqlite.setMaximumSize(QSize(16777215, 32))

        self.gridLayout_3.addWidget(self.archivo_sqlite, 1, 1, 1, 1)

        self.btn_migrar = QPushButton(self.sqlite_frame)
        self.btn_migrar.setObjectName(u"btn_migrar")

        self.gridLayout_3.addWidget(self.btn_migrar, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.sqlite_frame, 1, 0, 1, 3)

        self.groupBox_9 = QGroupBox(self.tabWidgetPage2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayoutWidget = QWidget(self.groupBox_9)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(80, 40, 471, 201))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.postgre_host = QLineEdit(self.gridLayoutWidget)
        self.postgre_host.setObjectName(u"postgre_host")

        self.gridLayout_18.addWidget(self.postgre_host, 0, 1, 1, 1)

        self.label_79 = QLabel(self.gridLayoutWidget)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_18.addWidget(self.label_79, 1, 0, 1, 2)

        self.label_78 = QLabel(self.gridLayoutWidget)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_18.addWidget(self.label_78, 0, 3, 1, 1)

        self.label_81 = QLabel(self.gridLayoutWidget)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_18.addWidget(self.label_81, 3, 0, 1, 2)

        self.postgre_password = QLineEdit(self.gridLayoutWidget)
        self.postgre_password.setObjectName(u"postgre_password")

        self.gridLayout_18.addWidget(self.postgre_password, 3, 3, 1, 2)

        self.postgre_port = QLineEdit(self.gridLayoutWidget)
        self.postgre_port.setObjectName(u"postgre_port")

        self.gridLayout_18.addWidget(self.postgre_port, 0, 4, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_18.addWidget(self.label_56, 0, 0, 1, 1)

        self.postgre_name = QLineEdit(self.gridLayoutWidget)
        self.postgre_name.setObjectName(u"postgre_name")

        self.gridLayout_18.addWidget(self.postgre_name, 1, 3, 1, 2)

        self.label_80 = QLabel(self.gridLayoutWidget)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_18.addWidget(self.label_80, 2, 0, 1, 2)

        self.postgre_user = QLineEdit(self.gridLayoutWidget)
        self.postgre_user.setObjectName(u"postgre_user")

        self.gridLayout_18.addWidget(self.postgre_user, 2, 3, 1, 2)

        self.btnCrearDBPostgreSQL = QPushButton(self.gridLayoutWidget)
        self.btnCrearDBPostgreSQL.setObjectName(u"btnCrearDBPostgreSQL")

        self.gridLayout_18.addWidget(self.btnCrearDBPostgreSQL, 4, 0, 1, 2)

        self.btnTestDBPostgreSQL = QPushButton(self.gridLayoutWidget)
        self.btnTestDBPostgreSQL.setObjectName(u"btnTestDBPostgreSQL")

        self.gridLayout_18.addWidget(self.btnTestDBPostgreSQL, 4, 3, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_9, 2, 1, 4, 4)

        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.gridLayout_14.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.create_page_empresa)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.tableView = QTableView(self.page)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(5, 11, 1261, 681))
        self.stackedWidget.addWidget(self.page)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.label = QLabel(FrmEmpresas)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        QWidget.setTabOrder(self.codigoempresa, self.nombre_comercial)
        QWidget.setTabOrder(self.nombre_comercial, self.forma_juridica)
        QWidget.setTabOrder(self.forma_juridica, self.nombre_fiscal)
        QWidget.setTabOrder(self.nombre_fiscal, self.non_tva)
        QWidget.setTabOrder(self.non_tva, self.pais)
        QWidget.setTabOrder(self.pais, self.btnBuscarPais)
        QWidget.setTabOrder(self.btnBuscarPais, self.direccion)
        QWidget.setTabOrder(self.direccion, self.cp)
        QWidget.setTabOrder(self.cp, self.poblacion)
        QWidget.setTabOrder(self.poblacion, self.provincia)
        QWidget.setTabOrder(self.provincia, self.cif_siren)
        QWidget.setTabOrder(self.cif_siren, self.siret)
        QWidget.setTabOrder(self.siret, self.ape_naf)
        QWidget.setTabOrder(self.ape_naf, self.rcs)
        QWidget.setTabOrder(self.rcs, self.ciudad_rcs)
        QWidget.setTabOrder(self.ciudad_rcs, self.registro_mercantil)
        QWidget.setTabOrder(self.registro_mercantil, self.inscripcion)
        QWidget.setTabOrder(self.inscripcion, self.telefono1)
        QWidget.setTabOrder(self.telefono1, self.telefono2)
        QWidget.setTabOrder(self.telefono2, self.movil)
        QWidget.setTabOrder(self.movil, self.email)
        QWidget.setTabOrder(self.email, self.web)
        QWidget.setTabOrder(self.web, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.enlace_web)
        QWidget.setTabOrder(self.enlace_web, self.gestion_internacional)
        QWidget.setTabOrder(self.gestion_internacional, self.dia_cierre_ejercicio)
        QWidget.setTabOrder(self.dia_cierre_ejercicio, self.mes_cierre_ejercicio)
        QWidget.setTabOrder(self.mes_cierre_ejercicio, self.autocodificar_nuevos_articulos)
        QWidget.setTabOrder(self.autocodificar_nuevos_articulos, self.tamano_codigo_articulo)
        QWidget.setTabOrder(self.tamano_codigo_articulo, self.irpf)
        QWidget.setTabOrder(self.irpf, self.porcentaje_irpf)
        QWidget.setTabOrder(self.porcentaje_irpf, self.id_tarifa)
        QWidget.setTabOrder(self.id_tarifa, self.margen_articulos)
        QWidget.setTabOrder(self.margen_articulos, self.margen_minimo_articulos)
        QWidget.setTabOrder(self.margen_minimo_articulos, self.actualizar_divisas)
        QWidget.setTabOrder(self.actualizar_divisas, self.id_divisa)
        QWidget.setTabOrder(self.id_divisa, self.digitos_factura)
        QWidget.setTabOrder(self.digitos_factura, self.serie_factura)
        QWidget.setTabOrder(self.serie_factura, self.decimales_en_calculos)
        QWidget.setTabOrder(self.decimales_en_calculos, self.decimales_precios)
        QWidget.setTabOrder(self.decimales_precios, self.btnAddLogo)
        QWidget.setTabOrder(self.btnAddLogo, self.btnDeleteLogo)
        QWidget.setTabOrder(self.btnDeleteLogo, self.cometarios_albaran)
        QWidget.setTabOrder(self.cometarios_albaran, self.comentarios_facturas)
        QWidget.setTabOrder(self.comentarios_facturas, self.comentarios_contrato_servicio)
        QWidget.setTabOrder(self.comentarios_contrato_servicio, self.horarios_lunes)
        QWidget.setTabOrder(self.horarios_lunes, self.horarios_martes)
        QWidget.setTabOrder(self.horarios_martes, self.horarios_miercoles)
        QWidget.setTabOrder(self.horarios_miercoles, self.horarios_jueves)
        QWidget.setTabOrder(self.horarios_jueves, self.horarios_viernes)
        QWidget.setTabOrder(self.horarios_viernes, self.horarios_sabado)
        QWidget.setTabOrder(self.horarios_sabado, self.horarios_domingo)
        QWidget.setTabOrder(self.horarios_domingo, self.google_id)
        QWidget.setTabOrder(self.google_id, self.google_acces_token)
        QWidget.setTabOrder(self.google_acces_token, self.google_refresh_token)
        QWidget.setTabOrder(self.google_refresh_token, self.googletoken_expires_at)
        QWidget.setTabOrder(self.googletoken_expires_at, self.google_email)
        QWidget.setTabOrder(self.google_email, self.activar_contabilidad)
        QWidget.setTabOrder(self.activar_contabilidad, self.digitos_cuentas)
        QWidget.setTabOrder(self.digitos_cuentas, self.cuenta_clientes)
        QWidget.setTabOrder(self.cuenta_clientes, self.cuenta_proveedores)
        QWidget.setTabOrder(self.cuenta_proveedores, self.cuenta_acreedores)
        QWidget.setTabOrder(self.cuenta_acreedores, self.cuenta_venta_mercaderias)
        QWidget.setTabOrder(self.cuenta_venta_mercaderias, self.cuenta_venta_servicios)
        QWidget.setTabOrder(self.cuenta_venta_servicios, self.cuenta_iva_soportado_n)
        QWidget.setTabOrder(self.cuenta_iva_soportado_n, self.cuenta_iva_soportado_r)
        QWidget.setTabOrder(self.cuenta_iva_soportado_r, self.cuenta_iva_soportado_sr)
        QWidget.setTabOrder(self.cuenta_iva_soportado_sr, self.cuenta_iva_soportado_e)
        QWidget.setTabOrder(self.cuenta_iva_soportado_e, self.cuenta_iva_soportado_re_n)
        QWidget.setTabOrder(self.cuenta_iva_soportado_re_n, self.cuenta_iva_soportado_re_r)
        QWidget.setTabOrder(self.cuenta_iva_soportado_re_r, self.cuenta_iva_soportado_re_sr)
        QWidget.setTabOrder(self.cuenta_iva_soportado_re_sr, self.cuenta_iva_soportado_re_e)
        QWidget.setTabOrder(self.cuenta_iva_soportado_re_e, self.cuenta_iva_repercutido_n)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_n, self.cuenta_iva_repercutido_r)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_r, self.cuenta_iva_repercutido_sr)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_sr, self.cuenta_iva_repercutido_e)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_e, self.cuenta_iva_repercutido_re_n)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_re_n, self.cuenta_iva_repercutido_re_r)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_re_r, self.cuenta_iva_repercutido_re_sr)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_re_sr, self.cuenta_iva_repercutido_re_e)
        QWidget.setTabOrder(self.cuenta_iva_repercutido_re_e, self.cuenta_cobros)
        QWidget.setTabOrder(self.cuenta_cobros, self.cuenta_pagos)
        QWidget.setTabOrder(self.cuenta_pagos, self.motordb)
        QWidget.setTabOrder(self.motordb, self.archivo_sqlite)
        QWidget.setTabOrder(self.archivo_sqlite, self.btnSelecionarBDSQLite)
        QWidget.setTabOrder(self.btnSelecionarBDSQLite, self.btn_migrar)
        QWidget.setTabOrder(self.btn_migrar, self.mariadb_host)
        QWidget.setTabOrder(self.mariadb_host, self.mariadb_port)
        QWidget.setTabOrder(self.mariadb_port, self.mariadb_name)
        QWidget.setTabOrder(self.mariadb_name, self.mariadb_user)
        QWidget.setTabOrder(self.mariadb_user, self.mariadb_password)
        QWidget.setTabOrder(self.mariadb_password, self.btnCrearDBMariaDb)
        QWidget.setTabOrder(self.btnCrearDBMariaDb, self.btnTestBDMariaDB)
        QWidget.setTabOrder(self.btnTestBDMariaDB, self.postgre_host)
        QWidget.setTabOrder(self.postgre_host, self.postgre_port)
        QWidget.setTabOrder(self.postgre_port, self.postgre_name)
        QWidget.setTabOrder(self.postgre_name, self.postgre_user)
        QWidget.setTabOrder(self.postgre_user, self.postgre_password)
        QWidget.setTabOrder(self.postgre_password, self.btnCrearDBPostgreSQL)
        QWidget.setTabOrder(self.btnCrearDBPostgreSQL, self.btnTestDBPostgreSQL)
        QWidget.setTabOrder(self.btnTestDBPostgreSQL, self.tableView)
        QWidget.setTabOrder(self.tableView, self.btn_salir)
        QWidget.setTabOrder(self.btn_salir, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.btn_guardar_nuevo)
        QWidget.setTabOrder(self.btn_guardar_nuevo, self.btn_deshacer)

        self.retranslateUi(FrmEmpresas)
        try:
            self.btn_salir.clicked.connect(FrmEmpresas.accept)
        except Exception:
            try:
                self.btn_salir.clicked.connect(FrmEmpresas.close)
            except Exception:
                pass

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FrmEmpresas)
    # setupUi

    def retranslateUi(self, FrmEmpresas):
        FrmEmpresas.setWindowTitle(QCoreApplication.translate("FrmEmpresas", u"Gesti\u00f3n de empresas", None))
        self.btn_guardar_nuevo.setText(QCoreApplication.translate("FrmEmpresas", u"Guardar cambios", None))
        self.btn_deshacer.setText(QCoreApplication.translate("FrmEmpresas", u"Deshacer cambios", None))
        self.btn_salir.setText(QCoreApplication.translate("FrmEmpresas", u"Salir", None))
        self.label_n_rm.setText(QCoreApplication.translate("FrmEmpresas", u"N\u00ba RM:", None))
        self.label_74.setText(QCoreApplication.translate("FrmEmpresas", u"Codigo:", None))
        self.label_cif_siren.setText(QCoreApplication.translate("FrmEmpresas", u"Cif:", None))
        self.label_21.setText(QCoreApplication.translate("FrmEmpresas", u"Web:", None))
        self.label_20.setText(QCoreApplication.translate("FrmEmpresas", u"Mail:", None))
        self.forma_juridica.setItemText(0, QCoreApplication.translate("FrmEmpresas", u"EI (Entreprise Individuelle)", None))
        self.forma_juridica.setItemText(1, QCoreApplication.translate("FrmEmpresas", u"EIRL", None))
        self.forma_juridica.setItemText(2, QCoreApplication.translate("FrmEmpresas", u"Micro-entrepreneur", None))
        self.forma_juridica.setItemText(3, QCoreApplication.translate("FrmEmpresas", u"SARL", None))
        self.forma_juridica.setItemText(4, QCoreApplication.translate("FrmEmpresas", u"EURL", None))
        self.forma_juridica.setItemText(5, QCoreApplication.translate("FrmEmpresas", u"SAS", None))
        self.forma_juridica.setItemText(6, QCoreApplication.translate("FrmEmpresas", u"SASU", None))
        self.forma_juridica.setItemText(7, QCoreApplication.translate("FrmEmpresas", u"SA", None))
        self.forma_juridica.setItemText(8, QCoreApplication.translate("FrmEmpresas", u"SCOP / SCIC", None))
        self.forma_juridica.setItemText(9, QCoreApplication.translate("FrmEmpresas", u"SEM", None))
        self.forma_juridica.setItemText(10, QCoreApplication.translate("FrmEmpresas", u"RM", None))

        self.label_50.setText(QCoreApplication.translate("FrmEmpresas", u"Poblaci\u00f3n:", None))
        self.label_18.setText(QCoreApplication.translate("FrmEmpresas", u"Telefono 2:", None))
        self.label_N_RCS.setText(QCoreApplication.translate("FrmEmpresas", u"N\u00ba RCS:", None))
        self.label_19.setText(QCoreApplication.translate("FrmEmpresas", u"Movil:", None))
        self.label_16.setText(QCoreApplication.translate("FrmEmpresas", u"Pais:", None))
        self.label_17.setText(QCoreApplication.translate("FrmEmpresas", u"Tel\u00e9fono 1:", None))
        self.label_13.setText(QCoreApplication.translate("FrmEmpresas", u"Direcci\u00f3n:", None))
        self.label_siret.setText(QCoreApplication.translate("FrmEmpresas", u"SIRET:", None))
        self.label_APE_NAF.setText(QCoreApplication.translate("FrmEmpresas", u"APE/NAF:", None))
        self.label_23.setText(QCoreApplication.translate("FrmEmpresas", u"Inscripci\u00f3n:", None))
        self.label_forma_juridica.setText(QCoreApplication.translate("FrmEmpresas", u"Forma juridica:", None))
        self.telefono2.setText("")
        self.label_ciudad_rcs.setText(QCoreApplication.translate("FrmEmpresas", u"Ciudad RCS:", None))
        self.label_14.setText(QCoreApplication.translate("FrmEmpresas", u"C.P.:", None))
        self.telefono1.setText("")
        self.btnBuscarPais.setText("")
        self.label_43.setText(QCoreApplication.translate("FrmEmpresas", u"Nombre comercial:", None))
        self.label_75.setText(QCoreApplication.translate("FrmEmpresas", u"Nombre Fiscal:", None))
        self.non_tva.setText(QCoreApplication.translate("FrmEmpresas", u"TVA non applicable", None))
        self.label_provincia.setText(QCoreApplication.translate("FrmEmpresas", u"Provincia:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("FrmEmpresas", u"Datos Fiscales y de Gesti\u00f3n", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("FrmEmpresas", u"Divisas", None))
        self.actualizar_divisas.setText(QCoreApplication.translate("FrmEmpresas", u"Actualizar divisas al entrar", None))
        self.label_42.setText(QCoreApplication.translate("FrmEmpresas", u"Divisa: ", None))
        self.groupBox_IRPF.setTitle(QCoreApplication.translate("FrmEmpresas", u"IRPF", None))
        self.irpf.setText(QCoreApplication.translate("FrmEmpresas", u"Autonomo / IRPF", None))
        self.label_71.setText(QCoreApplication.translate("FrmEmpresas", u"%IRPF:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("FrmEmpresas", u"Decimales", None))
        self.label_222.setText(QCoreApplication.translate("FrmEmpresas", u"Decimales en totales", None))
        self.label_85.setText(QCoreApplication.translate("FrmEmpresas", u"Decimales precios:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("FrmEmpresas", u"Facturas", None))
        self.label_25.setText(QCoreApplication.translate("FrmEmpresas", u"Digitos Factura:", None))
        self.label_26.setText(QCoreApplication.translate("FrmEmpresas", u"Serie Factura:", None))
        self.label_68.setText(QCoreApplication.translate("FrmEmpresas", u"Cierre ejercicio fiscal:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("FrmEmpresas", u"Varios", None))
        self.enlace_web.setText(QCoreApplication.translate("FrmEmpresas", u"Enlace Web.", None))
        self.gestion_internacional.setText(QCoreApplication.translate("FrmEmpresas", u"Gesti\u00f3n Internacional", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FrmEmpresas", u"Articulos", None))
        self.autocodificar_nuevos_articulos.setText(QCoreApplication.translate("FrmEmpresas", u"Auto codificar los nuevos art\u00edculos", None))
        self.label_41.setText(QCoreApplication.translate("FrmEmpresas", u"Tama\u00f1o del c\u00f3digo en caracteres:", None))
        self.groupBox.setTitle(QCoreApplication.translate("FrmEmpresas", u"Tarifas", None))
        self.label_33.setText(QCoreApplication.translate("FrmEmpresas", u"Margen M\u00ednimo:", None))
        self.label_31.setText(QCoreApplication.translate("FrmEmpresas", u"Margen:", None))
        self.label_58.setText(QCoreApplication.translate("FrmEmpresas", u"Tarifa predeterminada:", None))
        self.btnDeleteLogo.setText(QCoreApplication.translate("FrmEmpresas", u"Borrar", None))
        self.btnAddLogo.setText(QCoreApplication.translate("FrmEmpresas", u"Cambiar", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("FrmEmpresas", u"Logotipo", None))
        self.imgLogo.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("FrmEmpresas", u"Otros", None))
        self.label_36.setText(QCoreApplication.translate("FrmEmpresas", u"Comentarios en Albaranes", None))
        self.label_35.setText(QCoreApplication.translate("FrmEmpresas", u"Comentarios en Facturas:", None))
        self.label_5.setText(QCoreApplication.translate("FrmEmpresas", u"Comentarios para el contrato de servicios", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("FrmEmpresas", u"Comentarios", None))
        self.label_47.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Martes:", None))
        self.label_46.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Lunes:", None))
        self.label_45.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Viernes:", None))
        self.label_70.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Domingo:", None))
        self.label_44.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Jueves:", None))
        self.label_69.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Sabado:", None))
        self.label_48.setText(QCoreApplication.translate("FrmEmpresas", u"Horario Miercoles:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("FrmEmpresas", u"Acceso a Google Calendar", None))
        self.label_72.setText(QCoreApplication.translate("FrmEmpresas", u"Google Calendar ID:", None))
        self.label_73.setText(QCoreApplication.translate("FrmEmpresas", u"oauth Acces Token:", None))
        self.label_76.setText(QCoreApplication.translate("FrmEmpresas", u"oauth Refresh Token:", None))
        self.label_77.setText(QCoreApplication.translate("FrmEmpresas", u" Token Expirity:", None))
        self.label_6.setText(QCoreApplication.translate("FrmEmpresas", u"Google email:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("FrmEmpresas", u"Agenda", None))
        self.activar_contabilidad.setText(QCoreApplication.translate("FrmEmpresas", u"Activar contabilidad", None))
        self.cuenta_venta_servicios.setText(QCoreApplication.translate("FrmEmpresas", u"610", None))
        self.cuenta_venta_servicios.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_venta_mercaderias.setText(QCoreApplication.translate("FrmEmpresas", u"600", None))
        self.cuenta_venta_mercaderias.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_acreedores.setText(QCoreApplication.translate("FrmEmpresas", u"410", None))
        self.cuenta_acreedores.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_29.setText(QCoreApplication.translate("FrmEmpresas", u"Acreedores:", None))
        self.label_12.setText(QCoreApplication.translate("FrmEmpresas", u"Cuenta de venta de mercader\u00edas:", None))
        self.label_37.setText(QCoreApplication.translate("FrmEmpresas", u"Cuenta de venta (prestaci\u00f3n de servicios):", None))
        self.label_28.setText(QCoreApplication.translate("FrmEmpresas", u"Proveedores:", None))
        self.cuenta_proveedores.setText(QCoreApplication.translate("FrmEmpresas", u"400", None))
        self.cuenta_proveedores.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_clientes.setText(QCoreApplication.translate("FrmEmpresas", u"430", None))
        self.cuenta_clientes.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_30.setText(QCoreApplication.translate("FrmEmpresas", u"Digitos cuentas contables:", None))
        self.label_27.setText(QCoreApplication.translate("FrmEmpresas", u"Cientes:", None))
        self.cuenta_iva_repercutido_re_n.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_repercutido_sr.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_65.setText(QCoreApplication.translate("FrmEmpresas", u"E", None))
        self.cuenta_iva_soportado_e.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_59.setText(QCoreApplication.translate("FrmEmpresas", u"R", None))
        self.cuenta_iva_soportado_r.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_63.setText(QCoreApplication.translate("FrmEmpresas", u"R", None))
        self.label_38.setText(QCoreApplication.translate("FrmEmpresas", u"Cuenta IVA soportado", None))
        self.cuenta_iva_soportado_re_e.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_soportado_re_sr.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_39.setText(QCoreApplication.translate("FrmEmpresas", u"Cuenta IVA repercutido", None))
        self.label_40.setText(QCoreApplication.translate("FrmEmpresas", u"N", None))
        self.label_62.setText(QCoreApplication.translate("FrmEmpresas", u"N", None))
        self.cuenta_iva_soportado_n.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_repercutido_n.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_repercutido_e.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_repercutido_r.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_60.setText(QCoreApplication.translate("FrmEmpresas", u"SR", None))
        self.cuenta_iva_soportado_sr.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_64.setText(QCoreApplication.translate("FrmEmpresas", u"SR", None))
        self.label_61.setText(QCoreApplication.translate("FrmEmpresas", u"E", None))
        self.cuenta_iva_soportado_re_n.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_soportado_re_r.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_66.setText(QCoreApplication.translate("FrmEmpresas", u"IVA soportado RE", None))
        self.label_67.setText(QCoreApplication.translate("FrmEmpresas", u"IVA repercutido RE", None))
        self.cuenta_iva_repercutido_re_sr.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_repercutido_re_r.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.cuenta_iva_repercutido_re_e.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_9.setText(QCoreApplication.translate("FrmEmpresas", u"Cuenta cobros:", None))
        self.cuenta_cobros.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.label_10.setText(QCoreApplication.translate("FrmEmpresas", u"Cuenta Pagos:", None))
        self.cuenta_pagos.setPlaceholderText(QCoreApplication.translate("FrmEmpresas", u"(F1 - lista)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("FrmEmpresas", u"Contabilidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("FrmEmpresas", u"Otros datos", None))
        self.label_2.setText(QCoreApplication.translate("FrmEmpresas", u"Motor Activo de Base de Datos", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("FrmEmpresas", u"Datos Acceso MariaDB / MySQL ( Recomendado para empresas entre 2 y 10 ordenadores)", None))
        self.label_82.setText(QCoreApplication.translate("FrmEmpresas", u"Nombre Base de Datos:", None))
        self.label_87.setText(QCoreApplication.translate("FrmEmpresas", u"Usuario:", None))
        self.label_86.setText(QCoreApplication.translate("FrmEmpresas", u"Host:", None))
        self.label_84.setText(QCoreApplication.translate("FrmEmpresas", u"Puerto:", None))
        self.label_83.setText(QCoreApplication.translate("FrmEmpresas", u"Password:", None))
        self.btnTestBDMariaDB.setText(QCoreApplication.translate("FrmEmpresas", u"Test Database conexion", None))
        self.btnCrearDBMariaDb.setText(QCoreApplication.translate("FrmEmpresas", u"Crear DB", None))
        self.motordb.setItemText(0, QCoreApplication.translate("FrmEmpresas", u"SQLite", None))
        self.motordb.setItemText(1, QCoreApplication.translate("FrmEmpresas", u"MariaDB", None))
        self.motordb.setItemText(2, QCoreApplication.translate("FrmEmpresas", u"PostgreSQL", None))
        self.motordb.setItemText(3, QCoreApplication.translate("FrmEmpresas", u"MySQL", None))

        self.label_4.setText(QCoreApplication.translate("FrmEmpresas", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Acceso a SQLite (Para empresas con un solo ordenador)</span></p><p><span style=\" font-weight:700; color:#ffffff;\"><br/></span></p></body></html>", None))
        self.btnSelecionarBDSQLite.setText("")
        self.label_3.setText(QCoreApplication.translate("FrmEmpresas", u"Ruta SQLite Empresa", None))
        self.btn_migrar.setText(QCoreApplication.translate("FrmEmpresas", u"Migrar a BD Multipuesto", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("FrmEmpresas", u"Datos Acceso Postgre SQL(Recomendado para empresas con m\u00e1s de 10 ordenadores)", None))
        self.label_79.setText(QCoreApplication.translate("FrmEmpresas", u"Nombre Base de Datos:", None))
        self.label_78.setText(QCoreApplication.translate("FrmEmpresas", u"Puerto:", None))
        self.label_81.setText(QCoreApplication.translate("FrmEmpresas", u"Password:", None))
        self.label_56.setText(QCoreApplication.translate("FrmEmpresas", u"Host:", None))
        self.label_80.setText(QCoreApplication.translate("FrmEmpresas", u"Usuario:", None))
        self.btnCrearDBPostgreSQL.setText(QCoreApplication.translate("FrmEmpresas", u"Crear BD", None))
        self.btnTestDBPostgreSQL.setText(QCoreApplication.translate("FrmEmpresas", u"Test Database conexion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("FrmEmpresas", u"Datos conexi\u00f3n Base de datos", None))
        self.label.setText(QCoreApplication.translate("FrmEmpresas", u"Gesti\u00f3n de Empresas", None))
    # retranslateUi

