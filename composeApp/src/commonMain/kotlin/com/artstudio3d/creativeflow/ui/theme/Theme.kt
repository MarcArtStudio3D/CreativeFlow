package com.artstudio3d.creativeflow.ui.theme

import androidx.compose.material.darkColors
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import com.artstudio3d.creativeflow.ui.theme.*
import com.artstudio3d.creativeflow.ui.theme.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme

private val DarkColorScheme = darkColorScheme(
    primary = NaranjaPrincipal,
    onPrimary = BlancoPuro,
    secondary = GrisClaro,
    onSecondary = AzulPetroleo,
    background = AzulPetroleo,
    onBackground = BlancoPuro,
    surface = AzulPetroleo, // Color para contenedores como el Sidebar
    onSurface = BlancoPuro
)

@Composable
fun ArtStudioTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DarkColorScheme, // ¡Aquí está el cambio clave!
        typography = Typography,       // Asegúrate de que sea androidx.compose.material3.Typography
        content = content
    )
}