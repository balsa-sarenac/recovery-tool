import sys
from tool import recover_and_transform

if __name__ == '__main__':
    print("Tool for moving windows recovery environment files to specified location and removing timestamp suffixes")
    recover_and_transform(sys.argv[1], sys.argv[2])
