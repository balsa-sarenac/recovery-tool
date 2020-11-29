import os
from shutil import copyfile


def recover_and_transform(path_to_backup, where_to_move):
    print("Moving recovery files from {} to {} and removing suffixes"
          .format(path_to_backup, where_to_move))
    iterate_though_backup(path_to_backup)
    return None


def iterate_though_backup(path_to_backup):
    for subdir, dirs, files in os.walk(path_to_backup):
        print(files)
        for file in files:
            print(file)
    pass


