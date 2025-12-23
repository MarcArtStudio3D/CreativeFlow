package com.artstudio3d.creativeflow.repositories

import com.artstudio3d.creativeflow.models.ModuloModel

expect object ModuloRepository {
    fun obtenerModulosPadre(): List<ModuloModel>
}
