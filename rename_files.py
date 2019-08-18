import glob
import os

folder_path = '/Users/user/Desktop/<your_folder>/'


def rename(folder_path):
	
	for i, filename in enumerate(glob.glob(folder_path + '*.jpeg')):
		os.rename(filename, os.path.join(folder_path, str(i) + '.jpeg'))



if __name__ == '__main__':
	rename(folder_path)
