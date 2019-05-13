import glob
import os

folder_path = '/Users/user/Desktop/segmentation/object_detection/original/'


def rename(folder_path):
	
	for i, filename in enumerate(glob.glob(path + '*.jpg')):
		os.rename(filename, os.path.join(path, str(i) + '.jpg'))



if __name__ == '__main__':
	rename(path)