from textnode import *
from utils.file_utils import copy_static_to_public
from utils.generate_page import generate_page
from utils.generate_pages_recursive import generate_pages_recursive
#./main.sh
def main():
    print("page generator started!")
    copy_static_to_public("static", "public")
    # generate_page("content/index.md","template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()