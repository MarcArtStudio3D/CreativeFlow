package com.artstudio3d.creativeflow.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp

import com.artstudio3d.creativeflow.session.AppSession

// Para que 'seleccionado' (mutableStateOf/remember) funcione
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember

// Para que 'MaterialTheme.colorScheme' funcione
import androidx.compose.material3.MaterialTheme


// Para usar modificadores como Modifier.fillMaxSize() o background

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.background

@Composable
fun MainDashboard(onLogout: () -> Unit) {
    // Estado para saber qué módulo padre está seleccionado en el Sidebar
    var moduloSeleccionado by remember { mutableStateOf<Int?>(null) }
    var seccionSeleccionada by remember { mutableStateOf("Lista") }

    Row(modifier = Modifier.fillMaxSize()) {

        // 1. SIDEBAR (Izquierda) - Los Módulos Padre
        Surface(
            modifier = Modifier.width(100.dp).fillMaxHeight(), // Más estrecho para iconos de módulo
            color = MaterialTheme.colorScheme.primaryContainer,
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                // Aquí iteraríamos sobre los ModulosPadreTable de tu SQLite
                ModuloIcon(nombre = "Prod",
                    seleccionado = moduloSeleccionado == 1,
                    onClick = { moduloSeleccionado = 1 })
                ModuloIcon(nombre = "Assets",
                    seleccionado = moduloSeleccionado == 2,
                    onClick = { moduloSeleccionado = 2 })
                ModuloIcon(nombre = "Admin",
                    seleccionado = moduloSeleccionado == 3,
                    onClick = { moduloSeleccionado = 3 })
            }
        }

        // El resto de la pantalla se organiza verticalmente
        Column(modifier = Modifier.fillMaxSize()) {

            // 2. TOP BAR - Secciones del módulo seleccionado
            Surface(
                modifier = Modifier.fillMaxWidth().height(60.dp),
                elevation = 4.dp,
                color = MaterialTheme.colorScheme.surface
            ) {
                Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.padding(horizontal = 16.dp)) {
                    // Aquí aparecerían los botones de las secciones (ej: "Artículos", "Clientes")
                    // Solo las que pertenezcan al módulo seleccionado y el usuario tenga permiso
                    Text("Secciones: ", fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.onSurface)
                    SeccionButton(
                        "Lista",
                        seleccionado = seccionSeleccionada == "Lista",
                        onClick = { seccionSeleccionada = "Lista"} )
                    SeccionButton(
                        texto = "Calendario",
                        seleccionado = seccionSeleccionada == "Calendario",
                        onClick = { seccionSeleccionada = "Calendario" } )
                }
            }

            // 4. CONTENT AREA - El corazón de la App (MariaDB)
            Box(modifier = Modifier.weight(1f).fillMaxWidth().padding(16.dp)) {
                // Aquí irá el contenido dinámico
                Text("Área de Trabajo - Datos de MariaDB")
            }

            // 3. BOTTOM BAR - Info y Sesión
            Surface(
                modifier = Modifier.fillMaxWidth().height(40.dp),
                color = Color.LightGray.copy(alpha = 0.3f)
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 16.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Text("Usuario: ${AppSession.usuarioLogueado}", style = MaterialTheme.typography.labelMedium)
                    Text("Empresa: Artstudio3D VFX", style = MaterialTheme.typography.labelMedium)

                    TextButton(onClick = { onLogout() }) {
                        Text("Cerrar Sesión", color = Color.Red, style = MaterialTheme.typography.labelMedium)
                    }
                }
            }
        }
    }
}
@Composable
fun ModuloIcon(nombre: String, seleccionado: Boolean, onClick: () -> Unit) {
    val colorIcono = if (seleccionado)
        MaterialTheme.colorScheme.primary
    else
        MaterialTheme.colorScheme.secondary
    IconButton(
        onClick = onClick,
        modifier = Modifier.padding(8.dp).size(60.dp)
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            // Usamos un icono genérico por ahora, luego lo haremos dinámico
            Icon(
                imageVector = Icons.Default.GridView,
                contentDescription = nombre,
                tint = Color.White
            )
            Text(
                text = nombre,
                color = Color.White,
                style = MaterialTheme.typography.labelSmall
            )
        }
    }
}
@Composable
fun SeccionButton(
    texto: String,
    seleccionado: Boolean,
    onClick: () -> Unit
) {
    TextButton(
        onClick = onClick,
        colors = ButtonDefaults.textButtonColors(
            contentColor = if (seleccionado)
                MaterialTheme.colorScheme.primary
            else
                MaterialTheme.colorScheme.onSurface.copy(alpha = 0.6f)
        )
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Text(
                text = texto,
                style = MaterialTheme.typography.labelLarge,
                fontWeight = if (seleccionado) FontWeight.Bold else FontWeight.Normal
            )
            // Una barrita naranja debajo si está seleccionado
            if (seleccionado) {
                Box(
                    Modifier
                        .width(20.dp)
                        .height(2.dp)
                        .background(MaterialTheme.colorScheme.primary)
                )
            }
        }
    }
}