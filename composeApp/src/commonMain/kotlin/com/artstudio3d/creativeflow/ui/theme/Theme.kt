package com.artstudio3d.creativeflow.ui.theme

import androidx.compose.material.darkColors
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import com.artstudio3d.creativeflow.ui.theme.*
import com.artstudio3d.creativeflow.ui.theme.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = NaranjaPrincipal,
    onPrimary = BlancoPuro,
    // Esto cambiará el color de fondo de la TopBar y superficies elevadas
    primaryContainer = AzulPetroleo,
    onPrimaryContainer = NaranjaPrincipal,

    secondary = GrisClaro,
    onSecondary = AzulPetroleo,

    background = AzulPetroleo, // El fondo de la pantalla (ahora blanco)
    onBackground = BlancoPuro,

    surface = AzulPetroleo,
    onSurface = BlancoPuro,

    // Las Cards usan esto por defecto. Pongamos un azul un poco más claro para que resalten
    surfaceVariant = Color(0xFF243443),
    onSurfaceVariant = GrisClaro,

    // Este suele ser el color de la TopBar en M3 si no se especifica
    surfaceContainer = AzulPetroleo
)

@Composable
fun ArtStudioTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DarkColorScheme, // ¡Aquí está el cambio clave!
        typography = Typography,       // Asegúrate de que sea androidx.compose.material3.Typography
        content = content
    )
}