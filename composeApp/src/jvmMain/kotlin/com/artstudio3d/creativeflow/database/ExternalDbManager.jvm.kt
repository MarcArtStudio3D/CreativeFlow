package com.artstudio3d.creativeflow.database

import java.sql.Connection
import java.sql.DriverManager
import com.artstudio3d.creativeflow.models.EmpresaModel

actual object ExternalDbManager {
    private var connection: Connection? = null

    actual fun conectar(e: EmpresaModel): Boolean {
        return try {
            // Cerramos cualquier conexión abierta antes de cambiar de empresa
            connection?.takeIf { !it.isClosed }?.close()

            connection = when (e.motorDb.lowercase()) {
                "mariadb" -> {
                    val url = "jdbc:mariadb://${e.mariadbHost}:${e.mariadbPort}/${e.mariadbName}"
                    DriverManager.getConnection(url, e.mariadbUser, e.mariadbPassword)
                }
                "sqlite" -> {
                    // El path sería el valor de 'archivoSqlite'
                    DriverManager.getConnection("jdbc:sqlite:${e.archivoSqlite}")
                }
                "postgresql" -> {
                    val url = "jdbc:postgresql://${e.postgreHost}:${e.postgrePort}/${e.postgreName}"
                    DriverManager.getConnection(url, e.postgreUser, e.postgrePassword)
                }
                else -> throw Exception("Motor de base de datos no soportado: ${e.motorDb}")
            }

            connection != null
        } catch (ex: Exception) {
            println("❌ Error conectando a ${e.motorDb}: ${ex.message}")
            false
        }
    }

    actual fun obtenerConexion(): Connection {
        return connection?.takeIf { !it.isClosed }
            ?: throw Exception("No hay conexión activa a la base de datos de la empresa.")
    }
}