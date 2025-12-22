package com.artstudio3d.creativeflow.repositories

/**
 * Esta es la "mochila" donde metemos los datos de PermisosTable
 * para llevarlos de la base de datos a la pantalla.
 */
data class UserPermission(
    val section: String,
    val canRead: Boolean,
    val canEdit: Boolean
)