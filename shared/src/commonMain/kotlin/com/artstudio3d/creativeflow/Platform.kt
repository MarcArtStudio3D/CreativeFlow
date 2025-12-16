package com.artstudio3d.creativeflow

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform