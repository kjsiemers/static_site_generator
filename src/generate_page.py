from markdown_blocks import markdown_to_html_node
from htmlnode import *
import os

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, 'r') as f:
        markdown = f.read()
    title = extract_title(markdown)
    #print(f"Extracted title: {title}")
    html_content = markdown_to_html_node(markdown).to_html()  # Assuming you have a function to convert markdown to HTML
    #print(f"Generated HTML content:\n{html_content}\n==========") 
    with open(template_path, 'r') as f:
        template = f.read()
    p = template.replace("{{ Title }}", title)
    page_content = p.replace("{{ Content }}", html_content)
    #print(f"Generated page content:\n{page_content}\n==========")
    with open(dest_path, 'w') as fo:
        fo.write(page_content)

def generate_pages_recursive(src_dir, template_path, dest_dir):
    if os.path.exists(src_dir):
        files = os.listdir(src_dir)
        if files is None or len(files) == 0:
            return
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        files = os.listdir(src_dir)
        for file in files:
            src_file_path = os.path.join(src_dir, file)
            if os.path.isfile(src_file_path) and file.endswith(".md"):
                dest_file_path = os.path.join(dest_dir, file[:-3] + ".html")
                generate_page(src_file_path, template_path, dest_file_path)
            elif os.path.isdir(src_file_path):
                dest_file_path = os.path.join(dest_dir, file)
                generate_pages_recursive(src_file_path, template_path, dest_file_path)
    else:
        print(f"'{src_dir}' directory does not exist.")
