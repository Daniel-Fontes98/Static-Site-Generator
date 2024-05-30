from markdown_blocks import markdown_to_blocks, markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown_to_blocks(markdown)
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")
    raise ValueError("H1 header not found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        markdown = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path:
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as to_file:
        to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)

    for dir in dirs:
        next_dir = os.path.join(dir_path_content, dir)
        next_dest_dir = os.path.join(dest_dir_path, dir)
        if os.path.isfile(next_dir):
            generate_page(next_dir, template_path, next_dest_dir[:-2] + "html")
            continue
        generate_pages_recursive(next_dir, template_path, next_dest_dir)
