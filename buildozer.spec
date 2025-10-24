[app]

# --- Основная информация о приложении ---
title = AI Restore
package.name = ai_restore
package.domain = org.dmitry.airestore

# --- Исходники ---
source.dir = .
source.include_exts = py,kv,png,jpg

# --- Версия ---
version = 0.1

# --- Зависимости ---
requirements = python3,kivy,pillow,numpy,imageio

# --- Права доступа ---
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# --- Архитектура ---
android.archs = arm64-v8a

# --- Иконка и сплэш-экран (можно потом заменить) ---
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# --- Прочее ---
fullscreen = 0
orientation = portrait
