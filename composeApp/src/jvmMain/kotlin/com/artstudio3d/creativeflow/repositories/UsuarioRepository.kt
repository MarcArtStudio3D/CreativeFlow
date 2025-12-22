package com.artstudio3d.creativeflow.repositories
import org.jetbrains.exposed.sql.*
import org.jetbrains.exposed.sql.transactions.transaction
import com.artstudio3d.creativeflow.database.UsuariosTable // Asegúrate que el nombre coincida con tu tabla
import com.artstudio3d.creativeflow.database.SeccionesTable
import com.artstudio3d.creativeflow.database.PermisosTable

import com.artstudio3d.creativeflow.database.SecurityUtils
import com.artstudio3d.creativeflow.database.UsuarioRolesTable

object UsuarioRepository {

    /**
     * Valida si el usuario existe y la contraseña coincide.
     * Aquí podrías usar tu SecurityUtils para hashear la pass.
     */
    fun validarLogin(user: String, pass: String): Boolean {
        val passwordHasheada = SecurityUtils.hashPassword(pass)
        return transaction {
            // Ejemplo simple: busca un usuario que coincida
            val usuario = UsuariosTable
                .selectAll().where { (UsuariosTable.nombre eq user) and (UsuariosTable.contrasenaHash eq passwordHasheada) }
                .singleOrNull()

            usuario != null
        }
    }

    /**
     * Carga los permisos de la base de datos y los convierte
     * a nuestra data class de CommonMain.
     */
    fun getPermissions(userName: String): List<UserPermission> {
        return transaction {
            // 1. Unimos las 4 tablas necesarias siguiendo la cadena de relaciones
            val query = (UsuariosTable
                    innerJoin UsuarioRolesTable) // Vincula Usuario con su Rol
                .innerJoin(PermisosTable, { UsuarioRolesTable.rolId }, { PermisosTable.rolId }) // Vincula Rol con sus Permisos
                .innerJoin(SeccionesTable, { PermisosTable.seccionId }, { SeccionesTable.id }) // Vincula Permiso con la Sección

                .select(SeccionesTable.nombre, PermisosTable.puedeLeer, PermisosTable.puedeEditar)
                .where { UsuariosTable.nombre eq userName }

            query.map {
                UserPermission(
                    section = it[SeccionesTable.nombre],
                    canRead = it[PermisosTable.puedeLeer],
                    canEdit = it[PermisosTable.puedeEditar]
                )
            }
        }
    }
}