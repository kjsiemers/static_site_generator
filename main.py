def main():
    print("Hello from static-site-generator!")
    del_files_in_dir("/home/kent/projects/github.com/static_site_generator/public", [])

def del_files_in_dir(dir_path, dirs_to_delete):
    import os
    import shutil

    if os.path.exists(dir_path):
        files = os.listdir(dir_path)
        for file in files:            
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}") 
            elif os.path.isdir(file_path):
                #shutil.rmtree(file_path)
                dirs_to_delete.append(file_path)
        #shutil.rmtree(public_dir)
        # if we get here, files are gone, directories need processing
        for dir in dirs_to_delete:
            print(f"Processing directory: {dir}")
            del_files_in_dir(dir, dirs_to_delete)
            os.rmdir(dir)
            print(f"Deleted directory: {dir}")
            del dirs_to_delete[dirs_to_delete.index(dir)]
            print(f"Remaining directories to delete: {dirs_to_delete}")
    else:
        print(f"'{dir_path}' directory does not exist.")


if __name__ == "__main__":
    main()
