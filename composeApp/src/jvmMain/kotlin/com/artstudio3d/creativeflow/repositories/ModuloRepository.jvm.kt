// jvmMain/src/.../repositories/ModuloRepository.kt
package com.artstudio3d.creativeflow.repositories

import com.artstudio3d.creativeflow.models.ModuloModel
import com.artstudio3d.creativeflow.models.ModuloSeccionModel
import java.sql.DriverManager
import java.sql.Connection

actual object ModuloRepository {

    actual fun obtenerModulosPadre(): List<ModuloModel> {
        val lista = mutableListOf<ModuloModel>()

        // 1. Buscamos el archivo en las rutas relativas más comunes
        val posiblesRutas = listOf(
            "creativeflow.db",                            // Raíz del proyecto
            "composeApp/creativeflow.db",                 // Dentro del módulo
            System.getProperty("user.dir") + "/creativeflow.db" // Ruta absoluta dinámica
        )

        val archivoDb = posiblesRutas.map { java.io.File(it) }.firstOrNull { it.exists() }

        // Si no existe, imprimimos dónde lo buscó para que puedas corregirlo
        if (archivoDb == null) {
            println("⚠️ ERROR: No se encontró 'creativeflow.db'. Buscado en:")
            posiblesRutas.forEach { println("   - ${java.io.File(it).absolutePath}") }

            // Devolvemos datos de prueba para que la UI no esté vacía mientras arreglas la ruta
            return listOf(ModuloModel(1, "Error DB", "No se encontró el archivo .db", "Admin"))
        }

        val urlFinal = "jdbc:sqlite:${archivoDb.absolutePath}"
        println("✅ Base de datos conectada en: ${archivoDb.absolutePath}")

        try {
            DriverManager.getConnection(urlFinal).use { conn ->
                // DIAGNÓSTICO: Listamos las tablas que realmente tiene el archivo encontrado
                val rsTablas = conn.createStatement().executeQuery("SELECT name FROM sqlite_master WHERE type='table'")
                println("📊 Tablas detectadas en el archivo:")
                while (rsTablas.next()) {
                    println("   -> ${rsTablas.getString("name")}")
                }

                // 2. Consulta real
                val query = "SELECT id, nombre, descripcion, icono FROM modulos_padre"
                val stmt = conn.createStatement()
                val rs = stmt.executeQuery(query)

                while (rs.next()) {
                    lista.add(ModuloModel(
                        id = rs.getInt("id"),
                        // El operador ?: "" asegura que si es NULL, se convierta en un texto vacío
                        nombre = rs.getString("nombre") ?: "Sin nombre",
                        descripcion = rs.getString("descripcion") ?: "Sin descripción",
                        icono = rs.getString("icono") ?: "default_icon"
                    ))
                }
            }
        } catch (e: Exception) {
            println("❌ Error al ejecutar SQL: ${e.message}")
            e.printStackTrace()
        }

        return lista
    }
    // Añade la implementación real
    actual fun obtenerSecciones(moduloId: Int): List<ModuloSeccionModel> {
        val lista = mutableListOf<ModuloSeccionModel>()
        // Reutilizamos la lógica de búsqueda de archivo que ya tenemos
        val dbFile = java.io.File("creativeflow.db") // O la ruta que detectamos antes

        try {
            java.sql.DriverManager.getConnection("jdbc:sqlite:${dbFile.absolutePath}").use { conn ->
                val stmt = conn.prepareStatement("SELECT id, modulo_id, nombre, vista_id FROM modulos_secciones WHERE modulo_id = ? ORDER BY orden")
                stmt.setInt(1, moduloId)
                val rs = stmt.executeQuery()

                while (rs.next()) {
                    lista.add(
                        ModuloSeccionModel(
                            id = rs.getInt("id"),
                            moduloId = rs.getInt("modulo_id"),
                            nombre = rs.getString("nombre") ?: "",
                            vistaId = rs.getString("vista_id") ?: ""
                        )
                    )
                }
            }
        } catch (e: Exception) {
            println("❌ Error al cargar secciones: ${e.message}")
        }
        return lista
    }
}