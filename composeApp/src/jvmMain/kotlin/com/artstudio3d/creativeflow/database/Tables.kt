package com.artstudio3d.creativeflow.database

import org.jetbrains.exposed.dao.id.IntIdTable // IMPORTANTE: Nueva herencia

object UsuariosTable : IntIdTable("usuarios") {
    val nombre = varchar("nombre", 100).uniqueIndex()
    val emailEncriptado = varchar("email_encriptado", 255).nullable()
    val contrasenaHash = varchar("contrasena_hash", 256)
    val activo = bool("activo").default(true)
}

object RolesTable : IntIdTable("roles") {
    val nombre = varchar("nombre", 50).uniqueIndex()
}

object UsuarioRolesTable : IntIdTable("usuario_roles") {
    val usuarioId = reference("usuario_id", UsuariosTable)
    val rolId = reference("rol_id", RolesTable)
}

object ModulosPadreTable : IntIdTable("modulos_padre") {
    val nombre = varchar("nombre", 50)
    val icono = varchar("icono", 50).nullable()
}

object SeccionesTable : IntIdTable("secciones") {
    val nombre = varchar("nombre", 50)
    val moduloPadreId = reference("modulo_padre_id", ModulosPadreTable)
}

object PermisosTable : IntIdTable("permisos") {
    val rolId = reference("rol_id", RolesTable)
    val seccionId = reference("seccion_id", SeccionesTable)
    val puedeLeer = bool("puede_leer").default(true)
    val puedeCrear = bool("puede_crear").default(false)
    val puedeEditar = bool("puede_editar").default(false)
    val puedeBorrar = bool("puede_borrar").default(false)
}

object EmpresasTable : IntIdTable("empresas") {
    val razonSocial = varchar("razon_social", 200)
    val cifEncriptado = varchar("cif_encriptado", 255)
    val direccion = varchar("direccion", 255)
}