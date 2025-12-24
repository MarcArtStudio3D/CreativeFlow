package com.artstudio3d.creativeflow.ui

import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.painter.Painter
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ImageNotSupported
import androidx.compose.ui.graphics.toComposeImageBitmap
import androidx.compose.ui.graphics.vector.rememberVectorPainter
import java.io.File
import org.jetbrains.skia.Image

@Composable
actual fun cargarImagenDesdeRuta(rutaRelativa: String): Painter {
    // 1. Intentamos localizar el archivo físico
    val carpetaIconos = "iconos_modulos"
    val archivo = File(carpetaIconos, rutaRelativa)

    // Definimos el icono de error por fuera para no repetir código
    val iconoError = rememberVectorPainter(Icons.Default.ImageNotSupported)

    return (if (archivo.exists()) {
        try {
            // Intentamos convertir el archivo en un Bitmap
// MÉTODO ACTUAL: Leer bytes y convertir a Image de Skia, luego a ImageBitmap de Compose
            val bytes = archivo.readBytes()
            val skiaImage = Image.makeFromEncoded(bytes)
            val bitmap = skiaImage.toComposeImageBitmap()
        } catch (e: Exception) {
            println("❌ Error al procesar el archivo: ${e.message}")
            iconoError // Retornamos el icono de error
        }
    } else {
        println("⚠️ Archivo no encontrado: ${archivo.absolutePath}")
        iconoError // Retornamos el icono de error
    }) as Painter
}