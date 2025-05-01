from typing import List
from .extract_markdown import * 
from src.textnode import TextNode, TextType

def check_for_nodes(node, extraction_function: callable, is_image: bool ) -> List[TextNode]:
    to_return = []
    if node.text_type != TextType.TEXT:
        to_return.append(node)
        return to_return
    
    extracted_images = extraction_function(node.text)
    if extracted_images:
        current_text = node.text
        for alt_text, url in extracted_images:
            pattern = f"![{alt_text}]({url})" if is_image else f"[{alt_text}]({url})"
            parts = current_text.split(pattern,1)
            if parts[0]:
                to_return.append(TextNode(parts[0], TextType.TEXT))
                
            node_type = TextType.IMAGE if is_image else TextType.LINK
            to_return.append(TextNode(alt_text, node_type, url))
            current_text = parts[1] if len(parts) > 1 else ""           
        if current_text:
            to_return.append(TextNode(current_text, TextType.TEXT))
    else:
        to_return.append(node)
    
    return to_return

def split_nodes_image(old_nodes : List[TextNode]):
    to_return = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            to_return.extend(check_for_nodes(node, extract_markdown_images, True))
        else: to_return.append(node)
    return to_return
        
def split_nodes_link(old_nodes: List[TextNode]):
    to_return = []
    for node in old_nodes:
        to_return.extend(check_for_nodes(node, extract_markdown_links, False))
    return to_return