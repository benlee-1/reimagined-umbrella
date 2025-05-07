import os
import shutil

def copy_static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    
    inner_func(source, destination)

def inner_func(source, destination):
    if os.path.exists(source):
        parts = os.listdir(source)
        for part in parts:
            src_path = os.path.join(source, part)
            print(f"Processing: {src_path}")
            if os.path.isfile(src_path):
                print(f"Copying file: {src_path} to {destination}")
                shutil.copy(src_path, destination)
            else:
                dst_subdir = os.path.join(destination, part)
                print(f"Creating subdirectory: {dst_subdir}")
                os.mkdir(dst_subdir)
                inner_func(src_path, dst_subdir)