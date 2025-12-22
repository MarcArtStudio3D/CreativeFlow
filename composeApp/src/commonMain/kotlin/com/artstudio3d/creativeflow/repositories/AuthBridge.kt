package com.artstudio3d.creativeflow.repositories


expect object AuthGateway {
    fun login(user: String, pass: String): Boolean
    fun loadPermissions(user: String): List<UserPermission>
}