-- ==========================================================
-- ESTRUCTURA DE MAESTROS CON SOPORTE PARA ACENTOS
-- ==========================================================

-- 1. Habilitar la extensión unaccent (requiere superusuario)
CREATE EXTENSION IF NOT EXISTS unaccent;

-- 2. TABLA DE PAÍSES
CREATE TABLE IF NOT EXISTS paises (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    iso VARCHAR(5)
);

-- Índice especial para búsquedas rápidas sin acentos
CREATE INDEX IF NOT EXISTS idx_paises_nombre_unaccent ON paises (unaccent(nombre));

-- 3. TABLA DE POBLACIONES
CREATE TABLE IF NOT EXISTS poblaciones (
    id SERIAL PRIMARY KEY,
    id_pais INTEGER NOT NULL,
    cp VARCHAR(20),
    poblacion VARCHAR(255),
    poblacion_mayus VARCHAR(255),
    region_code VARCHAR(50),
    provincia_region VARCHAR(255),
    cp_adicionales TEXT,
    codigo_extra VARCHAR(100),
    CONSTRAINT fk_poblaciones_pais FOREIGN KEY (id_pais) REFERENCES paises(id) ON DELETE CASCADE
);

-- Índices optimizados para búsqueda INSENSITIVE a acentos y mayúsculas
CREATE INDEX IF NOT EXISTS idx_pob_cp ON poblaciones(cp);
CREATE INDEX IF NOT EXISTS idx_pob_nom_unaccent ON poblaciones(unaccent(poblacion));
CREATE INDEX IF NOT EXISTS idx_pob_prov_unaccent ON poblaciones(unaccent(provincia_region));

-- 4. TABLA DE MONEDAS
CREATE TABLE IF NOT EXISTS monedas (
    id SERIAL PRIMARY KEY,
    moneda VARCHAR(45),
    nombre_corto VARCHAR(10) NOT NULL UNIQUE,
    simbolo VARCHAR(5),
    cambio NUMERIC(15, 6) DEFAULT 1.000000,
    fecha_cambio DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ... (Inserciones de datos básicos igual que antes)