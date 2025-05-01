from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block) -> BlockType:
    if block.startswith("#"):
        return BlockType.HEADING
    elif is_code_block(block):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list_block(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list_block(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def is_code_block(block:str):
    return block.startswith("```") and block.endswith("```")

def is_quote_block(block:str):
    lines = block.split("\n")
    for line in lines:
        if line.startswith(">"):
            return True
    return False

def is_unordered_list_block(block:str):
    lines = block.split("\n")
    for line in lines:
        if line.startswith("- "):
            return True
    return False

def is_ordered_list_block(block:str):
    lines = block.split("\n")
    sequence = []
    for i, line in enumerate(lines):
        parts = line.split(". ", 1)
        if len(parts) != 2:
            return False

        if not parts[0].isdigit():
            return False
        
        expected_number = i + 1
        
        if int(parts[0]) != expected_number:
            return False
        
    return True

    
def is_heading(block: str) -> bool:
    # Check if it starts with 1-6 # characters followed by a space
    if not block.startswith('#'):
        return False
    
    # Find position of first non-# character
    i = 0
    while i < len(block) and i < 6 and block[i] == '#':
        i += 1
    
    # Check if the next character is a space
    return i <= 6 and i < len(block) and block[i] == ' '

