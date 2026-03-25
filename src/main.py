from copy_static import del_files_in_dir, copy_files
from generate_page import generate_page, generate_pages_recursive

def main():
    #print("Hello from static-site-generator!")
    del_files_in_dir("./public", [])
    copy_files("./static", "./public")
    #generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()
