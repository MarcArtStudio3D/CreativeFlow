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
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.wrapContentWidth
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.Color
import com.artstudio3d.creativeflow.database.DatabaseManager
import com.artstudio3d.creativeflow.ui.components.CFButtonText


// Imports del tema y el botón con la ruta correcta
import com.artstudio3d.creativeflow.ui.theme.CreativeFlowTheme
import com.artstudio3d.creativeflow.ui.components.CFNativeButton
import com.artstudio3d.creativeflow.ui.theme.BlueGray
import org.jetbrains.compose.ui.tooling.preview.Preview

fun main() = application {

    //Inicializamos la base de datos
    DatabaseManager.init()
    Window(
        onCloseRequest = ::exitApplication,
        title = "CreativeFlow ERP",
        state = WindowState(width = 1080.dp, height = 700.dp)
    ) {
        // Envolvemos todo con nuestro Tema
        CreativeFlowTheme {
            // Surface toma el color DarkPetrol del tema
            Surface(color = MaterialTheme.colorScheme.background) {
                MainCreativeFlowUI()
            }
        }
    }
}

@Composable
@Preview
fun MainCreativeFlowUI() {
    val spacing = 2.dp
    val buttonWidth = 150.dp
    val sidebarBackgroundColor = BlueGray
    MaterialTheme {
        Column(
            horizontalAlignment = Alignment.Start,
            modifier = Modifier
                .background(sidebarBackgroundColor)
                .fillMaxHeight()
                .wrapContentWidth()

                //.fillMaxSize()
        ) {
            CFButtonText(
                text = "Proyectos",
                buttonWidth = buttonWidth, // Ancho personalizado
                modifier = Modifier.padding(6.dp)
            )
            CFButtonText(
                text = "Clientes",
                buttonWidth = buttonWidth, // Ancho personalizado
                modifier = Modifier.padding(6.dp)
            )
            CFButtonText(
                text = "Facturación",
                buttonWidth = buttonWidth, // Ancho personalizado
                modifier = Modifier.padding(6.dp)
            )
        }
    }
}