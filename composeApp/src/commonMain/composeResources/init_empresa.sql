-- init_empresa.sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    activo SMALLINT DEFAULT 1,
    -- Configuración de Correo (SMTP)
      cuenta_smtp VARCHAR(100) DEFAULT NULL,
      usuario_mail VARCHAR(100) DEFAULT NULL,
      password_mail VARCHAR(100) DEFAULT NULL,
      puerto_email INTEGER DEFAULT NULL,

      -- Permisos de Nivel Superior
      super_user TINYINT DEFAULT 0, -- 1 para admin, 0 para usuario estándar
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS alb_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  albaran VARCHAR(30) DEFAULT NULL,
  fecha DATE DEFAULT NULL,
  id_proveedor INTEGER DEFAULT 0,
  proveedor VARCHAR(100) DEFAULT NULL,
  cif_proveedor VARCHAR(20) DEFAULT NULL,

  -- Bases e Impuestos (Usamos Decimal para precisión contable)
  total1 DECIMAL(15,4) DEFAULT 0,
  total2 DECIMAL(15,4) DEFAULT 0,
  total3 DECIMAL(15,4) DEFAULT 0,
  total4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0,
  porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0,
  porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0,
  iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0,
  iva4 DECIMAL(15,4) DEFAULT 0,
  base1 DECIMAL(15,4) DEFAULT 0,
  base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0,
  base4 DECIMAL(15,4) DEFAULT 0,

  factura VARCHAR(30) DEFAULT NULL,
  base_total DECIMAL(15,4) DEFAULT 0,
  iva_total DECIMAL(15,4) DEFAULT 0,
  total DECIMAL(15,4) DEFAULT 0,
  comentario TEXT,
  pedido INTEGER DEFAULT 0,

  -- Recargos y Totales
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0,
  porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0,
  porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0,
  rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0,
  rec4 DECIMAL(15,4) DEFAULT 0,
  total_recargo DECIMAL(15,4) DEFAULT 0,

  ejercicio INTEGER DEFAULT NULL,
  subtotal DECIMAL(15,4) DEFAULT 0,

  -- Datos de contacto y dirección (Universales)
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL, -- Nombre universal para evitar confusión ES/FR
  id_pais INTEGER DEFAULT NULL,

  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  telefono VARCHAR(20) DEFAULT NULL,
  fax VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(45) DEFAULT NULL,
  codigo_proveedor VARCHAR(20) DEFAULT NULL,
  id_forma_pago INTEGER DEFAULT 0,
  impreso SMALLINT DEFAULT 0,

  -- Gastos de envío
  desc_envio1 VARCHAR(100) DEFAULT NULL,
  desc_envio2 VARCHAR(100) DEFAULT NULL,
  desc_envio3 VARCHAR(100) DEFAULT NULL,
  imp_envio1 DECIMAL(15,4) DEFAULT 0,
  imp_envio2 DECIMAL(15,4) DEFAULT 0,
  imp_envio3 DECIMAL(15,4) DEFAULT 0,
  porc_iva_envio1 DECIMAL(5,2) DEFAULT 0,
  porc_iva_envio2 DECIMAL(5,2) DEFAULT 0,
  porc_iva_envio3 DECIMAL(5,2) DEFAULT 0,
  iva_envio1 DECIMAL(15,4) DEFAULT 0,
  iva_envio2 DECIMAL(15,4) DEFAULT 0,
  iva_envio3 DECIMAL(15,4) DEFAULT 0,

  envio_to_coste SMALLINT DEFAULT 0,
  editable SMALLINT DEFAULT 1,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS articulos_excepciones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  descripcion VARCHAR(100) DEFAULT NULL,

  -- Relaciones (IDs)
  id_articulo INTEGER DEFAULT NULL,
  id_familia INTEGER DEFAULT NULL,
  id_cliente INTEGER DEFAULT NULL,
  id_familia_cliente INTEGER DEFAULT NULL,
  id_subfamilia_cliente INTEGER DEFAULT NULL,
  id_proveedor INTEGER DEFAULT NULL,
  id_agente INTEGER DEFAULT NULL,

  -- Cálculos y Precios (Cambiado double por DECIMAL para precisión)
  importe_porc_aumento DECIMAL(15,4) DEFAULT 0,
  importe_moneda_aumento DECIMAL(15,4) DEFAULT 0,
  importe_fijo DECIMAL(15,4) DEFAULT 0,
  dto_aumento_fijo DECIMAL(15,4) DEFAULT 0,
  dto_aumento_porc DECIMAL(15,4) DEFAULT 0,
  dto_fijo DECIMAL(15,4) DEFAULT 0,

  -- Fechas y Avisos
  fecha_inicio DATE DEFAULT NULL,
  fecha_final DATE DEFAULT NULL,
  id_aviso_ini INTEGER DEFAULT NULL,
  id_aviso_fin INTEGER DEFAULT NULL,

  -- Trazabilidad Estándar
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS articulos_ofertas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_articulo INTEGER DEFAULT NULL,
  id_tarifa INTEGER DEFAULT 0,
  descripcion VARCHAR(100) NOT NULL,

  -- Flags de tipo de oferta (Convertidos a SMALLINT para compatibilidad universal)
  oferta_32 SMALLINT DEFAULT 0,
  oferta_dto SMALLINT DEFAULT 0,
  oferta_precio_final SMALLINT DEFAULT 0,
  oferta_web SMALLINT DEFAULT 0,

  -- Cantidades y Descuentos (DECIMAL para evitar errores de redondeo en cálculos)
  unidades DECIMAL(12,3) DEFAULT 0,
  regalo DECIMAL(12,3) DEFAULT 0,
  dto_local DECIMAL(5,2) DEFAULT 0,
  dto_web DECIMAL(5,2) DEFAULT 0,
  precio_final DECIMAL(15,4) DEFAULT 0,

  comentarios TEXT,
  fecha_inicio DATE DEFAULT NULL,
  fecha_fin DATE DEFAULT NULL,
  activa SMALLINT DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cab_alb (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  serie VARCHAR(5) DEFAULT NULL,
  albaran VARCHAR(45) DEFAULT '0',
  id_divisa INTEGER DEFAULT NULL,
  fecha DATE DEFAULT NULL,
  hora TIME DEFAULT '00:00:00',
  pedido_cliente VARCHAR(100) DEFAULT NULL,

  -- Datos del Cliente
  id_cliente INTEGER DEFAULT 0,
  codigo_cliente VARCHAR(20) DEFAULT NULL,
  cliente VARCHAR(100) DEFAULT NULL,
  cif_nif_siret VARCHAR(30) DEFAULT NULL, -- Nombre genérico para ID Fiscal

  -- Dirección Fiscal
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(45) DEFAULT NULL, -- 'Provincia' en ES, 'Departamento' o vacío en FR
  cp VARCHAR(15) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,

  -- Dirección de Entrega
  direccion1_entrega VARCHAR(100) DEFAULT NULL,
  direccion2_entrega VARCHAR(100) DEFAULT NULL,
  poblacion_entrega VARCHAR(100) DEFAULT NULL,
  provincia_entrega VARCHAR(45) DEFAULT NULL,
  cp_entrega VARCHAR(15) DEFAULT NULL,
  id_pais_entrega INTEGER DEFAULT NULL,
  email_entrega VARCHAR(150) DEFAULT NULL,
  comentarios_entrega TEXT,

  -- Contacto
  telefono VARCHAR(25) DEFAULT NULL,
  fax VARCHAR(25) DEFAULT NULL,
  movil VARCHAR(25) DEFAULT NULL,
  email VARCHAR(100) DEFAULT NULL,

  -- Totales y Descuentos (DECIMAL para precisión)
  subtotal DECIMAL(15,4) DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_dto_pp DECIMAL(5,2) DEFAULT 0,
  dto_pp DECIMAL(15,4) DEFAULT 0,

  -- Desglose de Impuestos (Hasta 4 tipos de IVA)
  base1 DECIMAL(15,4) DEFAULT 0,
  base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0,
  base4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0,
  porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0,
  porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0,
  iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0,
  iva4 DECIMAL(15,4) DEFAULT 0,

  -- Recargo de Equivalencia (Solo usado en ES, valor 0 en FR)
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0,
  porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0,
  porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0,
  rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0,
  rec4 DECIMAL(15,4) DEFAULT 0,

  -- IRPF (Solo usado en ES, valor 0 en FR)
  porc_irpf DECIMAL(5,2) DEFAULT 0,
  irpf DECIMAL(15,4) DEFAULT 0,

  -- Totales Albarán
  total1 DECIMAL(15,4) DEFAULT 0,
  total2 DECIMAL(15,4) DEFAULT 0,
  total3 DECIMAL(15,4) DEFAULT 0,
  total4 DECIMAL(15,4) DEFAULT 0,
  base_total DECIMAL(15,4) DEFAULT 0,
  iva_total DECIMAL(15,4) DEFAULT 0,
  rec_total DECIMAL(15,4) DEFAULT 0,
  total_albaran DECIMAL(15,4) DEFAULT 0,
  entregado_a_cuenta DECIMAL(15,4) DEFAULT 0,

  -- Gastos de Envío
  desc_gastos_envio1 VARCHAR(45) DEFAULT NULL,
  desc_gastos_envio2 VARCHAR(45) DEFAULT NULL,
  desc_gastos_envio3 VARCHAR(45) DEFAULT NULL,
  imp_gastos_envio1 DECIMAL(15,4) DEFAULT 0,
  imp_gastos_envio2 DECIMAL(15,4) DEFAULT 0,
  imp_gastos_envio3 DECIMAL(15,4) DEFAULT 0,
  porc_iva_gastos_envio1 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gastos_envio2 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gastos_envio3 DECIMAL(5,2) DEFAULT 0,
  iva_gastos_envio1 DECIMAL(15,4) DEFAULT 0,
  iva_gastos_envio2 DECIMAL(15,4) DEFAULT 0,
  iva_gastos_envio3 DECIMAL(15,4) DEFAULT 0,

  -- Estado y Relaciones
  impreso SMALLINT DEFAULT 0,
  facturado SMALLINT DEFAULT 0,
  factura VARCHAR(45) DEFAULT NULL,
  fecha_factura DATE DEFAULT NULL,
  id_forma_pago INTEGER DEFAULT 0,
  id_transportista INTEGER DEFAULT 0,
  id_agente INTEGER DEFAULT 0,
  id_usuario INTEGER DEFAULT 0,
  id_caja INTEGER DEFAULT 0,
  ejercicio INTEGER DEFAULT NULL,
  editable SMALLINT DEFAULT 1,
  es_simplificada SMALLINT DEFAULT 0,
  en_espera SMALLINT DEFAULT 0,
  comentario TEXT,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cab_fac (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  serie VARCHAR(10) DEFAULT NULL,
  factura VARCHAR(100) DEFAULT NULL,
  id_divisa INTEGER DEFAULT NULL,
  tarifa_cliente INTEGER DEFAULT 1,
  fecha DATE DEFAULT NULL,
  fecha_cobro DATE DEFAULT NULL,
  hora TIME DEFAULT '00:00:00',

  -- Datos del Cliente e Identificación Fiscal
  id_cliente INTEGER NOT NULL DEFAULT 0,
  codigo_cliente VARCHAR(100) DEFAULT NULL,
  cliente VARCHAR(100) DEFAULT NULL,
  cif_nif_siret VARCHAR(30) DEFAULT NULL, -- Campo genérico para España/Francia

  -- Dirección Fiscal
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(20) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,

  -- Envío (Francia suele usar mucho los puntos de entrega)
  direccion1_entrega VARCHAR(100) DEFAULT NULL,
  direccion2_entrega VARCHAR(100) DEFAULT NULL,
  poblacion_entrega VARCHAR(100) DEFAULT NULL,
  provincia_entrega VARCHAR(45) DEFAULT NULL,
  cp_entrega VARCHAR(20) DEFAULT NULL,
  id_pais_entrega INTEGER DEFAULT NULL,
  email_entrega VARCHAR(150) DEFAULT NULL,
  comentarios_entrega TEXT,

  -- Contacto
  telefono VARCHAR(25) DEFAULT NULL,
  fax VARCHAR(25) DEFAULT NULL,
  movil VARCHAR(25) DEFAULT NULL,
  email VARCHAR(100) DEFAULT NULL,

  -- Totales (Cambiado double por DECIMAL para precisión contable)
  subtotal DECIMAL(15,4) DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_dto_pp DECIMAL(5,2) DEFAULT 0,
  dto_pp DECIMAL(15,4) DEFAULT 0,
  base_total DECIMAL(15,4) DEFAULT 0,
  iva_total DECIMAL(15,4) DEFAULT 0,
  total DECIMAL(15,4) DEFAULT 0,

  -- Desglose por tipos de IVA (Hasta 4)
  base1 DECIMAL(15,4) DEFAULT 0,
  base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0,
  base4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0,
  porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0,
  porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0,
  iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0,
  iva4 DECIMAL(15,4) DEFAULT 0,

  -- Recargos e IRPF (Lógica España, valor 0 para Francia)
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0,
  porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0,
  porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0,
  rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0,
  rec4 DECIMAL(15,4) DEFAULT 0,
  total_recargo DECIMAL(15,4) DEFAULT 0,
  porc_irpf DECIMAL(5,2) DEFAULT 0,
  irpf DECIMAL(15,4) DEFAULT 0,

  -- Datos de Cobro y Bancarios
  entregado_a_cuenta DECIMAL(15,4) DEFAULT 0,
  importe_pendiente DECIMAL(15,4) DEFAULT 0,
  id_forma_pago INTEGER DEFAULT 0,
  forma_pago VARCHAR(100) DEFAULT NULL,
  codigo_entidad VARCHAR(4) DEFAULT NULL,
  oficina_entidad VARCHAR(4) DEFAULT NULL,
  dc_cuenta VARCHAR(2) DEFAULT NULL,
  cuenta_corriente VARCHAR(15) DEFAULT NULL, -- Aumentado por si acaso

  -- Desglose de pagos realizados
  efectivo DECIMAL(15,4) DEFAULT 0,
  transferencia DECIMAL(15,4) DEFAULT 0,
  tarjeta DECIMAL(15,4) DEFAULT 0,
  cheque DECIMAL(15,4) DEFAULT 0,
  internet DECIMAL(15,4) DEFAULT 0,
  pagado DECIMAL(15,4) DEFAULT 0,
  pendiente DECIMAL(15,4) DEFAULT 0,

  -- Otros Gastos
  desc_gasto1 VARCHAR(45) DEFAULT NULL,
  desc_gasto2 VARCHAR(45) DEFAULT NULL,
  desc_gasto3 VARCHAR(45) DEFAULT NULL,
  imp_gasto1 DECIMAL(15,4) DEFAULT 0,
  imp_gasto2 DECIMAL(15,4) DEFAULT 0,
  imp_gasto3 DECIMAL(15,4) DEFAULT 0,
  porc_iva_gasto1 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gasto2 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gasto3 DECIMAL(5,2) DEFAULT 0,
  iva_gasto1 DECIMAL(15,4) DEFAULT 0,
  iva_gasto2 DECIMAL(15,4) DEFAULT 0,
  iva_gasto3 DECIMAL(15,4) DEFAULT 0,

  -- Estados y Auditoría
  impreso SMALLINT DEFAULT 0,
  cobrado SMALLINT DEFAULT 0,
  contabilizado SMALLINT DEFAULT 0,
  asiento INTEGER DEFAULT NULL,
  id_transportista INTEGER DEFAULT 0,
  ejercicio INTEGER DEFAULT NULL,
  editable SMALLINT DEFAULT 1,
  id_agente INTEGER DEFAULT 0,
  es_simplificada SMALLINT DEFAULT 0,
  id_usuario INTEGER DEFAULT 0,
  en_espera SMALLINT DEFAULT 0,
  pedido_cliente INTEGER DEFAULT 0,
  comentario TEXT,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cab_pre (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  presupuesto VARCHAR(25) DEFAULT '0',
  id_divisa INTEGER NOT NULL DEFAULT 1,
  valor_divisa DECIMAL(12,6) DEFAULT 1.0, -- Mayor precisión para tipos de cambio
  fecha DATE DEFAULT NULL,
  valido_hasta DATE DEFAULT NULL,
  fecha_aprobacion DATE DEFAULT NULL,

  -- Datos del Cliente e ID Fiscal Universal
  id_cliente INTEGER DEFAULT -1,
  codigo_cliente VARCHAR(100) DEFAULT NULL,
  cliente VARCHAR(100) DEFAULT NULL,
  cif_nif_siret VARCHAR(30) DEFAULT NULL,
  atencion_de VARCHAR(100) DEFAULT NULL, -- Nombre del contacto

  -- Dirección Fiscal
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(20) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(45) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,

  -- Dirección de Entrega y Lugar
  direccion1_entrega VARCHAR(100) DEFAULT NULL,
  direccion2_entrega VARCHAR(100) DEFAULT NULL,
  poblacion_entrega VARCHAR(100) DEFAULT NULL,
  provincia_entrega VARCHAR(45) DEFAULT NULL,
  cp_entrega VARCHAR(20) DEFAULT NULL,
  id_pais_entrega INTEGER DEFAULT NULL,
  email_entrega VARCHAR(150) DEFAULT NULL,
  comentarios_entrega TEXT,
  lugar_entrega TEXT,

  -- Contacto
  telefono VARCHAR(25) DEFAULT NULL,
  movil VARCHAR(25) DEFAULT NULL,
  fax VARCHAR(25) DEFAULT NULL,
  email VARCHAR(100) DEFAULT NULL,

  -- Totales y Descuentos
  subtotal DECIMAL(15,4) DEFAULT 0, -- Se suele usar 'base' o 'subtotal'
  base_total DECIMAL(15,4) DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_dto_pp DECIMAL(5,2) DEFAULT 0,
  dto_pp DECIMAL(15,4) DEFAULT 0,
  total_iva DECIMAL(15,4) DEFAULT 0,
  total_recargo DECIMAL(15,4) DEFAULT 0,
  total_presupuesto DECIMAL(15,4) DEFAULT 0, -- Equivalente a tu 'total'

  -- Desglose de Impuestos (4 IVAs)
  base1 DECIMAL(15,4) DEFAULT 0,
  base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0,
  base4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0,
  porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0,
  porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0,
  iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0,
  iva4 DECIMAL(15,4) DEFAULT 0,

  -- Recargos e IRPF (Compatibilidad España)
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0,
  porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0,
  porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0,
  rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0,
  rec4 DECIMAL(15,4) DEFAULT 0,
  porc_irpf DECIMAL(5,2) DEFAULT 0,
  irpf DECIMAL(15,4) DEFAULT 0,

  -- Totales por tipo
  total1 DECIMAL(15,4) DEFAULT 0,
  total2 DECIMAL(15,4) DEFAULT 0,
  total3 DECIMAL(15,4) DEFAULT 0,
  total4 DECIMAL(15,4) DEFAULT 0,

  -- Gastos Distribuidos
  gastos_distribuidos1 VARCHAR(100) DEFAULT NULL,
  gastos_distribuidos2 VARCHAR(100) DEFAULT NULL,
  gastos_distribuidos3 VARCHAR(100) DEFAULT NULL,
  importe_gasto1 DECIMAL(15,4) DEFAULT 0,
  importe_gasto2 DECIMAL(15,4) DEFAULT 0,
  importe_gasto3 DECIMAL(15,4) DEFAULT 0,
  porc_iva_gasto1 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gasto2 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gasto3 DECIMAL(5,2) DEFAULT 0,
  iva_gasto1 DECIMAL(15,4) DEFAULT 0,
  iva_gasto2 DECIMAL(15,4) DEFAULT 0,
  iva_gasto3 DECIMAL(15,4) DEFAULT 0,

  -- Seguimiento y Enlace
  aprobado SMALLINT DEFAULT 0,
  impreso SMALLINT DEFAULT 0,
  editable SMALLINT DEFAULT 1,
  factura VARCHAR(25) DEFAULT '0',
  albaran VARCHAR(25) DEFAULT '0',
  pedido VARCHAR(25) DEFAULT '0',
  importe_factura DECIMAL(15,4) DEFAULT 0,
  importe_pendiente DECIMAL(15,4) DEFAULT 0,
  id_forma_pago INTEGER DEFAULT 0,
  id_agente INTEGER DEFAULT 0,
  ejercicio INTEGER DEFAULT NULL,
  comentarios TEXT,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS devoluciones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket INTEGER DEFAULT 0,
  fecha_devolucion TIMESTAMP DEFAULT NULL,
  atendido_por VARCHAR(100) DEFAULT NULL,

  -- Cliente y Artículo
  id_cliente INTEGER DEFAULT 0,
  cliente VARCHAR(100) DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo_articulo VARCHAR(20) DEFAULT NULL,
  descripcion VARCHAR(150) DEFAULT NULL,

  comentarios TEXT,
  ejercicio INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fac_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  factura VARCHAR(30) DEFAULT NULL,
  fecha DATE DEFAULT NULL,
  fecha_recepcion DATE DEFAULT NULL,
  pedido VARCHAR(30) DEFAULT NULL,
  albaran VARCHAR(20) DEFAULT NULL,

  -- Identificación del Proveedor
  id_proveedor INTEGER DEFAULT 0,
  codigo_proveedor VARCHAR(20) DEFAULT NULL,
  proveedor VARCHAR(100) DEFAULT NULL,
  cif_nif_siret VARCHAR(30) DEFAULT NULL, -- Genérico para ES (CIF) / FR (SIRET)

  -- Localización y Contacto
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,
  telefono VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(20) DEFAULT NULL,
  fax VARCHAR(20) DEFAULT NULL,

  -- Totales y Descuentos (Decimal para precisión)
  subtotal DECIMAL(15,4) DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  base_total DECIMAL(15,4) DEFAULT 0,
  iva_total DECIMAL(15,4) DEFAULT 0,
  total DECIMAL(15,4) DEFAULT 0,

  -- Desglose de Impuestos (4 tipos)
  base1 DECIMAL(15,4) DEFAULT 0,
  base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0,
  base4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0,
  porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0,
  porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0,
  iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0,
  iva4 DECIMAL(15,4) DEFAULT 0,

  -- Retenciones y Recargos (España)
  porc_irpf DECIMAL(5,2) DEFAULT 0,
  irpf DECIMAL(15,4) DEFAULT 0,
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0,
  porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0,
  porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0,
  rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0,
  rec4 DECIMAL(15,4) DEFAULT 0,
  total_recargo DECIMAL(15,4) DEFAULT 0,

  -- Totales por tipo
  total1 DECIMAL(15,4) DEFAULT 0,
  total2 DECIMAL(15,4) DEFAULT 0,
  total3 DECIMAL(15,4) DEFAULT 0,
  total4 DECIMAL(15,4) DEFAULT 0,

  -- Gestión de Gastos adicionales
  id_tipo_gasto INTEGER DEFAULT 0,
  desc_gasto1 VARCHAR(45) DEFAULT NULL,
  desc_gasto2 VARCHAR(45) DEFAULT NULL,
  desc_gasto3 VARCHAR(45) DEFAULT NULL,
  imp_gasto1 DECIMAL(15,4) DEFAULT 0,
  imp_gasto2 DECIMAL(15,4) DEFAULT 0,
  imp_gasto3 DECIMAL(15,4) DEFAULT 0,
  porc_iva_gasto1 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gasto2 DECIMAL(5,2) DEFAULT 0,
  porc_iva_gasto3 DECIMAL(5,2) DEFAULT 0,
  iva_gasto1 DECIMAL(15,4) DEFAULT 0,
  iva_gasto2 DECIMAL(15,4) DEFAULT 0,
  iva_gasto3 DECIMAL(15,4) DEFAULT 0,
  gasto_to_coste SMALLINT DEFAULT 0,

  -- Estados y Relaciones
  id_forma_pago INTEGER DEFAULT 0,
  pagado SMALLINT DEFAULT 0,
  contabilizada SMALLINT DEFAULT 0,
  impreso SMALLINT DEFAULT 0,
  editable SMALLINT DEFAULT 1,
  ejercicio INTEGER DEFAULT NULL,
  comentario TEXT,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS gastos_ped_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT 0, -- Referencia a la cabecera del pedido
  descripcion VARCHAR(45) DEFAULT NULL,
  importe DECIMAL(15,4) DEFAULT 0,
  ident INTEGER DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lin_alb (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(20) DEFAULT NULL,

  -- Cambiamos a TEXT para descripciones largas de proyectos creativos
  descripcion TEXT,

  -- Cantidad con 3 decimales para horas (ej: 1.250 horas)
  cantidad DECIMAL(12,3) DEFAULT 0,

  -- Precios e Importes con precisión contable
  precio DECIMAL(15,4) DEFAULT 0,
  precio_recom DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,

  -- Descuentos e Impuestos (IVA/TVA y Recargo ES)
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Gestión de Lotes o Proyectos
  promocion SMALLINT DEFAULT 0,
  id_lote INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS lin_alb_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(20) DEFAULT NULL,

  -- TEXT para descripciones detalladas de servicios subcontratados
  descripcion TEXT,

  -- Cantidad: He cambiado INTEGER a DECIMAL(12,3)
  -- Aunque en tu SQL original era INT, para creativos es mejor DECIMAL
  -- por si compras "media jornada" (0.500) o "horas de servidor" (10.5)
  cantidad DECIMAL(12,3) DEFAULT 0,

  -- Precios e Importes (Precisión contable)
  precio DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,
  coste_real_unidad DECIMAL(15,4) DEFAULT 0, -- Lo que realmente te costó tras gastos

  -- Descuentos e Impuestos
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lin_fac (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(100) DEFAULT NULL,

  -- Para el sector creativo: descripciones sin límite de caracteres
  descripcion TEXT,

  -- Cantidad: 3 decimales para horas o unidades fraccionadas
  cantidad DECIMAL(12,3) DEFAULT 0,

  -- Importes con precisión contable (DECIMAL)
  precio DECIMAL(15,4) DEFAULT 0,
  precio_recom DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,

  -- Descuentos e Impuestos
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Trazabilidad y Logística
  promocion SMALLINT DEFAULT 0,
  id_lote INTEGER DEFAULT NULL,
  albaran VARCHAR(45) DEFAULT NULL, -- Enlace visual al albarán de origen

  -- Trazabilidad estándar
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lin_fac_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(20) DEFAULT NULL,
  codigo_articulo_proveedor VARCHAR(45) DEFAULT NULL,

  -- TEXT para descripciones largas de servicios o licencias
  descripcion TEXT,

  -- Cantidad: Volvemos a DECIMAL por la flexibilidad de horas/servicios
  cantidad DECIMAL(12,3) DEFAULT 0,

  -- Importes con precisión contable
  precio DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,
  coste_real_unidad DECIMAL(15,4) DEFAULT 0,

  -- Descuentos e Impuestos
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Enlaces y Referencias
  pedido INTEGER DEFAULT 0,
  albaran VARCHAR(45) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para búsquedas rápidas por código de artículo
CREATE INDEX IF NOT EXISTS idx_lin_fac_pro_codigo ON lin_fac_pro(codigo);

CREATE TABLE IF NOT EXISTS lin_ped (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(20) DEFAULT NULL,

  -- Para creativos: descripciones extensas para el pliego de condiciones
  descripcion TEXT,

  -- Cantidades: DECIMAL para soportar horas o entregas parciales
  cantidad DECIMAL(12,3) DEFAULT 0,
  cantidad_a_servir DECIMAL(12,3) DEFAULT 0,

  -- Precios e Importes con precisión contable
  precio DECIMAL(15,4) DEFAULT 0,
  precio_recom DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,

  -- Descuentos e Impuestos (IVA/TVA y Recargo ES)
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Flags y Logística
  id_lote INTEGER DEFAULT NULL,
  promocion SMALLINT DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lin_ped_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT 0,
  codigo VARCHAR(100) DEFAULT NULL,

  -- TEXT para especificaciones técnicas del encargo
  descripcion TEXT,

  -- Cantidades: Pasamos de INT a DECIMAL para flexibilidad (horas, jornadas, GB)
  cantidad DECIMAL(12,3) DEFAULT 0,
  cantidad_recibida DECIMAL(12,3) DEFAULT 0,
  cantidad_pendiente DECIMAL(12,3) DEFAULT 0,
  en_albaran DECIMAL(12,3) DEFAULT 0,

  -- Precios e Importes (Precisión contable)
  precio DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,
  coste_real_unidad DECIMAL(15,4) DEFAULT 0,

  -- Descuentos e Impuestos
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Gestión de estado
  etiquetas INTEGER DEFAULT 0,
  cerrado SMALLINT DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lin_pre (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(20) DEFAULT NULL,

  -- Para creativos: descripciones detalladas del servicio/obra
  descripcion TEXT,

  -- Cantidad con 3 decimales (horas, jornadas, partes de un proyecto)
  cantidad DECIMAL(12,3) DEFAULT 0,

  -- Precios e Importes con precisión contable
  precio DECIMAL(15,4) DEFAULT 0,
  precio_recom DECIMAL(15,4) DEFAULT 0,
  subtotal DECIMAL(15,4) DEFAULT 0,

  -- Descuentos e Impuestos (IVA/TVA y Recargo ES)
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_iva DECIMAL(5,2) DEFAULT 0,
  iva DECIMAL(15,4) DEFAULT 0,
  porc_rec DECIMAL(5,2) DEFAULT 0,
  rec DECIMAL(15,4) DEFAULT 0,

  total DECIMAL(15,4) DEFAULT 0,

  -- Flags y Logística
  promocion SMALLINT DEFAULT 0,
  id_lote INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para acelerar la carga de presupuestos con muchas líneas
CREATE INDEX IF NOT EXISTS idx_lin_pre_cab ON lin_pre(id_cab);

CREATE TABLE IF NOT EXISTS lin_res (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cab INTEGER DEFAULT NULL,
  id_articulo INTEGER DEFAULT NULL,
  codigo VARCHAR(20) DEFAULT NULL,

  -- TEXT para detallar condiciones de la reserva
  descripcion TEXT,

  -- Cantidad: De INT a DECIMAL para reservar horas o jornadas
  cantidad DECIMAL(12,3) DEFAULT 0,

  -- Precios e Importes
  precio DECIMAL(15,4) DEFAULT 0,
  precio_recom DECIMAL(15,4) DEFAULT 0,
  importe_dto DECIMAL(15,4) DEFAULT 0,
  total DECIMAL(15,4) DEFAULT 0,

  -- Fechas de control de reserva
  fecha_reserva DATE DEFAULT NULL,
  reservado_hasta DATE DEFAULT NULL,

  -- Flags y Logística
  promocion SMALLINT DEFAULT 0,
  id_lote INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para buscar reservas por fecha de vencimiento
CREATE INDEX IF NOT EXISTS idx_lin_res_hasta ON lin_res(reservado_hasta);

CREATE TABLE IF NOT EXISTS divisas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre_divisa VARCHAR(45) DEFAULT NULL, -- Ej: "Euro", "US Dollar"

  -- Usamos 6 decimales para tipos de cambio (estándar bancario)
  valor_divisa DECIMAL(12,6) DEFAULT 1.0,

  id_divisa_base VARCHAR(45) DEFAULT NULL, -- Ej: "EUR"
  orden INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ped_cli (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pedido VARCHAR(45) DEFAULT '0',
  pedido_cliente VARCHAR(100) DEFAULT NULL, -- Referencia del cliente (PO Number)
  fecha DATE DEFAULT NULL,
  fecha_limite_entrega DATE DEFAULT NULL,
  id_divisa INTEGER NOT NULL DEFAULT 1,

  -- Datos del Cliente
  id_cliente INTEGER DEFAULT 0,
  codigo_cliente VARCHAR(20) DEFAULT NULL,
  cliente VARCHAR(100) DEFAULT NULL,
  cif_nif_siret VARCHAR(100) DEFAULT NULL, -- Identificación internacional
  email VARCHAR(100) DEFAULT NULL,
  telefono VARCHAR(25) DEFAULT NULL,
  movil VARCHAR(25) DEFAULT NULL,
  fax VARCHAR(25) DEFAULT NULL,

  -- Dirección de Facturación
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL, -- Ampliado para códigos postales internacionales
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL, -- Unificado para España/Francia
  id_pais INTEGER DEFAULT NULL,

  -- Dirección de Entrega (Vital para envío de assets físicos o material)
  direccion_entrega1 VARCHAR(100) DEFAULT NULL,
  direccion_entrega2 VARCHAR(100) DEFAULT NULL,
  cp_entrega VARCHAR(15) DEFAULT NULL,
  poblacion_entrega VARCHAR(100) DEFAULT NULL,
  provincia_entrega VARCHAR(100) DEFAULT NULL,
  id_pais_entrega INTEGER DEFAULT NULL,
  email_entrega VARCHAR(150) DEFAULT NULL,
  comentarios_entrega TEXT,

  -- Totales y Descuentos (Precisión Decimal)
  subtotal DECIMAL(15,4) DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  porc_dto_pp DECIMAL(5,2) DEFAULT 0, -- Pronto Pago
  dto_pp DECIMAL(15,4) DEFAULT 0,
  base_total DECIMAL(15,4) DEFAULT 0,
  iva_total DECIMAL(15,4) DEFAULT 0,
  rec_total DECIMAL(15,4) DEFAULT 0,
  irpf DECIMAL(15,4) DEFAULT 0,
  porc_irpf DECIMAL(5,2) DEFAULT 0,
  entregado_a_cuenta DECIMAL(15,4) DEFAULT 0,
  total_pedido DECIMAL(15,4) DEFAULT 0,

  -- Desglose de Impuestos (4 tramos)
  base1 DECIMAL(15,4) DEFAULT 0, base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0, base4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0, porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0, porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0, iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0, iva4 DECIMAL(15,4) DEFAULT 0,

  -- Recargo de Equivalencia (Específico España)
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0, porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0, porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0, rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0, rec4 DECIMAL(15,4) DEFAULT 0,

  -- Totales por tramo
  total1 DECIMAL(15,4) DEFAULT 0, total2 DECIMAL(15,4) DEFAULT 0,
  total3 DECIMAL(15,4) DEFAULT 0, total4 DECIMAL(15,4) DEFAULT 0,

  -- Gastos Adicionales
  desc_gasto1 VARCHAR(45) DEFAULT NULL, imp_gasto1 DECIMAL(15,4) DEFAULT 0,
  porc_iva_gasto1 DECIMAL(5,2) DEFAULT 0, iva_gasto1 DECIMAL(15,4) DEFAULT 0,
  gasto_to_coste SMALLINT DEFAULT 0,

  -- Estado y Trazabilidad de Documentos
  impreso SMALLINT DEFAULT 0,
  facturado SMALLINT DEFAULT 0,
  traspasado_albaran SMALLINT DEFAULT 0,
  traspasado_factura SMALLINT DEFAULT 0,
  enviado SMALLINT DEFAULT 0,
  completo SMALLINT DEFAULT 0,
  entregado SMALLINT DEFAULT 0,
  albaran VARCHAR(45) DEFAULT '0',
  factura VARCHAR(45) DEFAULT '0',
  fecha_factura DATE DEFAULT NULL,

  -- Otros
  id_forma_pago INTEGER DEFAULT 0,
  id_transportista INTEGER DEFAULT NULL,
  id_agente INTEGER DEFAULT 0,
  ejercicio INTEGER DEFAULT NULL,
  editable SMALLINT DEFAULT 1,
  comentario TEXT,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ped_pro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pedido VARCHAR(45) DEFAULT '0',
  ejercicio INTEGER DEFAULT NULL,
  fecha DATE DEFAULT NULL,
  recepcion DATE DEFAULT NULL, -- Fecha real de recepción del servicio/material
  fecha_entrega DATE DEFAULT NULL, -- Fecha estimada

  -- Identificación del Proveedor
  id_proveedor INTEGER DEFAULT 0,
  codigo_proveedor VARCHAR(20) DEFAULT NULL,
  proveedor VARCHAR(100) DEFAULT NULL,
  cif_nif_siret VARCHAR(45) DEFAULT NULL, -- Unificado para ES/FR

  -- Localización del Proveedor
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,

  -- Contacto
  telefono VARCHAR(20) DEFAULT NULL,
  fax VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(45) DEFAULT NULL,

  -- Totales y Financiero (DECIMAL para precisión)
  subtotal DECIMAL(15,4) DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto DECIMAL(15,4) DEFAULT 0,
  base_total DECIMAL(15,4) DEFAULT 0,
  rec_total DECIMAL(15,4) DEFAULT 0, -- Recargo total
  total DECIMAL(15,4) DEFAULT 0,

  -- Desglose de Impuestos (4 tramos)
  base1 DECIMAL(15,4) DEFAULT 0, base2 DECIMAL(15,4) DEFAULT 0,
  base3 DECIMAL(15,4) DEFAULT 0, base4 DECIMAL(15,4) DEFAULT 0,
  porc_iva1 DECIMAL(5,2) DEFAULT 0, porc_iva2 DECIMAL(5,2) DEFAULT 0,
  porc_iva3 DECIMAL(5,2) DEFAULT 0, porc_iva4 DECIMAL(5,2) DEFAULT 0,
  iva1 DECIMAL(15,4) DEFAULT 0, iva2 DECIMAL(15,4) DEFAULT 0,
  iva3 DECIMAL(15,4) DEFAULT 0, iva4 DECIMAL(15,4) DEFAULT 0,

  -- Recargos (Específico ES)
  recargo_equivalencia SMALLINT DEFAULT 0,
  porc_rec1 DECIMAL(5,2) DEFAULT 0, porc_rec2 DECIMAL(5,2) DEFAULT 0,
  porc_rec3 DECIMAL(5,2) DEFAULT 0, porc_rec4 DECIMAL(5,2) DEFAULT 0,
  rec1 DECIMAL(15,4) DEFAULT 0, rec2 DECIMAL(15,4) DEFAULT 0,
  rec3 DECIMAL(15,4) DEFAULT 0, rec4 DECIMAL(15,4) DEFAULT 0,

  -- Totales por tramo
  total1 DECIMAL(15,4) DEFAULT 0, total2 DECIMAL(15,4) DEFAULT 0,
  total3 DECIMAL(15,4) DEFAULT 0, total4 DECIMAL(15,4) DEFAULT 0,

  -- Gestión de Gastos Adicionales (Transporte, Aduanas, etc.)
  desc_gasto1 VARCHAR(45) DEFAULT NULL, imp_gasto1 DECIMAL(15,4) DEFAULT 0,
  porc_iva_gasto1 DECIMAL(5,2) DEFAULT 0, iva_gasto1 DECIMAL(15,4) DEFAULT 0,
  gasto_to_coste SMALLINT DEFAULT 0, -- Importante para el escandallo

  -- Dirección de Entrega (Útil si recibes material en el estudio)
  direccion_entrega1 VARCHAR(100) DEFAULT NULL,
  direccion_entrega2 VARCHAR(100) DEFAULT NULL,
  cp_entrega VARCHAR(15) DEFAULT NULL,
  poblacion_entrega VARCHAR(100) DEFAULT NULL,
  provincia_entrega VARCHAR(100) DEFAULT NULL,
  id_pais_entrega INTEGER DEFAULT NULL,
  nombre_cliente VARCHAR(100) DEFAULT NULL, -- Si es para un proyecto directo de un cliente

  -- Estados y Control
  enviado SMALLINT DEFAULT 0,
  recibido SMALLINT DEFAULT 0,
  recibido_completo SMALLINT DEFAULT 0,
  genero_pendiente SMALLINT DEFAULT 0,
  traspasado SMALLINT DEFAULT 0,
  impreso SMALLINT DEFAULT 0,
  editable SMALLINT DEFAULT 1,
  id_forma_pago INTEGER DEFAULT 0,
  pedido_cliente INTEGER DEFAULT 0, -- Relación con el encargo del cliente
  comentario TEXT,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recibos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  recibo INTEGER DEFAULT 0,
  fecha DATE DEFAULT NULL,
  fecha_cobro DATE DEFAULT NULL,
  ejercicio INTEGER DEFAULT NULL,

  -- Descripciones para el documento impreso
  descripcion_fecha1 VARCHAR(100) DEFAULT NULL,
  descripcion_fecha2 VARCHAR(100) DEFAULT NULL,
  localidad VARCHAR(100) DEFAULT NULL,

  -- Cliente
  id_cliente INTEGER DEFAULT 0,
  cliente VARCHAR(100) DEFAULT NULL,
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,

  -- Concepto e Importes
  concepto TEXT,
  importe DECIMAL(15,4) DEFAULT 0,
  importe_en_texto TEXT, -- Útil para cheques o recibos formales

  -- Datos Bancarios (Adaptado a SEPA: IBAN/BIC)
  descripcion_entidad VARCHAR(255) DEFAULT NULL,
  descripcion_oficina VARCHAR(254) DEFAULT NULL,
  iban VARCHAR(34) DEFAULT NULL, -- Reemplaza el formato antiguo entidad/oficina/dc/cuenta
  bic_swift VARCHAR(11) DEFAULT NULL,

  -- Para mantener compatibilidad con datos antiguos si los hubiera
  entidad VARCHAR(4) DEFAULT NULL,
  oficina_entidad VARCHAR(4) DEFAULT NULL,
  dc_cuenta VARCHAR(2) DEFAULT NULL,
  cuenta_corriente VARCHAR(10) DEFAULT NULL,

  -- Estado
  cobrado SMALLINT DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reportes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(255) NOT NULL, -- El nombre del reporte (ej: "Factura Pro-forma")
  descripcion TEXT,             -- Qué datos saca o para qué sirve
  ruta_archivo TEXT NOT NULL,   -- Ruta al .xml, .jasper o plantilla de diseño
  modulo VARCHAR(100) NOT NULL, -- Ej: "ventas", "compras", "proyectos"
  seccion VARCHAR(100) NOT NULL,-- Ej: "facturacion", "listados"
  orden INTEGER NOT NULL DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS reservas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  reserva INTEGER DEFAULT 0,
  fecha DATE DEFAULT NULL,
  fecha_limite DATE DEFAULT NULL,
  ejercicio INTEGER DEFAULT NULL,

  -- Datos del Cliente
  id_cliente INTEGER DEFAULT 0,
  cliente VARCHAR(100) DEFAULT NULL,
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,
  telefono1 VARCHAR(20) DEFAULT NULL,
  telefono2 VARCHAR(20) DEFAULT NULL,

  -- Gestión Económica (Señales y Pagos)
  importe DECIMAL(15,4) DEFAULT 0,   -- Total de la reserva
  entregado DECIMAL(15,4) DEFAULT 0, -- Lo que ya ha pagado como señal
  pendiente DECIMAL(15,4) DEFAULT 0, -- Lo que falta por pagar

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS acum_articulos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_empresa INTEGER NOT NULL DEFAULT 0,
  id_articulo INTEGER NOT NULL,
  ejercicio INTEGER NOT NULL, -- He añadido este campo para separar años fácilmente

  -- Unidades Compradas (Gastos de recursos/materiales)
  unid_comp_enero DECIMAL(12,3) DEFAULT 0, unid_comp_febrero DECIMAL(12,3) DEFAULT 0,
  unid_comp_marzo DECIMAL(12,3) DEFAULT 0, unid_comp_abril DECIMAL(12,3) DEFAULT 0,
  unid_comp_mayo DECIMAL(12,3) DEFAULT 0, unid_comp_junio DECIMAL(12,3) DEFAULT 0,
  unid_comp_julio DECIMAL(12,3) DEFAULT 0, unid_comp_agosto DECIMAL(12,3) DEFAULT 0,
  unid_comp_septiembre DECIMAL(12,3) DEFAULT 0, unid_comp_octubre DECIMAL(12,3) DEFAULT 0,
  unid_comp_noviembre DECIMAL(12,3) DEFAULT 0, unid_comp_diciembre DECIMAL(12,3) DEFAULT 0,
  unid_comp_ejercicio DECIMAL(15,3) DEFAULT 0,

  -- Acumulado Compras (Importe €/$)
  acum_comp_enero DECIMAL(15,4) DEFAULT 0, acum_comp_febrero DECIMAL(15,4) DEFAULT 0,
  acum_comp_marzo DECIMAL(15,4) DEFAULT 0, acum_comp_abril DECIMAL(15,4) DEFAULT 0,
  acum_comp_mayo DECIMAL(15,4) DEFAULT 0, acum_comp_junio DECIMAL(15,4) DEFAULT 0,
  acum_comp_julio DECIMAL(15,4) DEFAULT 0, acum_comp_agosto DECIMAL(15,4) DEFAULT 0,
  acum_comp_septiembre DECIMAL(15,4) DEFAULT 0, acum_comp_octubre DECIMAL(15,4) DEFAULT 0,
  acum_comp_noviembre DECIMAL(15,4) DEFAULT 0, acum_comp_diciembre DECIMAL(15,4) DEFAULT 0,
  acum_comp_ejercicio DECIMAL(18,4) DEFAULT 0,

  -- Unidades Vendidas (Horas de diseño, proyectos, etc.)
  unid_vent_enero DECIMAL(12,3) DEFAULT 0, unid_vent_febrero DECIMAL(12,3) DEFAULT 0,
  unid_vent_marzo DECIMAL(12,3) DEFAULT 0, unid_vent_abril DECIMAL(12,3) DEFAULT 0,
  unid_vent_mayo DECIMAL(12,3) DEFAULT 0, unid_vent_junio DECIMAL(12,3) DEFAULT 0,
  unid_vent_julio DECIMAL(12,3) DEFAULT 0, unid_vent_agosto DECIMAL(12,3) DEFAULT 0,
  unid_vent_septiembre DECIMAL(12,3) DEFAULT 0, unid_vent_octubre DECIMAL(12,3) DEFAULT 0,
  unid_vent_noviembre DECIMAL(12,3) DEFAULT 0, unid_vent_diciembre DECIMAL(12,3) DEFAULT 0,
  unid_vent_acumulado DECIMAL(15,3) DEFAULT 0,

  -- Acumulado Ventas (Facturación €/$)
  acum_vent_enero DECIMAL(15,4) DEFAULT 0, acum_vent_febrero DECIMAL(15,4) DEFAULT 0,
  acum_vent_marzo DECIMAL(15,4) DEFAULT 0, acum_vent_abril DECIMAL(15,4) DEFAULT 0,
  acum_vent_mayo DECIMAL(15,4) DEFAULT 0, acum_vent_junio DECIMAL(15,4) DEFAULT 0,
  acum_vent_julio DECIMAL(15,4) DEFAULT 0, acum_vent_agosto DECIMAL(15,4) DEFAULT 0,
  acum_vent_septiembre DECIMAL(15,4) DEFAULT 0, acum_vent_octubre DECIMAL(15,4) DEFAULT 0,
  acum_vent_noviembre DECIMAL(15,4) DEFAULT 0, acum_vent_diciembre DECIMAL(15,4) DEFAULT 0,
  acum_vent_ejercicio DECIMAL(18,4) DEFAULT 0,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para sacar informes rápidos por artículo y año
CREATE INDEX IF NOT EXISTS idx_acum_art_ejercicio ON acum_articulos(id_articulo, ejercicio);

CREATE TABLE IF NOT EXISTS acum_clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_empresa INTEGER NOT NULL DEFAULT 0,
  id_cliente INTEGER NOT NULL DEFAULT 0,
  ejercicio INTEGER NOT NULL, -- Fundamental para históricos anuales

  -- Importes de ventas mensuales (Facturación neta)
  acum_enero DECIMAL(15,4) DEFAULT 0,
  acum_febrero DECIMAL(15,4) DEFAULT 0,
  acum_marzo DECIMAL(15,4) DEFAULT 0,
  acum_abril DECIMAL(15,4) DEFAULT 0,
  acum_mayo DECIMAL(15,4) DEFAULT 0,
  acum_junio DECIMAL(15,4) DEFAULT 0,
  acum_julio DECIMAL(15,4) DEFAULT 0,
  acum_agosto DECIMAL(15,4) DEFAULT 0,
  acum_septiembre DECIMAL(15,4) DEFAULT 0,
  acum_octubre DECIMAL(15,4) DEFAULT 0,
  acum_noviembre DECIMAL(15,4) DEFAULT 0,
  acum_diciembre DECIMAL(15,4) DEFAULT 0,

  acum_ejercicio DECIMAL(18,4) DEFAULT 0, -- Total anual por cliente

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para sacar el ranking de mejores clientes por año rápidamente
CREATE INDEX IF NOT EXISTS idx_acum_cli_ejercicio ON acum_clientes(id_cliente, ejercicio);

CREATE TABLE IF NOT EXISTS acum_proveedores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_empresa INTEGER NOT NULL DEFAULT 0,
  id_proveedor INTEGER DEFAULT 0,
  ejercicio INTEGER NOT NULL, -- Para separar los gastos por año

  -- Acumulado de compras/gastos mensuales
  acum_enero DECIMAL(15,4) DEFAULT 0,
  acum_febrero DECIMAL(15,4) DEFAULT 0,
  acum_marzo DECIMAL(15,4) DEFAULT 0,
  acum_abril DECIMAL(15,4) DEFAULT 0,
  acum_mayo DECIMAL(15,4) DEFAULT 0,
  acum_junio DECIMAL(15,4) DEFAULT 0,
  acum_julio DECIMAL(15,4) DEFAULT 0,
  acum_agosto DECIMAL(15,4) DEFAULT 0,
  acum_septiembre DECIMAL(15,4) DEFAULT 0,
  acum_octubre DECIMAL(15,4) DEFAULT 0,
  acum_noviembre DECIMAL(15,4) DEFAULT 0,
  acum_diciembre DECIMAL(15,4) DEFAULT 0,

  acum_total DECIMAL(18,4) DEFAULT 0, -- Total anual de compras al proveedor

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para optimizar los informes de gastos
CREATE INDEX IF NOT EXISTS idx_acum_prov_ejercicio ON acum_proveedores(id_proveedor, ejercicio);

CREATE TABLE IF NOT EXISTS agenda (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fecha DATE DEFAULT NULL,
  hora VARCHAR(45) DEFAULT NULL,

  -- Fechas completas para integración con calendarios (tipo Google Calendar)
  inicio DATETIME DEFAULT NULL,
  fin DATETIME DEFAULT NULL,

  -- Información de la tarea/cita
  asunto VARCHAR(100) DEFAULT NULL, -- Ampliado de 40 a 100 por si los asuntos son largos
  descripcion_asunto TEXT, -- Cambiado de LONGTEXT a TEXT (suficiente para SQLite/MariaDB)

  -- Categorización y Visualización
  estado VARCHAR(50) DEFAULT NULL,    -- Ej: "Pendiente", "Completado", "Cancelado"
  importancia VARCHAR(50) DEFAULT NULL, -- Ej: "Alta", "Normal", "Baja"
  color VARCHAR(45) DEFAULT NULL,      -- Para el código Hexadecimal (ej: #FF5733)

  -- Relaciones
  id_usuario INTEGER DEFAULT 0,
  id_cliente INTEGER DEFAULT NULL,
  id_especialidad INTEGER DEFAULT NULL,
  id_departamento INTEGER DEFAULT NULL,

  -- Flags de control
  avisar_tiempo VARCHAR(50) DEFAULT NULL,
  is_medica SMALLINT DEFAULT 0,  -- Lo mantengo por compatibilidad, aunque quizás en tu sector sea "is_presencial"
  is_cita SMALLINT DEFAULT 0,
  is_privado SMALLINT DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para que el calendario cargue rápido al cambiar de mes
CREATE INDEX IF NOT EXISTS idx_agenda_fechas ON agenda(inicio, fin);
CREATE INDEX IF NOT EXISTS idx_agenda_cliente ON agenda(id_cliente);

CREATE TABLE IF NOT EXISTS agentes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(15) DEFAULT NULL,
  nombre VARCHAR(100) DEFAULT NULL, -- Ampliado a 100 para nombres completos

  -- Identificación internacional (DNI, NIE, SS)
  dni_nie_id VARCHAR(20) DEFAULT NULL,

  -- Contacto
  telefono VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(20) DEFAULT NULL,
  email VARCHAR(150) DEFAULT NULL,

  -- Financiero (DECIMAL para precisión en comisiones)
  facturado DECIMAL(15,4) DEFAULT 0,
  pendiente DECIMAL(15,4) DEFAULT 0,

  comentarios TEXT,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS agentes_comisiones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_agente INTEGER DEFAULT NULL,
  id_tarifa INTEGER DEFAULT NULL,

  -- Tramos de importe (DECIMAL para precisión en moneda)
  importe_desde DECIMAL(15,4) DEFAULT 0,
  importe_hasta DECIMAL(15,4) DEFAULT 0,

  -- Porcentaje de comisión (ej: 5.50 para un 5.5%)
  porc_comision DECIMAL(5,2) DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para buscar rápidamente los tramos de un agente
CREATE INDEX IF NOT EXISTS idx_comisiones_agente ON agentes_comisiones(id_agente);

-- Índice para búsquedas rápidas por código de agente
CREATE INDEX IF NOT EXISTS idx_agentes_codigo ON agentes(codigo);


CREATE TABLE IF NOT EXISTS articulos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(200) DEFAULT NULL,
  codigo_barras VARCHAR(30) DEFAULT NULL,
  codigo_fabricante VARCHAR(100) DEFAULT NULL,
  slug VARCHAR(100) DEFAULT '',

  -- Descripciones: TEXT para pliegos de condiciones técnicas
  descripcion TEXT,
  descripcion_reducida VARCHAR(100) DEFAULT NULL,
  comentario TEXT,

  -- Clasificación
  id_proveedor INTEGER DEFAULT NULL,
  id_familia INTEGER DEFAULT NULL,
  id_seccion INTEGER DEFAULT NULL,
  id_subfamilia INTEGER DEFAULT NULL,
  kit SMALLINT DEFAULT 0, -- Para "Packs" de servicios

  -- Precios y Márgenes (Precisión contable)
  coste DECIMAL(15,4) DEFAULT 0,
  coste_real DECIMAL(15,4) DEFAULT 0,
  pvp DECIMAL(15,4) DEFAULT 0,
  margen DECIMAL(15,4) DEFAULT 0,
  margen_min DECIMAL(15,4) DEFAULT 0,
  pvp_incluye_iva SMALLINT DEFAULT 0,

  -- Impuestos (IVA / TVA)
  id_tipos_iva INTEGER DEFAULT NULL,
  tipo_iva DECIMAL(5,2) DEFAULT 0,

  -- Descuentos
  porc_dto DECIMAL(5,2) DEFAULT 0,
  dto_proveedor DECIMAL(15,4) DEFAULT 0,

  -- Stock y Logística (Decimal para horas o servicios fraccionados)
  stock_real DECIMAL(12,3) DEFAULT 0,
  stock_fisico_almacen DECIMAL(12,3) DEFAULT 0,
  stock_maximo DECIMAL(12,3) DEFAULT 0,
  stock_minimo DECIMAL(12,3) DEFAULT 0,
  valor_stock DECIMAL(15,4) DEFAULT 0,
  unidades_reservadas DECIMAL(12,3) DEFAULT 0,
  cantidad_pendiente_recibir DECIMAL(12,3) DEFAULT 0,
  controlar_stock INTEGER DEFAULT 0,
  tipo_unitad VARCHAR(100) DEFAULT NULL, -- Ej: "Horas", "Días", "Proyecto"
  localizacion_en_almacen VARCHAR(100) DEFAULT NULL,

  -- Estadísticas Rápidas
  fecha_ultima_compra DATE DEFAULT NULL,
  fecha_ultima_venta DATE DEFAULT NULL,
  unidades_compradas DECIMAL(15,3) DEFAULT 0,
  unidades_vendidas DECIMAL(15,3) DEFAULT 0,
  importe_acumulado_compras DECIMAL(15,4) DEFAULT 0,
  importe_acumulado_ventas DECIMAL(15,4) DEFAULT 0,

  -- Flags de Visibilidad y Estado
  mostrar_web SMALLINT DEFAULT 0,
  id_web INTEGER DEFAULT 0,
  articulo_promocionado SMALLINT DEFAULT 0,
  mostrar_en_cuadro SMALLINT DEFAULT 0,
  lotes SMALLINT DEFAULT 0,
  etiquetas INTEGER DEFAULT 0,
  paquetes INTEGER DEFAULT 0,
  fecha_prevista_recepcion DATE DEFAULT NULL,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  UNIQUE(codigo)
);

CREATE TABLE IF NOT EXISTS articulos_imagenes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_articulo INTEGER NOT NULL,

  -- Ruta de la imagen o Base64 (TEXT es ideal para rutas largas o URIs)
  imagen TEXT,

  -- Para gestionar el orden en un carrusel o galería
  orden INTEGER DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para cargar la galería de un artículo al instante
CREATE INDEX IF NOT EXISTS idx_art_img_rel ON articulos_imagenes(id_articulo);

CREATE TABLE IF NOT EXISTS articulos_lotes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_articulo INTEGER NOT NULL,

  -- Identificador del lote o serie
  lote VARCHAR(45) DEFAULT NULL,

  -- Fecha de caducidad o fin de licencia
  caducidad DATE DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para búsquedas rápidas por artículo y control de caducidades
CREATE INDEX IF NOT EXISTS idx_lotes_articulo ON articulos_lotes(id_articulo);
CREATE INDEX IF NOT EXISTS idx_lotes_caducidad ON articulos_lotes(caducidad);

CREATE TABLE IF NOT EXISTS articulos_volumen (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_producto INTEGER DEFAULT NULL,
  id_tarifa INTEGER DEFAULT 1,

  -- Rangos de cantidad (DECIMAL para soportar horas o fracciones)
  desde DECIMAL(12,3) DEFAULT 0,
  hasta DECIMAL(12,3) DEFAULT 0,

  -- Precio resultante para ese tramo
  precio DECIMAL(15,4) DEFAULT 0,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para buscar precios rápidamente al añadir líneas a un documento
CREATE INDEX IF NOT EXISTS idx_art_vol_prod ON articulos_volumen(id_producto, id_tarifa);

CREATE TABLE IF NOT EXISTS avisos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_tipoaviso INTEGER DEFAULT NULL,
  id_usuario_origen INTEGER DEFAULT NULL,
  id_usuario_destino INTEGER DEFAULT NULL,
  id_empresa INTEGER DEFAULT NULL,

  -- Contenido del mensaje
  aviso TEXT,
  fecha_hora_aviso DATETIME DEFAULT NULL,

  -- Estado de la notificación
  completado SMALLINT DEFAULT 0, -- 0: Pendiente, 1: Leído/Cerrado

  -- Trazabilidad automática
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para cargar rápidamente los avisos pendientes de un usuario
CREATE INDEX IF NOT EXISTS idx_avisos_destino ON avisos(id_usuario_destino, completado);

CREATE TABLE IF NOT EXISTS bancos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  descripcion VARCHAR(100) DEFAULT NULL, -- Nombre de la cuenta (ej: "Cuenta Corriente Crédit Agricole")

  -- Formato SEPA Internacional (Indispensable para FR/ES)
  iban VARCHAR(34) DEFAULT NULL,
  bic_swift VARCHAR(11) DEFAULT NULL,

  -- Estado Financiero
  saldo DECIMAL(15,2) DEFAULT 0.00, -- Ampliado para evitar desbordamiento en saldos altos

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cliente_direcciones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER DEFAULT NULL,
  descripcion VARCHAR(100) DEFAULT NULL, -- Ej: "Oficina Lyon", "Almacén Madrid"

  -- Localización Internacional
  direccion1 VARCHAR(100) DEFAULT NULL, -- Ampliado de 45 a 100
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,         -- Ampliado para CP internacionales
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL, -- Para Provincias (ES) o Departamentos (FR)
  id_pais INTEGER DEFAULT NULL,

  -- Contacto específico para esta ubicación
  email VARCHAR(150) DEFAULT NULL,
  comentarios TEXT,

  -- Control de logística
  direccion_envio SMALLINT DEFAULT 0, -- 1 si es la dirección por defecto para envíos

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para localizar rápidamente todas las sedes de un cliente
CREATE INDEX IF NOT EXISTS idx_direcciones_cliente ON cliente_direcciones(id_cliente);


CREATE TABLE IF NOT EXISTS clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo_cliente VARCHAR(25) DEFAULT NULL,
  id_divisa INTEGER NOT NULL DEFAULT 1,
  id_empresa INTEGER DEFAULT NULL,
  id_idioma_documentos INTEGER DEFAULT 1, -- Clave para facturas en FR o ES

  -- Nombres y Branding
  nombre VARCHAR(100) DEFAULT NULL,
  apellido1 VARCHAR(100) DEFAULT NULL,
  apellido2 VARCHAR(100) DEFAULT NULL,
  nombre_fiscal VARCHAR(100) DEFAULT NULL,
  nombre_comercial VARCHAR(100) DEFAULT NULL,
  persona_contacto VARCHAR(100) DEFAULT NULL,

  -- Identificación Fiscal Internacional
  cif_nif_siret VARCHAR(35) DEFAULT NULL, -- Unificado para España y Francia
  cif_vies VARCHAR(35) DEFAULT NULL,      -- Para operadores intracomunitarios (ROI)

  -- Localización
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(15) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia_region VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,

  -- Contacto
  telefono1 VARCHAR(20) DEFAULT NULL,
  telefono2 VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(20) DEFAULT NULL,
  fax VARCHAR(20) DEFAULT NULL,
  email VARCHAR(100) DEFAULT NULL,
  web VARCHAR(100) DEFAULT NULL,

  -- Configuración Comercial y Pago
  id_tipo_cliente INTEGER DEFAULT NULL,
  id_tarifa INTEGER DEFAULT 1,
  id_forma_pago INTEGER DEFAULT NULL,
  dia_pago1 INTEGER DEFAULT 0,
  dia_pago2 INTEGER DEFAULT 0,
  porc_dto_cliente DECIMAL(5,2) DEFAULT 0,
  recargo_equivalencia SMALLINT DEFAULT 0, -- (España)
  irpf SMALLINT DEFAULT 0,                 -- (España)
  grupo_iva INTEGER DEFAULT 1,             -- (TVA Francia / IVA España)

  -- Datos Bancarios (Actualizado a SEPA)
  iban VARCHAR(34) DEFAULT NULL,
  bic_swift VARCHAR(11) DEFAULT NULL,
  entidad_bancaria VARCHAR(4) DEFAULT NULL, -- Compatibilidad legacy
  oficina_bancaria VARCHAR(4) DEFAULT NULL,
  dc VARCHAR(2) DEFAULT NULL,
  cuenta_corriente VARCHAR(50) DEFAULT NULL,

  -- Financiero (DECIMAL para precisión)
  acumulado_ventas DECIMAL(15,4) DEFAULT 0,
  ventas_ejercicio DECIMAL(15,4) DEFAULT 0,
  riesgo_maximo DECIMAL(15,4) DEFAULT 0,
  deuda_actual DECIMAL(15,4) DEFAULT 0,
  importe_a_cuenta DECIMAL(15,4) DEFAULT 0,
  importe_pendiente DECIMAL(15,4) DEFAULT 0,
  vales DECIMAL(15,4) DEFAULT 0,

  -- Logística y Agentes
  id_agente INTEGER DEFAULT NULL,
  id_transportista INTEGER DEFAULT NULL,

  -- Estado y Seguridad
  bloqueado SMALLINT DEFAULT 0,
  comentario_bloqueo TEXT,
  fecha_alta DATE DEFAULT NULL,
  fecha_ultima_compra DATE DEFAULT NULL,
  fecha_nacimiento DATE DEFAULT NULL,

  -- Acceso Web / App
  acceso_web VARCHAR(50) DEFAULT NULL,
  password_web VARCHAR(50) DEFAULT NULL,
  id_web INTEGER DEFAULT NULL,

  -- Notas
  comentarios TEXT,
  observaciones VARCHAR(255) DEFAULT NULL,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para búsquedas rápidas en el CRM
CREATE INDEX IF NOT EXISTS idx_cli_codigo ON clientes(codigo_cliente);
CREATE INDEX IF NOT EXISTS idx_cli_nombre ON clientes(nombre_fiscal);
CREATE INDEX IF NOT EXISTS idx_cli_cif ON clientes(cif_nif_siret);

CREATE TABLE IF NOT EXISTS clientes_deuda (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_empresa INTEGER NOT NULL DEFAULT 0,
  id_cliente INTEGER DEFAULT NULL,

  -- Documentación vinculada
  fecha DATE DEFAULT NULL,
  vencimiento DATE DEFAULT NULL,
  documento VARCHAR(50) DEFAULT '0', -- Nº de factura o recibo
  id_ticket INTEGER DEFAULT 0,
  id_factura INTEGER DEFAULT 0,
  tipo INTEGER DEFAULT 0, -- Ej: 1-Factura, 2-Recibo, 3-Nota de cargo

  -- Gestión de Importes (Precisión Decimal)
  importe DECIMAL(15,4) DEFAULT 0,
  pagado DECIMAL(15,4) DEFAULT 0,
  pendiente_cobro DECIMAL(15,4) DEFAULT 0,

  -- Desglose por Método de Pago (Útil para conciliación)
  importe_efectivo DECIMAL(15,4) DEFAULT 0,
  importe_tarjeta DECIMAL(15,4) DEFAULT 0,
  importe_cheque DECIMAL(15,4) DEFAULT 0,
  importe_transferencia DECIMAL(15,4) DEFAULT 0,
  importe_domiciliacion DECIMAL(15,4) DEFAULT 0,
  importe_internet DECIMAL(15,4) DEFAULT 0,
  importe_vale DECIMAL(15,4) DEFAULT 0,

  -- Datos Bancarios del Cobro

  iban VARCHAR(34) DEFAULT NULL, -- Añadido para entorno SEPA (FR/ES)

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para el informe de cobros pendientes (Cash Flow)
CREATE INDEX IF NOT EXISTS idx_deuda_vencimiento ON clientes_deuda(vencimiento, pendiente_cobro);
CREATE INDEX IF NOT EXISTS idx_deuda_cliente ON clientes_deuda(id_cliente);


CREATE TABLE IF NOT EXISTS clientes_entregas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER DEFAULT 0,
  fecha_entrega DATE DEFAULT NULL,

  -- Gestión económica con precisión
  importe DECIMAL(15,4) DEFAULT 0,     -- Lo que el cliente entregó originalmente
  disponible DECIMAL(15,4) DEFAULT 0,  -- El saldo que queda por consumir de ese pago

  -- Categorización
  concepto VARCHAR(255) DEFAULT NULL, -- Cambiado de INT a VARCHAR para permitir texto (ej: "Anticipo Proyecto Logo")
  id_concepto_ref INTEGER DEFAULT 0,  -- Para mantener la referencia numérica si es necesario

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para encontrar rápidamente el saldo a cuenta de un cliente
CREATE INDEX IF NOT EXISTS idx_entregas_cliente ON clientes_entregas(id_cliente, disponible);


CREATE TABLE IF NOT EXISTS clientes_intervalo_horario (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER DEFAULT NULL,

  -- Día de la semana (Recomiendo usar 1-7 para facilitar la lógica de programación)
  dia_semana VARCHAR(45) DEFAULT NULL,

  -- Bloque Mañana
  horario_manana_inicio TIME DEFAULT NULL,
  horario_manana_fin TIME DEFAULT NULL,

  -- Bloque Tarde
  horario_tarde_inicio TIME DEFAULT NULL,
  horario_tarde_fin TIME DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para consultar el horario al abrir la ficha del cliente o la agenda
CREATE INDEX IF NOT EXISTS idx_horario_cliente ON clientes_intervalo_horario(id_cliente);

CREATE TABLE IF NOT EXISTS codigotarifa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo_tarifa VARCHAR(20) DEFAULT NULL,
  descripcion VARCHAR(100) DEFAULT NULL, -- Ampliado para nombres más descriptivos

  -- Vinculación Geográfica y Monetaria
  id_pais INTEGER DEFAULT NULL,
  id_monedas INTEGER DEFAULT NULL,

  -- Lógica de Rentabilidad
  margen DECIMAL(15,4) DEFAULT 0,     -- Margen de beneficio estándar para esta tarifa
  margen_min DECIMAL(15,4) DEFAULT 0, -- Margen mínimo (suelo) para evitar ventas en pérdida

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  UNIQUE(descripcion)
);

CREATE TABLE IF NOT EXISTS deudas_proveedores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_empresa INTEGER NOT NULL DEFAULT 0,
  id_proveedor INTEGER DEFAULT NULL,

  -- Referencias del Documento
  id_documento INTEGER DEFAULT NULL, -- Referencia a la tabla facturas_proveedores
  documento VARCHAR(45) DEFAULT NULL,    -- Nº de factura del proveedor

  -- Fechas Críticas
  fecha_deuda DATE DEFAULT NULL,
  vencimiento DATE DEFAULT NULL,         -- Fecha en la que "sale" el dinero

  -- Gestión económica (DECIMAL para precisión)
  importe_deuda DECIMAL(15,4) DEFAULT 0,
  pagado DECIMAL(15,4) DEFAULT 0,
  pendiente DECIMAL(15,4) DEFAULT 0,

  -- Método de Pago y Tesorería
  pago_por VARCHAR(45) DEFAULT NULL,           -- Ej: "Transferencia", "Giro SEPA", "Tarjeta"
  numero_tarjeta_cuenta VARCHAR(45) DEFAULT NULL, -- Referencia rápida o IBAN parcial

  -- Enlace Contable (Si usas un motor externo)
  id_asiento INTEGER DEFAULT NULL,
  asiento_numero INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para el flujo de caja saliente (Cash Out)
CREATE INDEX IF NOT EXISTS idx_prov_deuda_venc ON deudas_proveedores(vencimiento, pendiente);
CREATE INDEX IF NOT EXISTS idx_prov_deuda_rel ON deudas_proveedores(id_proveedor);

CREATE TABLE IF NOT EXISTS familias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(100) DEFAULT NULL,
  familia VARCHAR(100) DEFAULT NULL, -- El nombre de la categoría
  slug VARCHAR(100) DEFAULT '',      -- Para URLs o búsquedas amigables

  -- Jerarquía
  id_seccion INTEGER DEFAULT 0,      -- Vinculación con un nivel superior (Secciones)

  -- Contenido Visual y Configuración
  image TEXT,                        -- Ruta o URI de la imagen del icono de la familia
  type VARCHAR(10) DEFAULT NULL,     -- Aumentado a 10 por si usas "SERVICE", "PRODUCT", etc.

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para organizar el catálogo rápidamente
CREATE INDEX IF NOT EXISTS idx_familias_seccion ON familias(id_seccion);

CREATE TABLE IF NOT EXISTS formpago (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(8) DEFAULT NULL,
  forma_pago VARCHAR(50) DEFAULT NULL,

  -- Configuración de Plazos
  numero_plazos INTEGER DEFAULT 1,
  dias_hasta_pago INTEGER DEFAULT 0,    -- Días de carencia antes del primer pago
  dias_entre_plazos INTEGER DEFAULT 0,  -- Frecuencia entre cuotas

  -- Días Fijos de Pago (común en grandes empresas)
  dia_pago1 INTEGER DEFAULT 0,
  dia_pago2 INTEGER DEFAULT 0,
  dia_pago3 INTEGER DEFAULT 0,
  dia_pago4 INTEGER DEFAULT 0,

  -- Contabilidad y Tipo
  cuenta_cont_pago VARCHAR(20) DEFAULT NULL,
  al_contado SMALLINT DEFAULT 0, -- 1 si el pago es inmediato (efectivo/tarjeta)

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS histo_clientes_deuda (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_empresa INTEGER NOT NULL DEFAULT 0,

  -- Relación con la deuda original (id de la tabla clientes_deuda)
  id_cab INTEGER NOT NULL DEFAULT 0,

  -- Datos del movimiento
  fecha_movimiento DATE DEFAULT NULL,
  importe_anterior DECIMAL(15,4) DEFAULT 0, -- Saldo antes del pago
  pagado DECIMAL(15,4) DEFAULT 0,           -- Cuánto se ha pagado en este movimiento
  importe_cambio DECIMAL(15,4) DEFAULT 0,   -- Por si hubo devolución de cambio
  pendiente_cobro DECIMAL(15,4) DEFAULT 0,  -- Saldo resultante tras el pago

  -- Desglose por método (Indispensable para conciliación)
  importe_efectivo DECIMAL(15,4) DEFAULT 0,
  importe_tarjeta DECIMAL(15,4) DEFAULT 0,
  importe_cheque DECIMAL(15,4) DEFAULT 0,
  importe_transferencia DECIMAL(15,4) DEFAULT 0,
  importe_domiciliacion DECIMAL(15,4) DEFAULT 0,
  importe_internet DECIMAL(15,4) DEFAULT 0,
  importe_vale DECIMAL(15,4) DEFAULT 0,

  -- Datos bancarios del movimiento (Opcional/SEPA)
  entidad VARCHAR(50) DEFAULT NULL,
  oficina VARCHAR(50) DEFAULT NULL,
  dc VARCHAR(50) DEFAULT NULL,
  cuenta VARCHAR(50) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para reconstruir el historial de una deuda específica
CREATE INDEX IF NOT EXISTS idx_histo_deuda_cab ON histo_clientes_deuda(id_cab);

CREATE TABLE IF NOT EXISTS idiomas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- Nombre del idioma (ej: "Español", "Français", "English")
  idioma VARCHAR(45) DEFAULT NULL,

  -- Código ISO (Recomendado para integraciones y traducciones automáticas)
  codigo_iso VARCHAR(5) DEFAULT NULL, -- ej: "es", "fr", "en"

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS kits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- Referencia al artículo "Padre" (el Kit)
  codigo_kit VARCHAR(200) DEFAULT NULL,

  -- Referencia al artículo "Hijo" (el Componente)
  id_componente INTEGER DEFAULT NULL,
  codigo_componente VARCHAR(100) DEFAULT NULL,
  descripcion VARCHAR(200) NOT NULL,

  -- Cantidades y Costes (Precisión Decimal)
  cantidad DECIMAL(12,3) NOT NULL DEFAULT 0,
  coste_base DECIMAL(15,4) NOT NULL DEFAULT 0,
  porc_dto DECIMAL(5,2) DEFAULT 0,
  coste_final DECIMAL(15,4) DEFAULT 0,

  -- Comportamiento de Inventario
  descontar_stock SMALLINT NOT NULL DEFAULT 1, -- 1: Descuenta los componentes al vender el kit

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para desglosar el kit rápidamente en el carrito/factura
CREATE INDEX IF NOT EXISTS idx_kits_padre ON kits(codigo_kit);
CREATE INDEX IF NOT EXISTS idx_kits_componente ON kits(id_componente);

CREATE TABLE IF NOT EXISTS monedas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- Identificación
  moneda VARCHAR(45) DEFAULT NULL,      -- Ej: "Euro", "US Dollar"
  nombre_corto VARCHAR(10) NOT NULL,    -- Ej: "EUR", "USD" (Código ISO)
  simbolo VARCHAR(5) DEFAULT NULL,      -- Ej: "€", "$"

  -- Lógica de Conversión
  cambio DECIMAL(15,6) DEFAULT 1.000000, -- Valor respecto a la moneda base
  fecha_cambio DATE DEFAULT NULL,        -- Última actualización del tipo de cambio

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  UNIQUE(nombre_corto)
);

CREATE TABLE IF NOT EXISTS paises (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pais VARCHAR(100) DEFAULT NULL,        -- Ej: "Francia", "España"
  country_code VARCHAR(5) NOT NULL,      -- ISO Alpha-2 (FR, ES, PT)
  id_monedas INTEGER DEFAULT NULL,       -- Relación con la tabla 'monedas'

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  UNIQUE(pais),
  UNIQUE(country_code)
);

-- Índice para búsquedas rápidas por código de país
CREATE INDEX IF NOT EXISTS idx_paises_code ON paises(country_code);

CREATE TABLE IF NOT EXISTS permisos_agenda (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- El usuario que concede el acceso o el que va a editar
  id_usuario_editor INTEGER DEFAULT NULL,

  -- El dueño de la agenda a la que se accede
  id_usuario_agenda INTEGER DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para verificar permisos de forma instantánea al abrir la agenda
CREATE INDEX IF NOT EXISTS idx_permisos_relacion
ON permisos_agenda(id_usuario_editor, id_usuario_agenda);

CREATE TABLE IF NOT EXISTS personascontactocliente (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER DEFAULT NULL,
  nombre VARCHAR(100) DEFAULT NULL, -- Ampliado para nombres completos
  cargo_empresa VARCHAR(100) DEFAULT NULL, -- Ej: "Chef de projet", "Director Creativo"
  email VARCHAR(150) DEFAULT NULL,

  -- Teléfonos y sus etiquetas descriptivas
  telefono1 VARCHAR(20) DEFAULT NULL,
  desc_telefono1 VARCHAR(45) DEFAULT NULL, -- Ej: "Directo", "Extensión 4"
  telefono2 VARCHAR(20) DEFAULT NULL,
  desc_telefono2 VARCHAR(45) DEFAULT NULL,
  telefono3 VARCHAR(20) DEFAULT NULL,
  desc_telefono3 VARCHAR(45) DEFAULT NULL,

  -- Móviles (especialmente útiles para mensajería directa)
  movil1 VARCHAR(20) DEFAULT NULL,
  desc_movil1 VARCHAR(45) DEFAULT NULL, -- Ej: "Solo WhatsApp", "Personal"
  movil2 VARCHAR(20) DEFAULT NULL,
  desc_movil2 VARCHAR(45) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para cargar rápidamente los contactos de un cliente específico
CREATE INDEX IF NOT EXISTS idx_contactos_cliente ON personascontactocliente(id_cliente);

CREATE TABLE IF NOT EXISTS personascontactoproveedor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_proveedor INTEGER DEFAULT NULL,
  nombre VARCHAR(100) DEFAULT NULL,
  cargo_empresa VARCHAR(100) DEFAULT NULL, -- Ej: "Responsable de Production", "Comercial"
  email VARCHAR(150) DEFAULT NULL,

  -- Centralita y extensiones
  telefono1 VARCHAR(20) DEFAULT NULL,
  desc_telefono1 VARCHAR(45) DEFAULT NULL,
  telefono2 VARCHAR(20) DEFAULT NULL,
  desc_telefono2 VARCHAR(45) DEFAULT NULL,
  telefono3 VARCHAR(20) DEFAULT NULL,
  desc_telefono3 VARCHAR(45) DEFAULT NULL,

  -- Contacto directo
  movil1 VARCHAR(20) DEFAULT NULL,
  desc_movil1 VARCHAR(45) DEFAULT NULL,
  movil2 VARCHAR(20) DEFAULT NULL,
  desc_movil2 VARCHAR(45) DEFAULT NULL,

  -- Trazabilidad técnica
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para agilizar la búsqueda de interlocutores de un proveedor
CREATE INDEX IF NOT EXISTS idx_contactos_proveedor ON personascontactoproveedor(id_proveedor);

CREATE TABLE IF NOT EXISTS personascontactotransportista (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_transportista INTEGER DEFAULT NULL,
  nombre VARCHAR(100) DEFAULT NULL,
  cargo_empresa VARCHAR(100) DEFAULT NULL, -- Ej: "Gestor de Tráfico", "Responsable Logística"
  email VARCHAR(150) DEFAULT NULL,

  -- Teléfonos de oficina/centralita
  telefono1 VARCHAR(20) DEFAULT NULL,
  desc_telefono1 VARCHAR(45) DEFAULT NULL,
  telefono2 VARCHAR(20) DEFAULT NULL,
  desc_telefono2 VARCHAR(45) DEFAULT NULL,
  telefono3 VARCHAR(20) DEFAULT NULL,
  desc_telefono3 VARCHAR(45) DEFAULT NULL,

  -- Contacto directo/móvil
  movil VARCHAR(20) DEFAULT NULL,
  desc_movil1 VARCHAR(45) DEFAULT NULL,
  movil2 VARCHAR(20) DEFAULT NULL,
  desc_movil2 VARCHAR(45) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para localizar rápidamente al contacto del transportista asignado
CREATE INDEX IF NOT EXISTS idx_contactos_transp ON personascontactotransportista(id_transportista);

CREATE TABLE IF NOT EXISTS proveedor_entregas_a_cuenta (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_proveedor INTEGER DEFAULT NULL,

  -- Gestión de fechas y descripción
  fecha_entrega DATE DEFAULT NULL,
  concepto VARCHAR(100) DEFAULT NULL, -- Ampliado para descripciones más claras

  -- Control económico (DECIMAL para evitar errores de redondeo)
  importe DECIMAL(15,4) DEFAULT 0,    -- Dinero total entregado
  disponible DECIMAL(15,4) DEFAULT 0, -- Saldo que aún no ha sido aplicado a facturas

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para calcular rápidamente el saldo a favor con un proveedor
CREATE INDEX IF NOT EXISTS idx_entregas_prov ON proveedor_entregas_a_cuenta(id_proveedor, disponible);

CREATE TABLE IF NOT EXISTS proveedores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(25) DEFAULT NULL,
  proveedor VARCHAR(100) DEFAULT NULL,
  cif VARCHAR(20) DEFAULT NULL, -- Ampliado para NIF/SIRET

  -- Sede Fiscal
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(12) DEFAULT NULL,
  poblacion VARCHAR(100) DEFAULT NULL,
  provincia VARCHAR(100) DEFAULT NULL,
  id_pais INTEGER DEFAULT NULL,
  id_monedas INTEGER DEFAULT NULL,

  -- Contacto General
  telefono1 VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(20) DEFAULT NULL,
  email VARCHAR(100) DEFAULT NULL,
  web VARCHAR(100) DEFAULT NULL,

  -- Logística (Almacén de recogida)
  direccion_almacen VARCHAR(100) DEFAULT NULL,
  cp_almacen VARCHAR(12) DEFAULT NULL,
  poblacion_almacen VARCHAR(100) DEFAULT NULL,
  id_pais_almacen INTEGER DEFAULT NULL,

  -- Configuración Comercial y Pago
  id_forma_pago INTEGER DEFAULT NULL,
  dia_cobro INTEGER DEFAULT 0,
  dto DECIMAL(5,2) DEFAULT 0,
  deuda_maxima DECIMAL(15,4) DEFAULT 0,

  -- Datos Bancarios (IBAN/SWIFT recomendado en el código)
  cc_proveedor VARCHAR(34) DEFAULT NULL, -- Ampliado para IBAN completo

  -- Fiscalidad (Clave para España/Francia)
  tipo_iva TINYINT NOT NULL DEFAULT 1,
  retencion_irpf DECIMAL(5,2) DEFAULT 0,
  tipo_retencion INTEGER DEFAULT 0,
  recargo_equivalencia SMALLINT DEFAULT 0,

  -- Históricos y Control
  fecha_alta DATE DEFAULT NULL,
  fecha_ultima_compra DATE DEFAULT NULL,
  importe_acumulado_compras DECIMAL(15,4) DEFAULT 0,
  deuda_actual DECIMAL(15,4) DEFAULT 0,
  entregado_a_cuenta DECIMAL(15,4) DEFAULT 0,

  comentarios TEXT,
  texto_para_pedidos TEXT,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para búsquedas rápidas por nombre o código
CREATE INDEX IF NOT EXISTS idx_prov_nombre ON proveedores(proveedor);
CREATE INDEX IF NOT EXISTS idx_prov_cif ON proveedores(cif);


CREATE TABLE IF NOT EXISTS secciones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(10) DEFAULT NULL, -- Aumentado de 3 a 10 para mayor flexibilidad
  seccion VARCHAR(100) DEFAULT NULL,
  slug VARCHAR(100) DEFAULT '',

  -- Clasificación y Multimedia
  image TEXT, -- URI o nombre de archivo para el icono principal
  type VARCHAR(10) DEFAULT NULL, -- Ej: 'SERV' (Servicio) o 'PROD' (Producto)

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para acelerar la navegación por categorías
CREATE INDEX IF NOT EXISTS idx_secciones_codigo ON secciones(codigo);

CREATE TABLE IF NOT EXISTS subfamilias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(10) DEFAULT NULL,
  sub_familia VARCHAR(100) DEFAULT NULL,
  slug VARCHAR(100) DEFAULT '',

  -- Jerarquía (Enlace con familias)
  id_familia INTEGER DEFAULT 0,

  -- Visual y Clasificación
  image TEXT,
  type VARCHAR(10) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para filtrar rápidamente por la familia padre
CREATE INDEX IF NOT EXISTS idx_subfam_parent ON subfamilias(id_familia);


CREATE TABLE IF NOT EXISTS tarifas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_articulo INTEGER DEFAULT NULL,
  id_codigo_tarifa INTEGER DEFAULT NULL, -- Relación con 'codigotarifa' (ej: Tarifa Web, Tarifa Amigo)

  -- Contexto Internacional
  id_pais INTEGER DEFAULT NULL,
  id_monedas INTEGER DEFAULT NULL,

  -- Precios y Márgenes
  pvp DECIMAL(15,4) DEFAULT 0,            -- El precio final de venta
  margen DECIMAL(5,2) DEFAULT 0,         -- Porcentaje de beneficio aplicado
  margen_minimo DECIMAL(5,2) DEFAULT 0,  -- El límite para que el comercial no pierda dinero

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices esenciales para que la búsqueda de precios sea instantánea
CREATE INDEX IF NOT EXISTS idx_tarifas_busqueda ON tarifas(id_articulo, id_codigo_tarifa);

CREATE TABLE IF NOT EXISTS tipocliente (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- Nombre del segmento (ej: "Empresa", "Autónomo", "Sector Público", "VIP")
  descripcion VARCHAR(100) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tiposubcliente (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_tipocliente INTEGER DEFAULT NULL, -- Relación con el tipo padre

  nombre VARCHAR(45) DEFAULT NULL,
  desc MEDIUMTEXT DEFAULT NULL,        -- Para notas sobre este perfil de cliente

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para filtrar sub-tipos según la categoría principal seleccionada
CREATE INDEX IF NOT EXISTS idx_subtipo_parent ON tiposubcliente(id_tipocliente);

CREATE TABLE IF NOT EXISTS tiposaviso (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- Nombre del tipo (ej: "Cobro", "Entrega", "Cita", "Stock Bajo")
  tipoaviso VARCHAR(45) DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tiposiva (
  id INTEGER PRIMARY KEY AUTOINCREMENT,

  -- Identificadores (ej: 'ES_GENERAL', 'FR_TVA_NORM')
  nombre_interno VARCHAR(45) NOT NULL,
  tipo VARCHAR(25) DEFAULT NULL,
  descripcion_tipo_iva VARCHAR(100) DEFAULT NULL, -- Ampliado para claridad

  -- Valores numéricos (Precision Decimal)
  iva DECIMAL(5,2) DEFAULT 0.00,
  recargo_equivalencia DECIMAL(5,2) DEFAULT 0.00,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transportista (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo VARCHAR(15) DEFAULT NULL,
  transportista VARCHAR(100) DEFAULT NULL, -- Nombre comercial de la agencia
  cif VARCHAR(20) DEFAULT NULL,            -- NIF o SIRET

  -- Sede de la Agencia
  direccion1 VARCHAR(100) DEFAULT NULL,
  direccion2 VARCHAR(100) DEFAULT NULL,
  cp VARCHAR(12) DEFAULT NULL,
  poblacion VARCHAR(45) DEFAULT NULL,
  provincia VARCHAR(45) DEFAULT NULL,
  pais VARCHAR(45) DEFAULT NULL,

  -- Contacto General
  telefono1 VARCHAR(20) DEFAULT NULL,
  telefono2 VARCHAR(20) DEFAULT NULL,
  movil VARCHAR(20) DEFAULT NULL,
  email VARCHAR(100) DEFAULT NULL,
  web VARCHAR(100) DEFAULT NULL,

  -- Vinculación Contable
  id_proveedor INTEGER NOT NULL DEFAULT 0, -- Referencia a la tabla 'proveedores'
  fecha_alta DATE DEFAULT NULL,

  -- Trazabilidad
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para búsquedas rápidas por nombre o código de agencia
CREATE INDEX IF NOT EXISTS idx_transp_nombre ON transportista(transportista);



-- Insertar datos maestros por defecto
INSERT INTO usuarios (username, password) VALUES ('admin', 'admin');
-- 1. Tarifas Base
INSERT INTO codigotarifa (id, descripcion, codigo_tarifa, id_pais, id_monedas)
VALUES (1, 'Precio venta público', 'PVP', 1, 1);

-- 2. Organización por defecto
INSERT INTO secciones (seccion, codigo)
VALUES ('Sin sección', 'SS');

-- 3. Configuración Financiera (Contado)
INSERT INTO formpago (codigo, forma_pago, dia_pago1, dia_pago2, dia_pago3, dia_pago4, dias_entre_plazos, cuenta_cont_pago, numero_plazos, dias_hasta_pago, al_contado)
VALUES ('CON', 'Contado', 0, 0, 0, 0, 0, '0', 1, 0, 1);

-- 4. Idiomas (Corregidos IDs únicos)
INSERT INTO idiomas (id, idioma) VALUES (1, 'Castellano');
INSERT INTO idiomas (id, idioma) VALUES (2, 'Français'); -- ID corregido a 2