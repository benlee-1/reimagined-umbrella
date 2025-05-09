import os

from utils.extract_title import extract_title
from utils.generate_page import generate_page
from utils.markdown_to_html_node import markdown_to_html_node
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    items = os.listdir(dir_path_content)

    #check if item is a file, if not, call same method recursively
    for item in items:
        joined_dir_path = os.path.join(dir_path_content, item)
        joined_destination_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(joined_dir_path):

    # file name ends in .md, create an .html file using the template.html
            if item.endswith(".md"):
                generate_page(joined_dir_path, template_path, joined_destination_path.replace(".md",".html"), basepath)
            else:
                continue
        
        else:
            os.makedirs(joined_destination_path, exist_ok=True)
            generate_pages_recursive(joined_dir_path, template_path, joined_destination_path, basepath)