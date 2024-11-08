import os, shutil


def copy_files(source_dir, dest_dir):
   
    # Check if dest dir exists
    if not os.path.exists(dest_dir):
        print(f'Destination {dest_dir} does not exist, creating directory...')
        os.mkdir(dest_dir)

    # Start copying files and recursing into sub-directories
    print(f"Copying files from: {source_dir} -> {dest_dir}")
    dir_paths = os.listdir(source_dir)

    print('Listing current directory files...')
    print(dir_paths)
    for path in dir_paths:
        full_source_path = os.path.join(source_dir, path)
        full_dest_path = os.path.join(dest_dir, path)
        if os.path.isfile(full_source_path):
            print(f"Current file: {full_source_path}")
            print(f"Copying file from {full_source_path} to {full_dest_path}...")
            shutil.copy(full_source_path, full_dest_path)
        if os.path.isdir(full_source_path):
            print(f"Current dir: {full_source_path}")
            print(f'Copying files recursively to sub directory')
            copy_files(full_source_path, full_dest_path)
