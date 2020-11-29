import os
from shutil import copyfile


def recover_and_transform(path_to_backup, where_to_move):
    print("Moving recovery files from {} to {} and removing suffixes"
          .format(path_to_backup, where_to_move))
    iterate_though_backup(path_to_backup, where_to_move)
    return None


def iterate_though_backup(path_to_backup, where_to_move):
    for subdir, dirs, files in os.walk(path_to_backup):
        # print(subdir)
        for file in files:
            copy_file(subdir, file, where_to_move, new_name(file))


def copy_file(subdir, file, where_to_move, new_filename):
    filename = os.path.join(subdir, file)
    copyfile(filename, os.path.join(where_to_move, new_filename))


def new_name(file):
    name_start = file[:file.rindex('(') - 1]
    if file.rfind('.') != -1:
        return name_start + file[file.rindex('.'):]
    else:
        return name_start
