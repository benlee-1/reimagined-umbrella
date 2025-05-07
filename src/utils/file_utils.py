import os
import shutil

def copy_static_to_public(source, destination):
    if(os.path.exists(destination)):
        #delete contents of the destination 
        shutil.rmtree(destination)

    inner_func(source, destination)

def inner_func(source, destination):
    if(os.path.exists(source)):
        #grab each file/component from the source file, and move it over to the destination file
        parts = os.listdir(source)
        for part in parts:
            src_path = os.path.join(source, part)
            if(os.path.isfile(src_path)):
                print(f"Copying {src_path} to {destination}")
                shutil.copy(src_path, destination)
            else:
                dst_subdir = os.path.join(destination, part)
                os.mkdir(dst_subdir)
                inner_func(src_path, dst_subdir)