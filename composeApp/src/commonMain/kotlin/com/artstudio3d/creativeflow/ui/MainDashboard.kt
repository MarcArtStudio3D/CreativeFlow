package com.artstudio3d.creativeflow.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.artstudio3d.creativeflow.session.AppSession
import com.artstudio3d.creativeflow.ui.components.ModuloCard
import creativeflow.composeapp.generated.resources.Projects
import creativeflow.composeapp.generated.resources.Res
import org.jetbrains.compose.resources.painterResource

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MainDashboard(onLogout: () -> Unit) {
    // 1. ESTADOS
    var moduloSeleccionado by remember { mutableStateOf<Int?>(null) }

    val modulos = listOf(
        Pair(1, "Proyectos"),
        Pair(2, "Ventas"),
        Pair(3, "Administración")
    )

    Scaffold(
        containerColor = MaterialTheme.colorScheme.background,
        topBar = {
            TopAppBar(
                title = { Text("CreativeFlow - ArtStudio3D", style = MaterialTheme.typography.titleMedium) },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.surface,
                    titleContentColor = MaterialTheme.colorScheme.primary
                ),
                navigationIcon = {
                    if (moduloSeleccionado != null) {
                        IconButton(onClick = { moduloSeleccionado = null }) {
                            Icon(Icons.Default.Apps, contentDescription = null)
                        }
                    }
                }
            )
        },
        bottomBar = {
            Surface(color = MaterialTheme.colorScheme.surface) {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 8.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Text("Usuario: ${AppSession.usuarioLogueado}", color = MaterialTheme.colorScheme.onSurface)
                    TextButton(onClick = onLogout) {
                        Text("Cerrar Sesión", color = Color.Red)
                    }
                }
            }
        }
    ) { paddingValues ->
        Row(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .background(MaterialTheme.colorScheme.background)
        ) {
            // SIDEBAR
            Surface(
                modifier = Modifier.width(260.dp).fillMaxHeight(),
                color = MaterialTheme.colorScheme.surface,
                tonalElevation = 2.dp
            ) {
                if (moduloSeleccionado == null) {
                    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                        Text("Selecciona un módulo", style = MaterialTheme.typography.bodySmall)
                    }
                } else {
                    Column(modifier = Modifier.padding(12.dp)) {
                        Text("Módulo Activo", fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
                        Spacer(Modifier.height(20.dp))
                        Text("Secciones aquí...", color = MaterialTheme.colorScheme.onSurfaceVariant)
                    }
                }
            }

            // CONTENT AREA
            Box(modifier = Modifier.weight(1f).fillMaxSize().padding(24.dp)) {
                if (moduloSeleccionado == null) {
                    LazyVerticalGrid(
                        columns = GridCells.Adaptive(minSize = 280.dp),
                        horizontalArrangement = Arrangement.spacedBy(24.dp),
                        verticalArrangement = Arrangement.spacedBy(24.dp)
                    ) {
                        items(modulos) { modulo ->
                            ModuloCard(
                                titulo = modulo.second,
                                descripcion = "Gestión de ${modulo.second}",
                                imagenPainter = painterResource(Res.drawable.Projects),
                                seleccionado = false,
                                onClick = { moduloSeleccionado = modulo.first }
                            )
                        }
                    }
                } else {
                    Column {
                        Text("Panel de Trabajo", style = MaterialTheme.typography.headlineMedium)
                        Text("Módulo: ${modulos.find { it.first == moduloSeleccionado }?.second}")
                    }
                }
            }
        }
    }
}

@Composable
fun SeccionButton(
    texto: String,
    icono: ImageVector,
    seleccionado: Boolean,
    onClick: () -> Unit
) {
    FilterChip(
        selected = seleccionado,
        onClick = onClick,
        leadingIcon = {
            Icon(
                imageVector = icono,
                contentDescription = null,
                modifier = Modifier.size(18.dp)
            )
        },
        label = { Text(texto) },
        modifier = Modifier.padding(end = 8.dp)
    )
}