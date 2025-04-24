from leafnode import LeafNode
from textnode import *

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value= text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":"alt text"})
        case _:
            raise Exception("Invalid Text Type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(handle_conversion(node, delimiter, text_type))
        else: 
            new_nodes.append(node)
    return new_nodes

def handle_conversion(node, delimiter, text_type):
    stored_strings = node.text.split(delimiter)
    if len(stored_strings) % 2 == 0:
        raise Exception("There is a unmatched delimiter")
    return_nodes = []
    for i in range(0, len(stored_strings)):
        segment_text = stored_strings[i]

        if segment_text == "" and i % 2 != 0:
            raise ValueError(f"invalid markdown syntax:empty section between delimiters '{delimiter}'")
        
        if segment_text == "":
            continue
        if i % 2 == 0:
            return_nodes.append(TextNode(segment_text, TextType.TEXT))
        else:
            return_nodes.append(TextNode(segment_text, text_type))
    return return_nodes