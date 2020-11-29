import os
from shutil import copyfile


def recover_and_transform(path_to_backup, where_to_move):
    print("Moving recovery files from {} to {} and removing suffixes"
          .format(path_to_backup, where_to_move))
    iterate_though_backup(path_to_backup, where_to_move)
    return None


def iterate_though_backup(path_to_backup, where_to_move):
    for subdir, dirs, files in os.walk(path_to_backup):
        location = subdir[subdir.index('Users'):][6:]
        for directory in dirs:
            new_dir = os.path.join(where_to_move, location, directory)
            os.mkdir(new_dir)
        for file in files:
            final_location = os.path.join(where_to_move, location, new_name(file))
            copy_file(subdir, file, final_location)


def copy_file(subdir, file, new_location):
    filename_location = os.path.join(subdir, file)
    copyfile(filename_location, new_location)


def new_name(file):
    name_start = file[:file.rindex('(') - 1]
    if file.rfind('.') != -1:
        return name_start + file[file.rindex('.'):]
    else:
        return name_start
