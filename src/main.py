from textnode import *
from utils.file_utils import copy_static_to_public
from utils.generate_page import generate_page
#./main.sh
# hello world
def main():
    tx_node = TextNode("test", TextType.IMAGE, "boot.dev")
    print(tx_node)

    copy_static_to_public("static", "public")
    generate_page("content/index.md","template.html", "public/index.html")

if __name__ == "__main__":
    main()