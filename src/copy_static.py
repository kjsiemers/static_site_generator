import os
import shutil

def del_files_in_dir(dir_path, dirs_to_delete):
    if os.path.exists(dir_path):
        files = os.listdir(dir_path)
        if files is None or len(files) == 0:
            return
        for file in files:            
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                #print(f"Deleted file: {file_path}") 
            elif os.path.isdir(file_path):
                #shutil.rmtree(file_path)
                dirs_to_delete.insert(0, file_path)
        # if we get here, files are gone, directories need processing
        if dirs_to_delete and len(dirs_to_delete) > 0:
            for dir in dirs_to_delete:
                #print(f"Processing directory: {dir}")
                dir_files = os.listdir(dir)
                if dir_files is None or len(dir_files) == 0:
                    return
                # recursive call to process the next directory
                del_files_in_dir(dir, dirs_to_delete) 
            # after processing all directories, we can delete them    
            for dir in dirs_to_delete:
                os.rmdir(dir)
                #print(f"Remaining directories to delete: {dirs_to_delete}")            
        else:
            return   
    else:
        print(f"'{dir_path}' directory does not exist.")

def copy_files(src_dir, dest_dir):
    if os.path.exists(src_dir):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        files = os.listdir(src_dir)
        for file in files:
            src_file_path = os.path.join(src_dir, file)
            dest_file_path = os.path.join(dest_dir, file)
            if os.path.isfile(src_file_path):
                shutil.copy2(src_file_path, dest_file_path)
                #print(f"Copied file: {src_file_path} to {dest_file_path}")
            elif os.path.isdir(src_file_path):
                copy_files(src_file_path, dest_file_path)
    else:
        print(f"'{src_dir}' directory does not exist.")
