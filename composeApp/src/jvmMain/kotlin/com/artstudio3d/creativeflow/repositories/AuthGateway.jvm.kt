package com.artstudio3d.creativeflow.repositories

actual object AuthGateway {
    actual fun login(user: String, pass: String): Boolean {
        // Aquí llamamos a lo que ya tienes en jvmMain
        return UsuarioRepository.validarLogin(user, pass)
    }

    actual fun loadPermissions(user: String): List<UserPermission> {
        // Aquí llamamos a tu lógica de base de datos
        return UsuarioRepository.getPermissions(user)
    }
}