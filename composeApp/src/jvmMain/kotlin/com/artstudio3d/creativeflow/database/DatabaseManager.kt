package com.artstudio3d.creativeflow.database

import org.jetbrains.exposed.sql.*
import org.jetbrains.exposed.sql.transactions.transaction
import java.io.File
// Este es el que hace que insertAndGetId funcione:
import org.jetbrains.exposed.sql.insertAndGetId
import org.jetbrains.exposed.sql.insert  // <--- ESTE ES EL CRÍTICO
import org.jetbrains.exposed.sql.SqlExpressionBuilder.eq

object DatabaseManager {
    fun init() {
        val dbFile = File("creativeflow.db")
        Database.connect("jdbc:sqlite:${dbFile.absolutePath}", "org.sqlite.JDBC")

        transaction {
            addLogger(StdOutSqlLogger)

            // 1. Creamos las tablas (en orden de dependencia)
            SchemaUtils.create(
                ModulosPadreTable,
                SeccionesTable,
                RolesTable,
                UsuariosTable,
                UsuarioRolesTable,
                PermisosTable,
                EmpresasTable
            )

            // 2. Poblamos los datos iniciales si la tabla de usuarios está vacía
            if (UsuariosTable.selectAll().empty()) {
                seedDatabase()
            }
        }
    }

    private fun seedDatabase() {
        // A. CREAR MÓDULOS PADRE (Apps)
        val idVentas = ModulosPadreTable.insertAndGetId { it[nombre] = "Ventas" }
        val idProyectos = ModulosPadreTable.insertAndGetId { it[nombre] = "Proyectos" }

        // B. CREAR SECCIONES (Submódulos)
        val idArticulos = SeccionesTable.insertAndGetId {
            it[nombre] = "Articulos"
            it[moduloPadreId] = idVentas.value
        }
        val idClientes = SeccionesTable.insertAndGetId {
            it[nombre] = "Clientes"
            it[moduloPadreId] = idVentas.value
        }
        val idGestionProyectos = SeccionesTable.insertAndGetId {
            it[nombre] = "Pipeline"
            it[moduloPadreId] = idProyectos.value
        }

        // C. CREAR ROL SUPERADMIN
        val idRolAdmin = RolesTable.insertAndGetId { it[nombre] = "SuperAdmin" }

        // D. ASIGNAR PERMISOS TOTALES AL ROL ADMIN
        // 'unaSeccionId' es el nombre que le damos a la variable del bucle
        listOf(idArticulos, idClientes, idGestionProyectos).forEach { unaSeccionId ->

            // 'fila' es el nombre que le damos a la fila de la base de datos
            PermisosTable.insert { fila ->
                fila[PermisosTable.rolId] = idRolAdmin
                fila[PermisosTable.seccionId] = unaSeccionId
                fila[PermisosTable.puedeLeer] = true
                fila[PermisosTable.puedeCrear] = true
                fila[PermisosTable.puedeEditar] = true
                fila[PermisosTable.puedeBorrar] = true
            }
        }

        // E. CREAR EL USUARIO ADMINISTRADOR
        val idUsuario = UsuariosTable.insertAndGetId {
            it[nombre] = "admin.artstudio"
            it[contrasenaHash] = SecurityUtils.hashPassword("admin123")
            it[activo] = true
        }

        // F. VINCULAR USUARIO CON ROL
        UsuarioRolesTable.insert { fila->
            fila[usuarioId] = idUsuario.value
            fila[rolId] = idRolAdmin.value
        }

        println("🌱 Base de datos poblada con éxito: Usuario 'admin.artstudio' listo.")
    }
    fun validarLogin(usuarioInput: String, passwordInput: String): Boolean {
        return transaction {
            // Buscamos al usuario por su nombre (ej: admin.artstudio)
            val userRow = UsuariosTable
                .selectAll()
                .where { (UsuariosTable.nombre eq usuarioInput) and (UsuariosTable.activo eq true) }
                .singleOrNull()

            if (userRow != null) {
                val hashGuardado = userRow[UsuariosTable.contrasenaHash]
                // Generamos el hash de lo que el usuario escribió y comparamos
                val hashInput = SecurityUtils.hashPassword(passwordInput)

                return@transaction hashInput == hashGuardado
            }

            false // Usuario no encontrado o inactivo
        }
    }
    
    fun obtenerPermisosUsuario(userName: String) {
    transaction {
        // Hacemos el JOIN de las 5 tablas involucradas
        // Usuarios -> UsuarioRoles -> Roles -> Permisos -> Secciones
        val query = (UsuariosTable innerJoin UsuarioRolesTable innerJoin RolesTable innerJoin PermisosTable innerJoin SeccionesTable)
            .select(SeccionesTable.nombre, PermisosTable.puedeLeer, PermisosTable.puedeEditar)
            .where { UsuariosTable.nombre eq userName }

        println("\n--- PERMISOS PARA: $userName ---")
        query.forEach { row ->
            val seccion = row[SeccionesTable.nombre]
            val leer = if (row[PermisosTable.puedeLeer]) "SÍ" else "NO"
            val editar = if (row[PermisosTable.puedeEditar]) "SÍ" else "NO"
            
            println("Sección: $seccion | Leer: $leer | Editar: $editar")
        }
        println("----------------------------------\n")
    }
}
}