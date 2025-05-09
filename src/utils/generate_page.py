import os
from utils.extract_title import extract_title
from utils.markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown file
    with open(from_path, 'r') as f:
        markdown = f.read()
    
    # Read the template file\
    with open(template_path, 'r') as f:
        template = f.read()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    final = template.replace("{{ Title }}", title)
    final = final.replace("{{ Content }}", html_string)

    #make directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    #write to destination file
    with open(dest_path, "w") as f:
        f.write(final)