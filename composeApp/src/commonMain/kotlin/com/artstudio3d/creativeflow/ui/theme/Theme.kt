package com.artstudio3d.creativeflow.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable

val CreativeFlowDarkColorScheme = darkColorScheme(
    primary = OrangePrimary,
    onPrimary = White,
    background = BlueGray,
    surface = DarkPetrol,
    onBackground = BlueGray,
    onSurface = LightGray,
    secondary = LightGray,
)

@Composable
fun CreativeFlowTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = CreativeFlowDarkColorScheme,
        content = content
    )
}