import os

path_to_folder = '/Users/user/Desktop/<your_folder>/'


def rename(path_to_folder):

    i = 1   # first folder name
    for folder in os.listdir(path_to_folder):
        # If folder is not a folder
        if not os.path.isdir(os.path.join(path_to_folder, folder)):
            continue
        # There should not be any folders with the same names in initial path
        os.rename(os.path.join(path_to_folder, folder), os.path.join(path_to_folder, '{}'.format(i)))
        i += 1


if __name__ == '__main__':
    rename(path_to_folder)
