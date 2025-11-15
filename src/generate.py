import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):    
    splitted = markdown.split("\n")
    for line in splitted:
        if line.strip().startswith("# "):
            return line.strip("# ").strip()
    raise Exception("No h1 header")

def generate_page(from_path, template_path, dest_path):
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
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)    
    

