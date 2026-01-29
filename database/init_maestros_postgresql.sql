-- ==========================================================
-- ESTRUCTURA DE MAESTROS CON SOPORTE PARA ACENTOS (POSTGRESQL)
-- ==========================================================

-- 1. Habilitar la extensión unaccent (requiere superusuario)
CREATE EXTENSION IF NOT EXISTS unaccent;

-- 2. Crear función wrapper IMMUTABLE para permitir índices
-- Esto soluciona el error de "functions must be marked IMMUTABLE"
CREATE OR REPLACE FUNCTION f_unaccent(text)
  RETURNS text AS
$func$
SELECT public.unaccent('public.unaccent', $1)
$func$  LANGUAGE sql IMMUTABLE;

-- 3. TABLA DE MONEDAS (Estructura recuperada)
CREATE TABLE IF NOT EXISTS monedas (
    id SERIAL PRIMARY KEY,
    moneda VARCHAR(45) DEFAULT NULL,
    nombre_corto VARCHAR(10) NOT NULL UNIQUE,
    simbolo VARCHAR(5) DEFAULT NULL,
    cambio NUMERIC(15, 6) DEFAULT 1.000000,
    fecha_cambio DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. TABLA DE PAÍSES (Estructura recuperada con country_code)
CREATE TABLE IF NOT EXISTS paises (
    id SERIAL PRIMARY KEY,
    pais VARCHAR(100) NOT NULL UNIQUE,
    country_code VARCHAR(5) NOT NULL UNIQUE,
    id_monedas INTEGER REFERENCES monedas(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice inmutable para países
CREATE INDEX IF NOT EXISTS idx_paises_nombre_unaccent ON paises (f_unaccent(pais));
CREATE INDEX IF NOT EXISTS idx_paises_code ON paises (country_code);

-- 5. TABLA DE POBLACIONES
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

-- Índices optimizados usando la función inmutable f_unaccent
CREATE INDEX IF NOT EXISTS idx_pob_cp ON poblaciones(cp);
CREATE INDEX IF NOT EXISTS idx_pob_nom_unaccent ON poblaciones (f_unaccent(poblacion));
CREATE INDEX IF NOT EXISTS idx_pob_prov_unaccent ON poblaciones (f_unaccent(provincia_region));

-- 6. REAJUSTE DE SECUENCIAS (Para sincronizar tras la migración de SQLite)
-- Estas líneas se ejecutarán cada vez, asegurando que el ID serial no falle
SELECT setval(pg_get_serial_sequence('monedas', 'id'), coalesce(max(id), 1)) FROM monedas;
SELECT setval(pg_get_serial_sequence('paises', 'id'), coalesce(max(id), 1)) FROM paises;
SELECT setval(pg_get_serial_sequence('poblaciones', 'id'), coalesce(max(id), 1)) FROM poblaciones;