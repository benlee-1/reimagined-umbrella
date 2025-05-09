import os

from utils.extract_title import extract_title
from utils.markdown_to_html_node import markdown_to_html_node
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #get all parts of the 
    items = os.listdir(dir_path_content)
    with open(template_path, 'r') as f:
        template = f.read()

    #check if item is a file, if not, call same method recursively
    for item in items:
        joined_dir_path = os.path.join(dir_path_content, item)
        joined_destination_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(joined_dir_path):

    # file name ends in .md, create an .html file using the template.html
            if item[-3:] == ".md":
                #read and save the source string
                with open(os.path.join(dir_path_content, item)) as f:
                    markdown = f.read()

                #create the html string
                html_string = markdown_to_html_node(markdown).to_html()
                title = extract_title(markdown)
                final = template.replace("{{ Title }}", title)
                final = final.replace("{{ Content }}", html_string)

                #write to destination path - make html file
                with open(joined_destination_path.replace(".md",".html"), "w") as f:
                    f.write(final)
            else:
                continue
        
        else:
            os.makedirs(joined_destination_path, exist_ok=True)
            generate_pages_recursive(joined_dir_path, template_path, joined_destination_path)