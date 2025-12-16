package com.artstudio3d.creativeflow.ui.components

import androidx.compose.animation.animateColorAsState
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsHoveredAsState
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
// Imports de colores desde tu paquete de tema
import com.artstudio3d.creativeflow.ui.theme.DarkPetrol
import com.artstudio3d.creativeflow.ui.theme.OrangePrimary
import com.artstudio3d.creativeflow.ui.theme.LightGray
//import androidx.compose.foundation.layout.padding

@Composable
fun CFNativeButton(
    text: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    isActive: Boolean = false,
    buttonWidth: Dp
) {
    val interactionSource = remember { MutableInteractionSource() }
    val isHovered by interactionSource.collectIsHoveredAsState()

    val targetBackgroundColor = when {
        isActive -> OrangePrimary.copy(alpha = 0.9f)
        isHovered -> DarkPetrol.copy(alpha = 0.6f)
        else -> DarkPetrol
    }

    val targetTextColor = if (isActive) MaterialTheme.colorScheme.onPrimary else LightGray

    val animatedBackgroundColor by animateColorAsState(targetBackgroundColor)
    // Define el radio de redondeo deseado
    val buttonShape = RoundedCornerShape(4.dp)
    Box(
        modifier = modifier
            .width(buttonWidth)
            .background(animatedBackgroundColor, shape = buttonShape)
            .clickable(
                onClick = onClick,
                interactionSource = interactionSource,
                indication = null // <-- ESTO ELIMINA EL EFECTO ONDA Y LA SOMBRA
            )
            .padding(vertical = 10.dp, horizontal = 16.dp),
        contentAlignment = Alignment.CenterStart
    ) {
        Text(
            text = text,
            color = targetTextColor,
            style = MaterialTheme.typography.labelLarge,
            //modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp)

        )
    }
}