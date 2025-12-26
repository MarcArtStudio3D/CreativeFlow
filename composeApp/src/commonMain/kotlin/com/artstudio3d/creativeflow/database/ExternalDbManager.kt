package com.artstudio3d.creativeflow.database
// commonMain/.../database/ExternalDbManager.kt


import com.artstudio3d.creativeflow.models.EmpresaModel
import java.sql.Connection

expect object ExternalDbManager {
    fun conectar(e: EmpresaModel): Boolean

    fun obtenerConexion(): Connection
    // No ponemos obtenerConexion() aquí porque devuelve un objeto de Java (Connection)
    // y commonMain no sabe qué es eso.
}