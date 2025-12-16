package com.artstudio3d.creativeflow

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import androidx.compose.material3.MaterialTheme
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.WindowState
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.padding
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.ui.graphics.Color



// Imports del tema y el botón con la ruta correcta
import com.artstudio3d.creativeflow.ui.theme.CreativeFlowTheme
import com.artstudio3d.creativeflow.ui.components.CFNativeButton
import com.artstudio3d.creativeflow.ui.theme.BlueGray

fun main() = application {
    Window(
        onCloseRequest = ::exitApplication,
        title = "CreativeFlow ERP",
        state = WindowState(width = 300.dp, height = 700.dp)
    ) {
        // Envolvemos todo con nuestro Tema
        CreativeFlowTheme {
            // Surface toma el color DarkPetrol del tema
            Surface(color = MaterialTheme.colorScheme.background) {
                TestCreativeFlowUI()
            }
        }
    }
}

@Composable
fun TestCreativeFlowUI() {
    val spacing = 2.dp
    val buttonWidth = 150.dp
    val sidebarBackgroundColor = BlueGray
    Column(
        modifier = Modifier
            .background(sidebarBackgroundColor)
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(spacing),

    ) {
        // Botón Activo (Naranja)

        CFNativeButton(
            text = "Proyectos",
            buttonWidth = buttonWidth, // Ancho personalizado
            onClick = { println("Navegar a Proyectos") },
            isActive = true,
            modifier = Modifier.padding(bottom = spacing)
        )
        // ESPACIADOR: Separación de 8dp
        Spacer(modifier = Modifier.height(spacing))
        // Botón Inactivo (Azul Petróleo)
        CFNativeButton(
            text = "Ventas",
            buttonWidth = buttonWidth, // Ancho personalizado
            onClick = { println("Navegar a Ventas") },
            isActive = false,
            modifier = Modifier.padding(bottom = spacing)
        )
        // ESPACIADOR: Separación de 8dp
        Spacer(modifier = Modifier.height(spacing))
        // Otro botón Inactivo
        CFNativeButton(
            text = "Facturación",
            buttonWidth = buttonWidth, // Ancho personalizado
            onClick = { println("Navegar a Facturación") },
            isActive = false,
            modifier = Modifier.padding(bottom = spacing)
        )
    }
}