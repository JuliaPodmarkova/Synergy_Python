# Задача 2. Мозаика из пикселей

from PIL import Image

def create_pixel_art(image, block_size):
    width, height = image.size
    new_width = (width // block_size) * block_size
    new_height = (height // block_size) * block_size
    image = image.crop((0, 0, new_width, new_height))

    pixel_art_image = Image.new("RGB", (new_width, new_height))

    for y in range(0, new_height, block_size):
        for x in range(0, new_width, block_size):
            box = (x, y, x + block_size, y + block_size)
            block = image.crop(box)
            r, g, b = 0, 0, 0
            pixels = list(block.getdata())
            for pixel in pixels:
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
            num_pixels = len(pixels)
            r //= num_pixels
            g //= num_pixels
            b //= num_pixels
            pixel_art_image.paste((r, g, b), box)
    return pixel_art_image


if __name__ == "__main__":
    picture = input("Enter a picture: ")
    img = Image.open(picture)
    pixel_art_img = create_pixel_art(img, block_size=20)
    pixel_art_img.show()