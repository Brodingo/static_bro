import os, shutil

from copy_static import copy_files

SOURCE_DIR = './static'
DEST_DIR = './public'


def main():

    print("Main function executing, build process starting...")

    if os.path.exists(DEST_DIR):
        print(f"{DEST_DIR} exists, deleting...")
        shutil.rmtree(DEST_DIR)

    print('Starting to copy files...')
    copy_files(SOURCE_DIR, DEST_DIR)


main()