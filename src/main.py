import os
from pathlib import Path
import shutil

from markdown_to_html import markdown_to_html_node


def copy_from_static_to_public():
    SRC_DIR = './static'
    DEST_DIR = './public'

    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)
    
    os.makedirs(DEST_DIR)

    for root, dirs, files in os.walk(SRC_DIR):
        rel_path = os.path.relpath(root, SRC_DIR)
        dest_path = os.path.join(DEST_DIR, rel_path)
        
        for dir_name in dirs:
            dir_path = os.path.join(dest_path, dir_name)
            os.makedirs(dir_path, exist_ok=True)
        
        for file_name in files:
            source_file = os.path.join(root, file_name)
            dest_file = os.path.join(dest_path, file_name)
            shutil.copy2(source_file, dest_file)

def extract_title(markdown):
    
    for line in markdown.split('\n'):
        line = line.strip()
        if line.startswith('# '):
            header = line[2:]
            header = header.strip()
            return header

    raise ValueError("No header in markdown file")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copy_from_static_to_public()
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()