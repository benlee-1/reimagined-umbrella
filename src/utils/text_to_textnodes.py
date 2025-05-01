from src.textnode import TextNode, TextType
from src.utils.split_nodes import split_nodes_image, split_nodes_link
from src.utils.inline_conversion import split_nodes_delimiter

def text_to_textnodes(text):
    # Create initial text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Process each type of markdown in order
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes