# Скрипт для подсчета количества изображений в папках
import os
import numpy as np


folderpath = '/Users/user/Desktop/21-1000/'


init_folders_num = []
c = 0
for dirpath, dirnames, filenames in os.walk(folderpath):
    path, dirs, files = next(os.walk(dirpath))
    file_count = len(files)
    init_folders_num.append(file_count)

#print('Init folders num: ', len(init_folders_num))
#print('Init number of images: ', sum(init_folders_num))
#print('Median number of images: ', np.mean(init_folders_num))

folders_num_after_filtering = [elem for elem in init_folders_num if elem > 1 and elem < 100]
print('Folders num after filtering: ', len(folders_num_after_filtering))
print('Number of images after filtering: ', sum(folders_num_after_filtering))
print('Mean of images after filtering: ', np.mean(folders_num_after_filtering))

