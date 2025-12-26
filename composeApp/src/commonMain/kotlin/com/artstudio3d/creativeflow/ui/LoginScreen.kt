package com.artstudio3d.creativeflow.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import com.artstudio3d.creativeflow.models.EmpresaModel
import com.artstudio3d.creativeflow.repositories.AuthGateway
import com.artstudio3d.creativeflow.repositories.ModuloRepository
import com.artstudio3d.creativeflow.services.AuthService
import com.artstudio3d.creativeflow.session.AppSession
import kotlin.system.exitProcess

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LoginScreen(onLoginSuccess: () -> Unit) {
    // Estados locales para los campos de texto
    var empresas by remember { mutableStateOf<List<EmpresaModel>>(emptyList()) }
    var empresaSeleccionada by remember { mutableStateOf<EmpresaModel?>(null) }
    var userText by remember { mutableStateOf("") }
    var passText by remember { mutableStateOf("") }
    var errorVisible by remember { mutableStateOf(false) }
    var mensajeError by remember { mutableStateOf("") }
    var expandido by remember { mutableStateOf(false) } // Para controlar el desplegable

// Cargar empresas de SQLite al entrar a la pantalla
    LaunchedEffect(Unit) {
        empresas = ModuloRepository.obtenerEmpresas()
        if (empresas.isNotEmpty()) {
            empresaSeleccionada = empresas[0] // Seleccionar la primera por defecto
        }
    }
    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.width(300.dp)
        ) {
            // --- SELECTOR DE EMPRESA ---
            Box(modifier = Modifier.fillMaxWidth().padding(bottom = 16.dp)) {
                OutlinedTextField(
                    value = empresaSeleccionada?.nombreComercial ?: "Seleccione Empresa",
                    onValueChange = {},
                    readOnly = true,
                    label = { Text("Empresa") },
                    trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expandido) },
                    modifier = Modifier.fillMaxWidth().clickable { expandido = true }
                )
                DropdownMenu(
                    expanded = expandido,
                    onDismissRequest = { expandido = false },
                    modifier = Modifier.fillMaxWidth()
                ) {
                    empresas.forEach { empresa ->
                        DropdownMenuItem(
                            text = { Text(empresa.nombreComercial ?: empresa.nombreFiscal) },
                            onClick = {
                                empresaSeleccionada = empresa
                                expandido = false
                            }
                        )
                    }
                }
            }
            Text("CREATIVE FLOW", style = MaterialTheme.typography.headlineMedium)
            Text("VFX Pipeline System", style = MaterialTheme.typography.bodySmall)

            Spacer(modifier = Modifier.height(32.dp))

            OutlinedTextField(
                value = userText,
                onValueChange = { userText = it; errorVisible = false },
                label = { Text("Usuario") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true
            )

            Spacer(modifier = Modifier.height(16.dp))

            OutlinedTextField(
                value = passText,
                onValueChange = { passText = it; errorVisible = false },
                label = { Text("Contraseña") },
                visualTransformation = PasswordVisualTransformation(),
                modifier = Modifier.fillMaxWidth(),
                singleLine = true
            )

            if (errorVisible) {
                Text(
                    mensajeError,
                    color = MaterialTheme.colorScheme.error,
                    style = MaterialTheme.typography.bodySmall,
                    modifier = Modifier.padding(top = 8.dp)
                )
            }

            Spacer(modifier = Modifier.height(32.dp))

            Button(onClick = {
                AuthService.login(empresaSeleccionada, userText, passText)
                    .onSuccess {
                        println("✅ Login correcto")
                        onLoginSuccess()
                    }
                    .onFailure { error ->
                        // Aquí solo manejas cómo mostrar el error al usuario (ej: un Snackbar)
                        mensajeError = error.message ?: "Error desconocido"
                        errorVisible = true
                    }
            }) {
                Text("Entrar")
            }
            Spacer(modifier = Modifier.height(32.dp))

            Button(
                onClick = {
                    exitProcess(0)
                },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(50.dp)

            ) {
                Text("CERRAR APLICACIÓN")
            }
        }
    }
}
