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

# (list) Application requirements
# NOTA: Agregamos kivy y kivymd de forma explícita
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# (string) Custom source folders for requirements
# requirements.source.kivy =

# (string) Presplash of the application
# CORRECCIÓN: Apunta exactamente a tu archivo calcu.jpeg
presplash.filename = %(source.dir)s/calcu.jpeg

# (string) Icon of the application
# CORRECCIÓN: Apunta exactamente a tu archivo calcu.jpeg
icon.filename = %(source.dir)s/calcu.jpeg

# (string) Supported orientations (valid options are: landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configuration
# =============================================================================

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (int) Android SDK version to use
# android.sdk = 33

# (str) Android NDK version to use
# android.ndk = 25b

# (bool) Use --private data directory for storage (True) or public (/sdcard)
android.private_storage = True

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support (required for modern KivyMD)
android.enable_androidx = True

# (str) Bootstrap to use for android builds
android.bootstrap = sdl2

# =============================================================================
# Buildozer configurations
# =============================================================================
[buildozer]

# (int) Log level (1 = error only, 2 = all)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
