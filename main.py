import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import imageio.v3 as iio
import subprocess
from datetime import datetime

# Папки
input_folder = "/storage/emulated/0/AI_Restore"
output_folder = "/storage/emulated/0/GOTOVOE"
os.makedirs(output_folder, exist_ok=True)

# Поддерживаемые форматы
supported_ext = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# Список файлов
files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_ext)]

if not files:
    print("❌ Нет изображений для обработки в", input_folder)
    exit()

print(f"🔍 Найдено {len(files)} файлов. Начинаю обработку...\n")

for file in files:
    photo_path = os.path.join(input_folder, file)
    print(f"📷 Обрабатывается: {photo_path}")

    try:
        # Загружаем и обрабатываем
        img = iio.imread(photo_path)
        img = img.astype(np.float32) / 255.0

        pil_img = Image.fromarray((img * 255).astype(np.uint8))
        pil_img = pil_img.filter(ImageFilter.MedianFilter(size=3))
        pil_img = pil_img.filter(ImageFilter.BoxBlur(radius=1))

        enhancer = ImageEnhance.Contrast(pil_img)
        final_img = enhancer.enhance(1.3)
        final_img = final_img.filter(ImageFilter.SHARPEN)

        # Формируем имя
        name, ext = os.path.splitext(file)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_folder, f"{name}_restored_{timestamp}{ext}")

        # Сохраняем
        final_img.save(output_file)
        print(f"✅ Готово: {output_file}\n")

    except Exception as e:
        print(f"⚠️ Ошибка при обработке {file}: {e}")

# Обновляем медиабазу Android
try:
    subprocess.run(["termux-media-scan", output_folder])
    print("📱 Галерея обновлена — фото должны быть видны.")
except Exception as e:
    print(f"⚠️ Не удалось обновить медиабазу: {e}")
