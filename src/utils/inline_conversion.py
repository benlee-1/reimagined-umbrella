from ..leafnode import LeafNode
from ..textnode import *

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