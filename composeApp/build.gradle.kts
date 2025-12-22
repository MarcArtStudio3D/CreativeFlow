import org.jetbrains.compose.desktop.application.dsl.TargetFormat
import org.jetbrains.kotlin.gradle.ExperimentalWasmDsl
import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
    alias(libs.plugins.kotlinMultiplatform)
  //  alias(libs.plugins.androidApplication)
    alias(libs.plugins.composeMultiplatform)
    alias(libs.plugins.composeCompiler)
    alias(libs.plugins.composeHotReload)
}

kotlin {
   /* androidTarget {
        compilerOptions {
            jvmTarget.set(JvmTarget.JVM_11)
        }
    } */
    
    jvm()
    
    /*js {
        browser()
        binaries.executable()


    }
    
    @OptIn(ExperimentalWasmDsl::class)
    wasmJs {
        browser()
        binaries.executable()
    }
    */
    sourceSets {
    /*    androidMain.dependencies {

            implementation(compose.preview)
            implementation(libs.androidx.activity.compose)
            // Exposed para Android
            val exposedVersion = "0.56.0"
            implementation("org.jetbrains.exposed:exposed-core:$exposedVersion")
            implementation("org.jetbrains.exposed:exposed-jdbc:$exposedVersion")
            // CAMBIO: Sustituimos javatime por kotlin-datetime
            //implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.1")

        }
    */
        commonMain.dependencies {

            implementation(compose.runtime)
            implementation(compose.foundation)
            implementation(compose.material3)
            implementation(compose.ui)
            implementation(compose.components.resources)
            implementation(compose.components.uiToolingPreview)
            implementation(libs.androidx.lifecycle.viewmodelCompose)
            implementation(libs.androidx.lifecycle.runtimeCompose)
            implementation(projects.shared)
            implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.1")
            implementation(compose.materialIconsExtended)



        }
        commonTest.dependencies {
            implementation(libs.kotlin.test)
        }
        jvmMain.dependencies {
            implementation(compose.desktop.currentOs)
            implementation(libs.kotlinx.coroutinesSwing)
            val exposedVersion = "0.56.0"
            // Exposed para Desktop (JVM)
            implementation("org.jetbrains.exposed:exposed-core:$exposedVersion")
            implementation("org.jetbrains.exposed:exposed-dao:${exposedVersion}")
            implementation("org.jetbrains.exposed:exposed-jdbc:$exposedVersion")
            implementation("org.jetbrains.exposed:exposed-kotlin-datetime:${exposedVersion}")


            // Drivers solo para Desktop
            implementation("org.xerial:sqlite-jdbc:3.45.1.0")
            implementation("org.postgresql:postgresql:42.7.2")
            implementation("org.mariadb.jdbc:mariadb-java-client:3.3.3")
        }
    }
}

/*android {
    namespace = "com.artstudio3d.creativeflow"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.artstudio3d.creativeflow"
        minSdk = libs.versions.android.minSdk.get().toInt()
        targetSdk = libs.versions.android.targetSdk.get().toInt()
        versionCode = 1
        versionName = "1.0"
    }
    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
    buildTypes {
        getByName("release") {
            isMinifyEnabled = false
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
} */

dependencies {
 //   debugImplementation(compose.uiTooling)
}

compose.desktop {
    application {
        mainClass = "com.artstudio3d.creativeflow.MainKt"

        nativeDistributions {
            targetFormats(TargetFormat.Dmg, TargetFormat.Msi, TargetFormat.Deb)
            packageName = "com.artstudio3d.creativeflow"
            packageVersion = "1.0.0"
        }
    }
}
