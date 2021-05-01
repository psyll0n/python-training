#!/usr/bin/env python

import fire
import os

# os.listdir returns the contents of a directory.
def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        childs = os.listdir(parent_path)
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.join(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
    # Construct the full path of an item in the parent directory.
    for child in childs:
        child_path = os.path.join(parent_path, child)
        
    # Check to see if the path represents a file.
    if os.path.isfile(child_path):
        size = os.path.getsize(child_path)
        # Get the last time the file was accessed.
        last_access = os.path.getatime(child_path)
        print(f"File: {child_path}")
        print(f"\tlast accessed: {last_access}")
        # Get the size of the file.
        print(f"\tsize: {size}")
    # Check if the path represents a directory.
    elif os.path.isdir(child_path):
        # Check the tree from this directory down.
        walk_path(child_path)



if __name__ == '__main__':
    fire.Fire()
    
    
    