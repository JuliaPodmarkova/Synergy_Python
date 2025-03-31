# Задача 3. Геометрический абстракционизм

from PIL import Image, ImageDraw
import random

random.seed(777)

def create_geometric_art(width, height):
    blank_image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(blank_image)

    for _ in range(100):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        size_x, size_y = random.randint(20, 100), random.randint(20, 100)
        shape_type = random.randint(0, 1)
        if shape_type == 0:
            draw.ellipse((x, y, x + size_x, y + size_y), fill=color)
        else:
            draw.rectangle((x, y, x + size_x, y + size_y), fill=color)
    return blank_image

if __name__ == "__main__":
    width, height = 800, 600
    geometric_art_image = create_geometric_art(width, height)
    geometric_art_image.show()