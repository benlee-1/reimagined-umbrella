from leafnode import LeafNode
from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            # Split the text by the delimiter
            parts = node.text.split(delimiter)
            
            # If there's an even number of parts, it means there's an unmatched delimiter
            if len(parts) % 2 == 0:
                raise Exception(f"Invalid markdown syntax: unmatched delimiter '{delimiter}'")
            
            # If there's only one part, no delimiters were found
            if len(parts) == 1:
                new_nodes.append(node)
                continue
            
            # Process each part
            for i in range(len(parts)):
                if parts[i] == "":
                    continue
                if i % 2 == 0:
                    # Even indices are text outside delimiters
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                else:
                    # Odd indices are text inside delimiters
                    new_nodes.append(TextNode(parts[i], text_type))
        else:
            new_nodes.append(node)
    
    return new_nodes

def handle_conversion(node, delimiter, text_type):
    # Split the text by the delimiter
    parts = node.text.split(delimiter)
    print(f"Split parts: {parts}")
    
    # If there's an even number of parts, it means there's an unmatched delimiter
    if len(parts) % 2 == 0:
        raise Exception(f"Invalid markdown syntax: unmatched delimiter '{delimiter}'")
    
    # If there's only one part, no delimiters were found
    if len(parts) == 1:
        print("No delimiters found, returning original node")
        return [node]
    
    new_nodes = []
    for i in range(len(parts)):
        if parts[i] == "":
            continue
        if i % 2 == 0:
            # Even indices are text outside delimiters
            new_nodes.append(TextNode(parts[i], TextType.TEXT))
        else:
            # Odd indices are text inside delimiters
            new_nodes.append(TextNode(parts[i], text_type))
    
    print(f"Created nodes: {new_nodes}")
    return new_nodes 