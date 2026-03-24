from markdown_blocks import markdown_to_html_node
from htmlnode import *

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