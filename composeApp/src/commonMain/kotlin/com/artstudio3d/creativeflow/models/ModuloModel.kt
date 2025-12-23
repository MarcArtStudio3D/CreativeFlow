package com.artstudio3d.creativeflow.models

data class ModuloModel(
    val id: Int,
    val nombre: String,        // Cambiamos StringResource por String
    val descripcion: String,   // Cambiamos StringResource por String
    val icono: String    // Guardamos el nombre del recurso, ej: "Projects"
)
