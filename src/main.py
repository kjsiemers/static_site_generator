from copy_static import del_files_in_dir, copy_files

def main():
    #print("Hello from static-site-generator!")
    del_files_in_dir("./public", [])
    copy_files("./static", "./public")


if __name__ == "__main__":
    main()
