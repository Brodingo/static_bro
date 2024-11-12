import os

from markdown_html import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line.split(' ', 1)[1].strip()
    raise ValueError("Title not found in markdown")

def generate_content(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    print("Reading markdown file")
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()
    print(f"Markdown file length: {len(markdown)}")

    print("Reading template file")
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    new_page_html = template.replace('{{ Title }}', title).replace('{{ Content }}', html)

    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    new_page_file = open(dest_path, 'w')
    new_page_file.write(new_page_html)
    new_page_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages from {dir_path_content} with {template_path} in {dest_dir_path}")
    dir_paths = os.listdir(dir_path_content)
    for path in dir_paths:
        print(f"Current path: {path}")
        full_source_path = os.path.join(dir_path_content, path)
        if os.path.isfile(full_source_path) and path.endswith(".md"):
            new_file_name = f"{path.rstrip('.md')}.html"
            print(f"Generating HTML file {new_file_name} from markdown file {path}")
            full_dest_path = os.path.join(dest_dir_path, new_file_name)
            generate_content(full_source_path, template_path, full_dest_path)
        if os.path.isdir(full_source_path):
            full_dest_dir_path = os.path.join(dest_dir_path, path)
            print("Recursively generating pages in subdirectory")
            generate_pages_recursive(full_source_path, template_path, full_dest_dir_path)