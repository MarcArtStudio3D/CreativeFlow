package com.artstudio3d.creativeflow.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.shape.RoundedCornerShape
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

import androidx.compose.material.icons.filled.Search

import androidx.compose.material3.OutlinedTextField

import androidx.compose.material3.OutlinedTextFieldDefaults
import com.artstudio3d.creativeflow.models.ModuloModel
import com.artstudio3d.creativeflow.models.ModuloSeccionModel
import com.artstudio3d.creativeflow.repositories.ModuloRepository

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MainDashboard(onLogout: () -> Unit) {
// 1. ESTADOS
    var moduloSeleccionado by remember { mutableStateOf<Int?>(null) }
    var seccionSeleccionada by remember { mutableStateOf("No hay ninguna seleccionada") }
    var textoBusqueda by remember { mutableStateOf("") }

    // CORRECCIÓN: Usamos ModuloModel, no DTO
    var listaModulos by remember { mutableStateOf<List<ModuloModel>>(emptyList()) }
    var secciones by remember { mutableStateOf(listOf<ModuloSeccionModel>()) }
    // Cargar módulos de la base de datos al iniciar
    LaunchedEffect(Unit) {
        val datos = ModuloRepository.obtenerModulosPadre()
        // Si la DB viene vacía, ponemos los de prueba para que no veas la pantalla en blanco
        listaModulos = datos.ifEmpty {
            listOf(
                ModuloModel(1, "Proyectos", "Gestión de producción 3D", "Projects"),
                ModuloModel(2, "Ventas", "Facturación y presupuestos", "Sales"),
                ModuloModel(3, "ADMIN", "Configuración del sistema", "Admin")
            )
        }
    }

    // Dentro de tu @Composable MainDashboard


// Efecto para cargar secciones cuando cambie el ID seleccionado
    LaunchedEffect(moduloSeleccionado) {
        moduloSeleccionado?.let { id ->
            println("Cargando secciones para el módulo ID: $id") // Debug
            secciones = ModuloRepository.obtenerSecciones(id)
        }
    }

    Row(Modifier.fillMaxSize()) {
        // SIDEBAR
        Column(Modifier.width(250.dp).fillMaxHeight().background(Color.DarkGray)) {
            Text("SECCIONES", color = Color.White, modifier = Modifier.padding(16.dp))

            secciones.forEach { seccion ->
                Text(
                    text = seccion.nombre,
                    color = Color.LightGray,
                    modifier = Modifier.fillMaxWidth().padding(16.dp).clickable { /* Cambiar vista */ }
                )
            }
        }

    }

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
            // Busca la parte del Sidebar (Surface con ancho 260.dp) y reemplázala por esto:
            Surface(
                modifier = Modifier.width(260.dp).fillMaxHeight(),
                color = MaterialTheme.colorScheme.surface,
                tonalElevation = 2.dp
            ) {
                Column(modifier = Modifier.padding(12.dp)) {
                    if (moduloSeleccionado == null) {
                        Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                            Text("Selecciona un módulo para ver secciones",
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    } else {
                        // TÍTULO DEL SIDEBAR
                        Text("SECCIONES",
                            fontWeight = FontWeight.Bold,
                            color = MaterialTheme.colorScheme.primary,
                            style = MaterialTheme.typography.labelLarge)

                        Spacer(Modifier.height(20.dp))

                        // LISTA DINÁMICA DE SECCIONES DE LA DB
                        secciones.forEach { seccion ->
                            NavigationDrawerItem(
                                label = { Text(seccion.nombre) },
                                selected = seccionSeleccionada == seccion.vistaId,
                                onClick = { seccionSeleccionada = seccion.vistaId },
                                icon = { Icon(Icons.Default.List, contentDescription = null) },
                                shape = RoundedCornerShape(8.dp),
                                modifier = Modifier.padding(vertical = 2.dp)
                            )
                        }

                        if (secciones.isEmpty()) {
                            Text("No hay secciones configuradas",
                                style = MaterialTheme.typography.bodySmall,
                                color = Color.Gray)
                        }
                    }
                }
            }

            // CONTENT AREA
            val modulosFiltrados = listaModulos
                .filter { it.nombre.contains(textoBusqueda, ignoreCase = true) }
                .distinctBy { it.id } // Esto evita que se repitan IDs iguales

            Box(modifier = Modifier.weight(1f).fillMaxSize().padding(24.dp)) {
                if (moduloSeleccionado == null) {
                    // ... dentro del Box del Content Area (donde moduloSeleccionado == null)
                    Column(modifier = Modifier.fillMaxSize()) {

                        // --- BUSCADOR ESTILIZADO ---
                        OutlinedTextField(
                            value = textoBusqueda,
                            onValueChange = { textoBusqueda = it },
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(bottom = 24.dp),
                            placeholder = { Text("Buscar módulo o herramienta...", color = MaterialTheme.colorScheme.onSurfaceVariant) },
                            leadingIcon = {
                                Icon(
                                    imageVector = Icons.Default.Search,
                                    contentDescription = null,
                                    tint = MaterialTheme.colorScheme.primary
                                )
                            },
                            singleLine = true,
                            shape = RoundedCornerShape(12.dp),
                            colors = OutlinedTextFieldDefaults.colors(
                                focusedBorderColor = MaterialTheme.colorScheme.primary, // Naranja
                                unfocusedBorderColor = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.2f),

                                // AQUÍ ESTÁ EL CAMBIO CLAVE:
                                focusedContainerColor = MaterialTheme.colorScheme.surfaceVariant,
                                unfocusedContainerColor = MaterialTheme.colorScheme.surfaceVariant,

                                // También es buena idea definir el color del texto para que no haya sorpresas
                                focusedTextColor = MaterialTheme.colorScheme.onSurface,
                                unfocusedTextColor = MaterialTheme.colorScheme.onSurface
                            )
                        )

                        // --- REJILLA FILTRADA ---

                        LazyVerticalGrid(
                            columns = GridCells.Adaptive(minSize = 280.dp),
                            modifier = Modifier
                                .fillMaxSize()
                                .weight(1f),
                            contentPadding = PaddingValues(16.dp),
                            horizontalArrangement = Arrangement.spacedBy(24.dp),
                            verticalArrangement = Arrangement.spacedBy(24.dp)
                        ) {
                            items(modulosFiltrados, key ={it.id}) { modulo ->
                                ModuloCard(
                                    titulo = modulo.nombre,
                                    descripcion = modulo.descripcion,
                                    imagenPainter = painterResource(Res.drawable.Projects),
                                    seleccionado = false,
                                    onClick = { moduloSeleccionado = modulo.id }
                                )
                            }
                        }
                    }
                    
                } else {
                    // Buscamos el objeto completo del módulo seleccionado en nuestra lista de la DB
                    val moduloActual = listaModulos.find { it.id == moduloSeleccionado }
                    Column {
                        Text(
                            text = moduloActual?.nombre?: "Módulo Desconocido",
                            style = MaterialTheme.typography.headlineMedium,
                            color = MaterialTheme.colorScheme.primary
                        )
                        Spacer(Modifier.height(8.dp))
                        Text(
                            text = "Panel de control: ${moduloActual?.descripcion}",
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )

                        HorizontalDivider(
                            modifier = Modifier.padding(vertical = 16.dp),
                            thickness = 1.dp,
                            color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.1f)
                        )

                        // Aquí es donde cargarás los datos de MariaDB según la seccionSeleccionada
                        Text("Visualizando sección: $seccionSeleccionada")
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