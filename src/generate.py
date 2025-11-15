import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):    
    splitted = markdown.split("\n")
    for line in splitted:
        if line.strip().startswith("# "):
            return line.strip("# ").strip()
    raise Exception("No h1 header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        with open(from_path, "r") as md:
            markdown = md.read()
        with open(template_path, "r") as temp:
            template = temp.read()
    except Exception as e:
        print(f"Can not open files. {e}")
        return
    
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    temp_splited = template.split("{{ Title }}")
    template = title.join(temp_splited)
    temp_splited = template.split("{{ Content }}")
    template = html.join(temp_splited)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
    
#def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
#    content_path = Path(dir_path_content)
#    content_files = content_path.rglob("*.md")
#
#    for file in content_files:
#        file_dest = str(file).replace("content/", "public/", 1)
#        file_dest = file_dest.replace(".md", ".html", 1)
#        generate_page(str(file), template_path, file_dest, basepath)