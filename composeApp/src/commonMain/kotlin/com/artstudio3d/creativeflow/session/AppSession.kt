package com.artstudio3d.creativeflow.session

import com.artstudio3d.creativeflow.models.EmpresaModel

object AppSession {
    // Datos de Usuario
    var usuarioLogueado: String? = null
    var rolActual: String? = null
    var permisos: List<com.artstudio3d.creativeflow.repositories.UserPermission> = emptyList()

    // Contexto de Empresa (Configuración Técnica)
    var empresaActivaId: Int? = null
    var nombreEmpresa: String = "ArtStudio 3D"
    var ejercicio: Int = 2025

    // Configuración de Cálculo y Formato
    var decimalesCalculos: Int = 2
    var decimalesPrecios: Int = 2
    var monedaLocal: String = "EUR"
    var conversionTiempoReal: Boolean = false
    var tamanoCodigoArticulo: Int = 13

    // Datos de la Conexión Activa (Opcional, para debug o reconexión)
    var hostMariaDB: String? = null
    var motorDb: String = "MariaDB"
    var archivoSqlite: String? = null
    var mariadbHost: String? = null
    var mariadbPort: String? = null
    var mariadbName: String? = null
    var mariadbUser: String? = null
    var mariadbPassword: String? = null
    var postgreHost: String? = null
    var postgreName: String? = null
    var postgreUser: String? = null
    var postgrePort: String? = null
    var postgrePassword: String? = null

    fun cargarEmpresa(empresa: EmpresaModel) {
        this.empresaActivaId = empresa.id
        this.nombreEmpresa = empresa.nombreComercial ?: empresa.nombreFiscal

        // Configuración técnica para cálculos
        this.decimalesCalculos = empresa.decimalesEnCalculos
        this.decimalesPrecios = empresa.decimalesPrecios
        this.tamanoCodigoArticulo = empresa.tamanoCodigoArticulo
        this.monedaLocal = empresa.idDivisa?.toString() ?: "EUR"
        this.conversionTiempoReal = empresa.actualizarDivisas

        // Guardamos el host para saber a dónde estamos conectados
        this.hostMariaDB = empresa.mariadbHost
        this.motorDb = empresa.motorDb
        this.archivoSqlite = empresa.archivoSqlite
        this.mariadbHost = empresa.mariadbHost
        this.mariadbPort = empresa.mariadbPort
        this.mariadbName = empresa.mariadbName
        this.mariadbUser = empresa.mariadbUser
        this.mariadbPassword = empresa.mariadbPassword
        this.postgreHost = empresa.postgreHost
        this.postgreName = empresa.postgreName
        this.postgreUser = empresa.postgreUser
        this.postgrePort = empresa.postgrePort
        this.postgrePassword = empresa.postgrePassword


        // Aquí podrías guardar la lista de permisos para no volver a consultar la DB
        var permisos: List<com.artstudio3d.creativeflow.repositories.UserPermission> = emptyList()
    }
    fun logout() {
        usuarioLogueado = null
        rolActual = null
        permisos = emptyList()
    }
}