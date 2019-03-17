# Скрипт для подсчета количества изображений в папках
import os


image_paths = []

folderpath = '/Volumes/WD_NEW/cats/'

c = 0
for dirpath, dirnames, filenames in os.walk(folderpath):
    for filename in filenames:
        c += 1
print(c)
