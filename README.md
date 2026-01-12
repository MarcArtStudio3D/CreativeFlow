CreativeFlow 🚀

Gestión Profesional Nativa para Estudios Creativos.

CreativeFlow nace como la respuesta técnica para los profesionales que huyen de las suscripciones SaaS de alto coste y las herramientas web lentas.
Es un software de rendimiento nativo diseñado para ofrecer potencia, privacidad y propiedad total sobre la información, sin depender de nubes externas ni cuotas mensuales.

Gestion Professionnelle Native pour Studios Créatifs

CreativeFlow est né comme la réponse technique pour les professionnels qui fuient les abonnements SaaS coûteux et les outils web lents.
C'est un logiciel de performance native conçu pour offrir puissance, confidentialité et propriété totale de l'information, sans dépendre de clouds externes ni de mensualités.

🇪🇸 Castellano
🔹 Filosofía del Proyecto

    Independencia del Navegador: Olvida las pestañas lentas y el consumo excesivo de RAM. CreativeFlow es una aplicación nativa que aprovecha al máximo el hardware.

    Privacidad y Propiedad: Los datos te pertenecen. El sistema trabaja con bases de datos locales (o servidores propios), eliminando la dependencia de terceros.

    Eficiencia Radical (RAD): Interfaz optimizada para el flujo de trabajo real. Menos clics, más velocidad, sin la complejidad innecesaria de los grandes ERP genéricos.

    Sin Costes Ocultos: Diseñado para empresas que buscan una herramienta potente y profesional sin el sangrado económico de los modelos de suscripción actuales.

🛠️ Especificaciones

    Motor: Python 3.13 sobre MacOS, Linux o Windows.

    Interfaz: UI Oscura nativa de alto contraste (#2D2D2D).

    Datos: Arquitectura modular con persistencia en SQLite/MariaSQL local.

🇫🇷 Français
🔹 Philosophie du Projet

    Indépendance du Navigateur: Fini les onglets lents. CreativeFlow est une application native qui exploite pleinement la puissance de votre matériel.

    Vie Privée et Propriété: Vos données vous appartiennent. Le système fonctionne avec des bases de données locales, éliminant toute dépendance vis-à-vis des tiers.

    Efficacité Radicale (RAD): Une interface optimisée pour le flux de travail réel. Moins de clics, plus de vitesse, sans la complexité inutile des ERP génériques.

    Pas de Coûts Cachés: Conçu pour les entreprises à la recherche d'un outil puissant et professionnel sans le fardeau financier des abonnements SaaS.

🛠️ Spécifications Techniques

    Moteur: Python 3.13 sous MacOS, Linux o Windows.

    Interface: UI sombre native à haut contraste (#2D2D2D).

    Données: Architecture modulaire avec persistance SQLite/MariaSQL locale.

---

## 📦 Instalación / Installation

### Requisitos / Prérequis
- Python 3.10 o superior / Python 3.10 ou supérieur
- 100 MB de espacio en disco / 100 Mo d'espace disque
- Git (opcional / optionnel)

### 🐧 Linux / macOS

#### Instalación automática / Installation automatique:
```bash
# Clonar el repositorio / Cloner le dépôt
git clone https://github.com/tu-usuario/CreativeFlow.git
cd CreativeFlow

# Ejecutar instalador / Exécuter l'installateur
chmod +x install.sh
./install.sh
```

#### Instalación manual / Installation manuelle:
```bash
# Crear entorno virtual / Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias / Installer les dépendances
pip install -r requirements.txt

# Compilar interfaces / Compiler les interfaces
chmod +x scripts/compile_ui.sh
./scripts/compile_ui.sh

# Ejecutar / Exécuter
python main.py
```

### 🪟 Windows

#### Instalación automática / Installation automatique:
```cmd
REM Clonar el repositorio / Cloner le dépôt
git clone https://github.com/tu-usuario/CreativeFlow.git
cd CreativeFlow

REM Ejecutar instalador / Exécuter l'installateur
install.bat
```

#### Instalación manual / Installation manuelle:
```cmd
REM Crear entorno virtual / Créer l'environnement virtuel
python -m venv .venv
.venv\Scripts\activate.bat

REM Instalar dependencias / Installer les dépendances
pip install -r requirements.txt

REM Ejecutar / Exécuter
python main.py
```

### 🔧 Configuración de Base de Datos / Configuration de la Base de Données

CreativeFlow soporta tres tipos de bases de datos:
- **SQLite** (predeterminado, sin configuración) / (par défaut, sans configuration)
- **MariaDB/MySQL** (servidor local o remoto) / (serveur local ou distant)
- **PostgreSQL** (servidor local o remoto) / (serveur local ou distant)

La configuración se realiza desde la interfaz de administración después del primer inicio.

---

## 🚀 Inicio Rápido / Démarrage Rapide

```bash
# Activar entorno / Activer l'environnement
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate.bat # Windows

# Ejecutar aplicación / Exécuter l'application
python main.py
```

**Usuario por defecto / Utilisateur par défaut:**
- Usuario / Utilisateur: `admin`
- Contraseña / Mot de passe: *(configurar en primer inicio / à configurer au premier démarrage)*

---

## 📚 Estructura del Proyecto / Structure du Projet

```
CreativeFlow/
├── main.py                 # Punto de entrada / Point d'entrée
├── requirements.txt        # Dependencias / Dépendances
├── install.sh             # Instalador Linux/macOS
├── install.bat            # Instalador Windows
├── styles.qss             # Estilos de interfaz / Styles d'interface
├── creativeflow.db        # Base de datos SQLite
├── database/              # Gestión de datos / Gestion des données
├── login/                 # Módulo de autenticación
├── modulos/               # Módulos de aplicación
│   ├── empresas/         # Gestión de empresas
│   ├── ventas/           # Módulo de ventas
│   ├── almacen/          # Gestión de almacén
│   ├── configuracion/    # Configuración
│   └── ...
├── scripts/               # Scripts de utilidad
│   └── compile_ui.sh     # Compilador de interfaces
└── ui/                    # Archivos de interfaz Qt Designer

```

---

## 🛠️ Desarrollo / Développement

### Compilar interfaces después de cambios / Compiler les interfaces après modifications:
```bash
./scripts/compile_ui.sh
```

### Estructura de un módulo / Structure d'un module:
```
modulos/mi_modulo/
├── __init__.py
├── controller/
│   └── controller.py     # Lógica de negocio
├── model/
│   └── model.py          # Acceso a datos
└── view/
    ├── view.py           # Clase de vista
    └── ui_*.py           # Archivos generados (no editar)
```

### Añadir nueva pantalla / Ajouter un nouvel écran:
1. Diseñar en Qt Designer (.ui en carpeta `ui/`)
2. Ejecutar `./scripts/compile_ui.sh`
3. Crear clase View que herede de Ui_*
4. Crear Controller y Model según patrón MVC

---

## 📄 Licencia / Licence

[Especificar licencia / Spécifier la licence]

---

## 👥 Contribuir / Contribuer

Las contribuciones son bienvenidas. Por favor:
1. Fork del proyecto
2. Crea una rama feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit de cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

---

## 📞 Soporte / Support

Para problemas o preguntas / Pour des problèmes ou questions:
- 📧 Email: support@creativeflow.com
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/CreativeFlow/issues)

---

**CreativeFlow** - Potencia nativa, privacidad total, costes bajo control.
**CreativeFlow** - Puissance native, confidentialité totale, coûts maîtrisés.

