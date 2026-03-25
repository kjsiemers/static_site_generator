import sys

from copy_static import del_files_in_dir, copy_files
from generate_page import generate_page, generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    #print("Hello from static-site-generator!")
    del_files_in_dir("./docs", [])
    copy_files("./static", "./docs")
    #generate_page("./content/index.md", "./template.html", "./docs/index.html", basepath)
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()
