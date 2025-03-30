from PIL import Image
import requests
from PIL.ImageDraw import ImageDraw
from matplotlib import pyplot as plt

'''url = 'https://i.pinimg.com/originals/7d/76/7f/7d767fee79d3ee638c3c0fb20e8735a7.jpg' # загрузка изображения и работа с ним
resp = requests.get(url, stream=True).raw
img = Image.open(resp)
img.save('cats.png')
#img.show()
#print(img.size)
#print(type(img))
#print(img)
plt.imshow(img)
#plt.axis('off')
plt.show()

cropped = img.crop((400, 200, 1200, 600)) # обрезка изображения по векторам 400 - ось Х начало, 200 - ось Y верх, 1200 - ось X конец, 600 - ось Y низ
plt.imshow(cropped)
plt.axis('off')
plt.show()

image = Image.open('cats.png') # изображение как матрица - вывод пикселей форматом RGB в ч/б виде с интенсивностью от 0 до 255 в зависимости от наличия цвета в части картинки
r, g, b = image.split()

for im, title in (r, 'red'), (g, 'green'), (b, 'blue'):
    plt.figure(figsize=(5, 5))
    plt.axis('off')
    print(title)
    plt.imshow(im, cmap='gray')
    plt.show()'''

'''img_new = Image.new('RGBA', (200, 200), 'white') # создание нового изображения
idraw = ImageDraw(img_new)
idraw.rectangle((10, 10, 100, 100), fill='red') # прямоугольник размещенный в векторах
idraw.ellipse((10, 10, 100, 100), fill='blue') # окружность размещенная в векторах
idraw.arc((110, 10, 150, 100), fill='green', start=0, end=360) # часть окружности размещенный в векторах. start и end это та чатсть окружности, которая будет отрисована. Отрисовка идет по часовой стрелке
plt.imshow(img_new)
plt.show()'''

#cats = Image.open('cats.png')
#print(cats.size)
#pixels = cats.load()
'''for i in range(cats.size[0]): #смена каналов местами
    for j in range(cats.size[1]):
        r, g, b = pixels[i, j]
        pixels[i, j] = (g, r, b)'''
'''for i in range(cats.size[0]): # инверсия цветов
    for j in range(cats.size[1]):
        r, g, b = pixels[i, j]
        pixels[i, j] = (255-r, 255-g, 255-b)'''
'''for i in range(cats.size[0]): # ч/б фильтр
    for j in range(cats.size[1]):
        r, g, b = pixels[i, j]
        intensity = int(r*0.25 + b*0.25 + g*0.5)
        pixels[i, j] = (intensity, intensity, intensity)'''
'''shift = 20
for j in range(cats.size[1]): # анаглиф
    for i in range(cats.size[0] - shift):
        r, g, b = pixels[i, j]
        pixels[i, j] = (pixels[i+shift, j][0], g, b)'''

# Задача: водный знак
# На входе передается две строки: файл с изображением и файл с водным знаком.
# Требуется нанести водный знак на правый нижний угол изображения. Черные пиксели водного знака игнорируются

picture = input("Введите название файла с изображением: ")
watermark = input("Введите название файла с водяным знаком: ")

cats = Image.open(picture)
wm = Image.open(watermark)
plt.imshow(cats)
plt.show()
water_pixels = wm.load()
pixels = cats.load()
x = 1200
y = 1000

for i in range(wm.size[0]):
    for j in range(wm.size[1]):
        if water_pixels[i, j] != (0, 0, 0, 255):
            pixels[x+i, y+j] = water_pixels[i, j]
plt.imshow(cats)
plt.axis('off')
plt.show()
