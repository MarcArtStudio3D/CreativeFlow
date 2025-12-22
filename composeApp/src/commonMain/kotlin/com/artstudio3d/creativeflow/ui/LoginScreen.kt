package com.artstudio3d.creativeflow.ui

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import com.artstudio3d.creativeflow.repositories.AuthGateway
import com.artstudio3d.creativeflow.session.AppSession

@Composable
fun LoginScreen(onLoginSuccess: () -> Unit) {
    // Estados locales para los campos de texto
    var userText by remember { mutableStateOf("") }
    var passText by remember { mutableStateOf("") }
    var errorVisible by remember { mutableStateOf(false) }

    Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.width(300.dp)
        ) {
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
                    "Usuario o contraseña incorrectos",
                    color = MaterialTheme.colorScheme.error,
                    style = MaterialTheme.typography.bodySmall,
                    modifier = Modifier.padding(top = 8.dp)
                )
            }

            Spacer(modifier = Modifier.height(32.dp))

            Button(
                onClick = {
                    val valido = AuthGateway.login(userText, passText)
                    if (valido) {
                        // RELLENAMOS LA SESIÓN
                        AppSession.usuarioLogueado = userText
                        AppSession.permisos = AuthGateway.loadPermissions(userText)

                        // AVISAMOS AL MAIN
                        onLoginSuccess()
                    } else {
                        errorVisible = true
                    }
                },
                modifier = Modifier.fillMaxWidth().height(50.dp)
            ) {
                Text("ENTRAR")
            }
        }
    }
}