package com.artstudio3d.creativeflow.database

import java.sql.Connection

object DbSchemaManager {
    fun inicializarNuevaEmpresa(conn: Connection) {
        try {
            // 1. Leer el archivo SQL (puedes leerlo como recurso o desde disco)
            val sqlScript = this::class.java.getResource("/files/init_empresa.sql")?.readText()
                ?: throw Exception("No se encontró el script de inicialización")

            // 2. Ejecutar el script
            // Nota: Algunos drivers JDBC no permiten ejecutar múltiples sentencias a la vez.
            // Es mejor separar por ";" y ejecutar una a una.
            conn.autoCommit = false
            val statements = sqlScript.split(";")

            conn.createStatement().use { stmt ->
                for (sql in statements) {
                    if (sql.trim().isNotBlank()) {
                        stmt.execute(sql.trim())
                    }
                }
            }
            conn.commit()
            println("✅ Esquema de empresa creado con éxito.")
        } catch (e: Exception) {
            conn.rollback()
            println("❌ Error inicializando esquema: ${e.message}")
            throw e
        }
    }
}