package com.artstudio3d.creativeflow.repositories

import com.artstudio3d.creativeflow.models.EmpresaModel
import com.artstudio3d.creativeflow.models.ModuloModel
import com.artstudio3d.creativeflow.models.ModuloSeccionModel

expect object ModuloRepository {
    fun obtenerModulosPadre(): List<ModuloModel>
    fun obtenerSecciones(moduloId: Int): List<ModuloSeccionModel>

    fun obtenerEmpresas(): List<EmpresaModel>
}
