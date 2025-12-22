package com.artstudio3d.creativeflow

import androidx.compose.runtime.*
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import androidx.compose.ui.window.rememberWindowState
import androidx.compose.ui.unit.dp
import com.artstudio3d.creativeflow.database.DatabaseManager
import com.artstudio3d.creativeflow.ui.LoginScreen // Tu pantalla en Common
import com.artstudio3d.creativeflow.ui.MainDashboard
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.remember
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.runtime.mutableStateOf
import com.artstudio3d.creativeflow.ui.theme.ArtStudioTheme
import com.artstudio3d.creativeflow.session.AppSession // Tu

fun main() = application {
    var showMainApp by remember { mutableStateOf(false) }
    //Inicializamos la base de datos
    DatabaseManager.init()
    Window(
        onCloseRequest = ::exitApplication,
        title = "CreativeFlow VFX Studio - Studio Management Tool",
        state = rememberWindowState(width = 1200.dp, height = 800.dp)
    ) {
        ArtStudioTheme {
            Surface(color = MaterialTheme.colorScheme.background) {
                if (!showMainApp) {
                    // Mostramos el Login de commonMain
                    LoginScreen(
                        onLoginSuccess = {
                            showMainApp = true
                        }
                    )
                } else {
                    MainDashboard(
                        onLogout = {
                            showMainApp = false
                        }
                    )
                }
            }
        }
    }
}

/*@Composable
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
}*/