package com.artstudio3d.creativeflow.session

object AppSession {
    var usuarioLogueado: String? = null
    var rolActual: String? = null
    var empresaActiva: String = "ArtStudio 3D"
    var ejercicio: Int = 2025

    // Aquí podrías guardar la lista de permisos para no volver a consultar la DB
    var permisos: List<com.artstudio3d.creativeflow.repositories.UserPermission> = emptyList()

    fun logout() {
        usuarioLogueado = null
        rolActual = null
        permisos = emptyList()
    }
}