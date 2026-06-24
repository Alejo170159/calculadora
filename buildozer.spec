[app]

# (string) Title of your application
title = Calculadora

# (string) Package name
package.name = calculadora

# (string) Package domain (needed for android packaging)
package.domain = org.test

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas

# CORRECCIÓN 1: ¡Faltaba la versión de la app! Aquí la agregamos
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# (string) Presplash of the application
presplash.filename = %(source.dir)s/calcu.jpeg

# (string) Icon of the application
icon.filename = %(source.dir)s/calcu.jpeg

# (string) Supported orientations (valid options are: landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configuration
# =============================================================================

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (bool) Use --private data directory for storage (True) or public (/sdcard)
android.private_storage = True

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support (required for modern KivyMD)
android.enable_androidx = True

# CORRECCIÓN 2: Se cambió de 'android.bootstrap' a 'p4a.bootstrap' como exige el nuevo Buildozer
p4a.bootstrap = sdl2

# =============================================================================
# Buildozer configurations
# =============================================================================
[buildozer]

# (int) Log level (1 = error only, 2 = all)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
