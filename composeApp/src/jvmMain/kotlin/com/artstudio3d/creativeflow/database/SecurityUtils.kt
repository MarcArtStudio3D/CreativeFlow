package com.artstudio3d.creativeflow.database

object SecurityUtils {
    // Esta es la función que te pide el punto E
    fun hashPassword(password: String): String {
        return java.security.MessageDigest.getInstance("SHA-256")
            .digest(password.toByteArray())
            .joinToString("") { "%02x".format(it) }
    }

    // Funciones para encriptar/desencriptar CIF y Email (opcional por ahora, pero útil)
    fun encrypt(value: String): String = value // Por ahora puedes dejarlas así de simples
    fun decrypt(value: String): String = value
}