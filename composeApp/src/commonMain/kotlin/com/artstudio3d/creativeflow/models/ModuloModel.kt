package com.artstudio3d.creativeflow.models

import androidx.compose.ui.graphics.vector.ImageVector
import org.jetbrains.compose.resources.DrawableResource
import org.jetbrains.compose.resources.StringResource

data class ModuloModel(
    val id: Int,
    val titulo: StringResource,
    val descripcion: StringResource,
    val imagen: DrawableResource,
    val icono: ImageVector
)
