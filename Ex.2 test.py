import os


def scan_files(path='./'):
    for root, dirs, files in os.walk(path):
        print(files)
        for file in files:
            print(os.path.basename(file))
            print(type(os.stat(file)))
            print(os.stat(file).st_size)


scan_files()


