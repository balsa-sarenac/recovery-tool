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
            print(new_name(file))
    pass


def new_name(file):
    name_start = file[:file.rindex('(') - 1]
    if file.rfind('.') != -1:
        return name_start + file[file.rindex('.'):]
    else:
        return name_start
