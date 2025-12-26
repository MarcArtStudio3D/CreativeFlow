package com.artstudio3d.creativeflow.services
import com.artstudio3d.creativeflow.database.ExternalDbManager
import com.artstudio3d.creativeflow.models.EmpresaModel
import com.artstudio3d.creativeflow.repositories.ModuloRepository
import com.artstudio3d.creativeflow.session.AppSession

object AuthService {
    /**
     * Orquesta el proceso de entrada a la aplicación.
     * Retorna un Result con éxito o el mensaje de error.
     */
    fun login(empresa: EmpresaModel?, user: String, pass: String): Result<Unit> {
        println("🚀 Iniciando proceso de login para: $user") // LOG
        if (empresa == null) return Result.failure(Exception("Seleccione empresa"))

        // 1. Intentamos la conexión técnica (JDBC)
        // Aquí usa las credenciales de 'root/admin' guardadas en el SQLite central
        val exitoConexion = ExternalDbManager.conectar(empresa)
        println("🔗 Conexión a ${empresa.motorDb}: $exitoConexion") // LOG
        if (!exitoConexion) {
            return Result.failure(Exception("Error de red: No se pudo alcanzar el servidor ${empresa.motorDb}"))
        }

        // 2. Una vez dentro de esa base de datos, buscamos al usuario de la aplicación
        // Esta función está en ModuloRepository y usa ExternalDbManager.obtenerConexion()
        val usuarioValido = ModuloRepository.validarUsuarioEnConexionActiva(user, pass)
        println("👤 Validación de usuario: $usuarioValido") // LOG

        return if (usuarioValido) {
            AppSession.cargarEmpresa(empresa)
            AppSession.usuarioLogueado = user
            Result.success(Unit)
        } else {
            Result.failure(Exception("Usuario o contraseña inválidos para ${empresa.nombreComercial}"))
        }
    }
}


