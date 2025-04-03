# Задача 1. Магия фото фильтров

from PIL import Image, ImageEnhance


def apply_magic_filter(image, brightness, color, contrast):
   image = ImageEnhance.Brightness(image).enhance(brightness)
   image = ImageEnhance.Color(image).enhance(color)
   image = ImageEnhance.Contrast(image).enhance(contrast)
   return image



if __name__ == "__main__":
    picture = input("Enter the picture filename: ")
    img = Image.open(picture)
    modified_img = apply_magic_filter(img, brightness=1.5, color=1.2, contrast=1.3)
    modified_img.show()