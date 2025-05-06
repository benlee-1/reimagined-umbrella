from utils.convert_text_node import text_node_to_html_node
from src.parentnode import ParentNode
from src.textnode import TextNode, TextType
from src.utils.text_to_textnodes import text_to_textnodes
from src.utils.markdown_to_blocks import markdown_to_blocks
from src.blocktype import BlockType, block_to_block_type
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode


def markdown_to_html_node(markdown):
    #1. split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    children_for_total = []
    #loop over each block
    for block in blocks:
        #1.determine type of block
        block_type = block_to_block_type(block)
        #2. based on type of block, create a new HTMLNode with proper data
        if(block_type == BlockType.CODE):
            code_parent_node = handle_code_block(block)
            children_for_total.append(code_parent_node)
        elif(block_type == BlockType.HEADING):
           heading_parent_node = handle_heading_block(block)
           children_for_total.append(heading_parent_node)
        elif(block_type == BlockType.ORDERED_LIST):
            ordered_list_block = handle_ordered_list_block(block)
            children_for_total.append(ordered_list_block)
        elif(block_type == BlockType.UNORDERED_LIST):
            unordered_list_block = handle_unordered_list_block(block)
            children_for_total.append(unordered_list_block)
        elif(block_type == BlockType.PARAGRAPH):
            # Replace internal newlines with spaces
            block = block.replace('\n', ' ')
            tag = blocktype_to_tag.get(block_type)
            if tag:
                children_for_total.append(ParentNode(tag, text_to_children(block)))
        elif block_type == BlockType.QUOTE:
            block = block.replace('\n', ' ')
            tag = blocktype_to_tag.get(block_type)
            if tag:
                children_for_total.append(ParentNode(tag, text_to_children(block)))

    return ParentNode('div', children_for_total)

    
def text_to_children(text):
    #1. convert text to textnodes
    textnodes = text_to_textnodes(text)
    #2. convert textnodes to HTMLNodes
    return [text_node_to_html_node(textnode) for textnode in textnodes]

blocktype_to_tag = {
    BlockType.PARAGRAPH: "p",
    BlockType.QUOTE: "blockquote",
    # UNORDERED_LIST is handled separately
    # ORDERED_LIST is handled separately
    # CODE is handled separately
    # HEADING is handled separately
}

def handle_code_block(block):
    code_text = block[3:-3].strip()
    return ParentNode ('pre', [ParentNode('code', [LeafNode(None, code_text)])])
     
def handle_heading_block(block):
    level = 0
    while level < len(block) and block[level] == "#":
        level += 1
     # Clamp level between 1-6
    level = min(max(level, 1), 6)
    tag = f"h{level}"
    return ParentNode(tag, text_to_children(block[level:].strip()))

def handle_unordered_list_block(block):
    lines = block.split('\n')
    li_nodes = []
    for line in lines:
        # Remove the "- " at the start
        item_text = line[2:].strip() if line.startswith('- ') else line.strip()
        li_nodes.append(ParentNode('li', text_to_children(item_text)))
    return ParentNode('ul', li_nodes)

def handle_ordered_list_block(block):
    lines = block.split('\n')
    li_nodes = []
    for line in lines:
        # Remove the "1. ", "2. ", etc. at the start
        dot_index = line.find('. ')
        item_text = line[dot_index+2:].strip() if dot_index != -1 else line.strip()
        li_nodes.append(ParentNode('li', text_to_children(item_text)))
    return ParentNode('ol', li_nodes)