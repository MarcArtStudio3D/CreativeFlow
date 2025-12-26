// jvmMain/src/.../repositories/ModuloRepository.kt
package com.artstudio3d.creativeflow.repositories

import com.artstudio3d.creativeflow.models.EmpresaModel
import com.artstudio3d.creativeflow.models.ModuloModel
import com.artstudio3d.creativeflow.models.ModuloSeccionModel
import com.artstudio3d.creativeflow.database.ExternalDbManager
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
        val dbFile = java.io.File(System.getProperty("user.dir") + "/creativeflow.db")
        if (!dbFile.exists()) {
            println("⚠️ Error: No se encuentra creativeflow.db en ${dbFile.absolutePath}")
            return emptyList()
        }

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
    actual fun validarUsuarioEnConexionActiva(user: String, pass: String): Boolean {
        return try {
            // Usamos la conexión que el AuthService acaba de abrir
            val conn = ExternalDbManager.obtenerConexion()

            val sql = "SELECT COUNT(*) FROM usuarios WHERE username = ? AND password = ? AND activo = 1"

            conn.prepareStatement(sql).use { pstmt ->
                pstmt.setString(1, user)
                pstmt.setString(2, pass)

                val rs = pstmt.executeQuery()
                if (rs.next()) {
                    rs.getInt(1) > 0 // Si el conteo es mayor a 0, las credenciales son válidas
                } else {
                    false
                }
            }
        } catch (e: Exception) {
            println("❌ Error en validación MariaDB: ${e.message}")
            false
        }
    }
    actual fun obtenerEmpresas(): List<EmpresaModel> {
        val lista = mutableListOf<EmpresaModel>()
        val dbFile = java.io.File("creativeflow.db")

        try {
            java.sql.DriverManager.getConnection("jdbc:sqlite:${dbFile.absolutePath}").use { conn ->
                val rs = conn.createStatement().executeQuery("SELECT * FROM empresas")
                while (rs.next()) {
                    lista.add(
                        EmpresaModel(
                            id = rs.getInt("id"),
                            codigoEmpresa = rs.getString("codigoempresa") ?: "",
                            nombreComercial = rs.getString("nombre_comercial"),
                            nombreFiscal = rs.getString("nombre_fiscal") ?: "",
                            formaJuridica = rs.getString("forma_juridica") ?: "",
                            direccion = rs.getString("direccion") ?: "",
                            cp = rs.getString("cp"),
                            poblacion = rs.getString("poblacion"),
                            provincia = rs.getString("provincia"),
                            pais = rs.getString("pais") ?: "",
                            logoRuta = rs.getString("logo_ruta"),
                            cifSiren = rs.getString("cif_siren") ?: "",
                            siret = rs.getString("siret"),
                            apeNaf = rs.getString("ape_naf"),
                            rcs = rs.getString("rcs"),
                            ciudadRcs = rs.getString("cuidad_rcs"),
                            inscripcion = rs.getString("inscripcion"),
                            telefono1 = rs.getString("telefono1"),
                            telefono2 = rs.getString("telefono2"),
                            movil = rs.getString("movil"),
                            email = rs.getString("email"),
                            web = rs.getString("web"),
                            enlaceWeb = rs.getInt("enlace_web") == 1,
                            gestionInternacional = rs.getInt("gestion_internacional") == 1,
                            fechaAlta = rs.getString("fecha_alta"),
                            diaCierreEjercicio = rs.getInt("dia_cierre_ejercicio"),
                            mesCierreEjercicio = rs.getInt("mes_cierre_ejercicio"),
                            autocodificarNuevosArticulos = rs.getInt("autocodificar_nuevos_articulos") == 1,
                            tamanoCodigoArticulo = rs.getInt("tamano_codigo_articulo"),
                            irpf = rs.getInt("irpf") == 1,
                            porcentajeIrpf = rs.getDouble("porcentaje_irpf"),
                            idTarifa = rs.getInt("id_tarifa"),
                            margenArticulos = rs.getDouble("margen_articulos"),
                            margenMinimoArticulo = rs.getDouble("margen_minimo_articulo"),
                            actualizarDivisas = rs.getInt("actualizar_divisas") == 1,
                            idDivisa = rs.getInt("id_divisa"),
                            digitosFactura = rs.getInt("digitos_factura"),
                            serieFactura = rs.getString("serie_factura") ?: "F-",
                            decimalesEnCalculos = rs.getInt("decimales_en_calculos"),
                            decimalesPrecios = rs.getInt("decimales_precios"),
                            comentariosAlbaran = rs.getString("comentarios_albaran"),
                            comentariosContratoServicio = rs.getString("comentarios_contrato_servicio"),
                            comentariosFacturas = rs.getString("comentarios_facturas"),
                            horariosLunes = rs.getString("horarios_lunes"),
                            horariosMartes = rs.getString("horarios_martes"),
                            horariosMiercoles = rs.getString("horarios_miercoles"),
                            horariosJueves = rs.getString("horarios_jueves"),
                            horariosViernes = rs.getString("horarios_viernes"),
                            horariosSabado = rs.getString("horarios_sabado"),
                            horariosDomingo = rs.getString("horarios_domingo"),
                            googleId = rs.getString("google_id"),
                            googleEmail = rs.getString("google_email"),
                            googleAccessToken = rs.getString("google_access_token"),
                            googleRefreshToken = rs.getString("google_refresh_token"),
                            googleTokenExpiresAt = rs.getString("google_token_expires_at"),
                            googleCalendarId = rs.getString("google_calendar_id"),
                            googleLastSyncToken = rs.getString("google_last_sync_token"),
                            cuentaClientes = rs.getString("cuenta_clientes"),
                            cuentaProveedores = rs.getString("cuenta_proveedores"),
                            cuentaVentaMercaderias = rs.getString("cuenta_venta_mercaderias"),
                            cuentaVentaServicios = rs.getString("cuenta_venta_servicios"),
                            cuentaIvaSoportadoN = rs.getString("cuenta_iva_soportado_n"),
                            cuentaIvaSoportadoR = rs.getString("cuenta_iva_soportado_r"),
                            cuentaIvaSoportadoSr = rs.getString("cuenta_iva_soportado_sr"),
                            cuentaIvaSoportadoE = rs.getString("cuenta_iva_soportado_e"),
                            cuentaIvaSoportadoReN = rs.getString("cuenta_iva_soportado_re_n"),
                            cuentaIvaSoportadoReR = rs.getString("cuenta_iva_soportado_re_r"),
                            cuentaIvaSoportadoReSr = rs.getString("cuenta_iva_soportado_re_sr"),
                            cuentaIvaSoportadoReE = rs.getString("cuenta_iva_soportado_re_e"),
                            cuentaIvaRepercutidoN = rs.getString("cuenta_iva_repercutido_n"),
                            cuentaIvaRepercutidoR = rs.getString("cuenta_iva_repercutido_r"),
                            cuentaIvaRepercutidoSr = rs.getString("cuenta_iva_repercutido_sr"),
                            cuentaIvaRepercutidoE = rs.getString("cuenta_iva_repercutido_e"),
                            cuentaIvaRepercutidoReN = rs.getString("cuenta_iva_repercutido_re_n"),
                            cuentaIvaRepercutidoReR = rs.getString("cuenta_iva_repercutido_re_r"),
                            cuentaIvaRepercutidoReSr = rs.getString("cuenta_iva_repercutido_re_sr"),
                            cuentaIvaRepercutidoReE = rs.getString("cuenta_iva_repercutido_re_e"),
                            motorDb = rs.getString("motordb") ?: "MariaDB",
                            archivoSqlite = rs.getString("archivo_sqlite"),
                            mariadbHost = rs.getString("mariadb_host"),
                            mariadbPort = rs.getString("mariadb_port"),
                            mariadbName = rs.getString("mariadb_name"),
                            mariadbUser = rs.getString("mariadb_user"),
                            mariadbPassword = rs.getString("mariadb_password"),
                            postgreHost = rs.getString("postgre_host"),
                            postgreName = rs.getString("postgre_name"),
                            postgreUser = rs.getString("postgre_user"),
                            postgrePort = rs.getString("postgre_port"),
                            postgrePassword = rs.getString("postgre_password")
                        )
                    )
                }
            }
        } catch (e: Exception) {
            println("❌ Error crítico leyendo empresas: ${e.message}")
        }
        return lista
    }
    actual fun guardarNuevaEmpresa(empresa: EmpresaModel): Result<Unit> {
        return try {
            val dbFile = java.io.File("creativeflow.db")
            DriverManager.getConnection("jdbc:sqlite:${dbFile.absolutePath}").use { conn ->
                val sql = """
                INSERT INTO empresas (nombre_comercial, motordb, archivo_sqlite, mariadb_host, ...) 
                VALUES (?, ?, ?, ?, ...)
            """.trimIndent()

                // 1. Guardar en el índice local
                val pstmt = conn.prepareStatement(sql)
                pstmt.setString(1, empresa.nombreComercial)
                pstmt.setString(2, empresa.motorDb)
                // ... resto de parámetros
                pstmt.executeUpdate()

                // 2. Inicializar la base de datos de destino
                inicializarTablasEmpresa(empresa)

                Result.success(Unit)
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}