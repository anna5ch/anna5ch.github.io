import os
from PIL import Image

def resize_image(input_path, output_path, target_size_kb):
    image = Image.open(input_path)
    quality = 95  # Start with high quality
    step = 5  # Initial step size

    while True:
        image.save(output_path, quality=quality, optimize=True)
        size_kb = os.path.getsize(output_path) / 1024
        if size_kb <= target_size_kb or quality <= 10:
            break
        quality -= step

        # Reduce the step size for finer adjustments if close to target size
        if size_kb <= target_size_kb * 1.5:
            step = 1

def process_folder(input_folder, output_folder, target_size_kb):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, target_size_kb)

if __name__ == "__main__":
    input_folder = "images/"  # Ersetzen Sie dies durch den Pfad zu Ihrem Eingabeordner
    output_folder = "images/thumbnails/"  # Ersetzen Sie dies durch den Pfad zu Ihrem Ausgabeordner
    target_size_kb = 100  # Zielgröße in KB
    process_folder(input_folder, output_folder, target_size_kb)
