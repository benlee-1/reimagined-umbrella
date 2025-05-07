from textnode import *
from utils.file_utils import copy_static_to_public
#./main.sh
# hello world
def main():
    tx_node = TextNode("test", TextType.IMAGE, "boot.dev")
    print(tx_node)

    copy_static_to_public("static", "public")
main()