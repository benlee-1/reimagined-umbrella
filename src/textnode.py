from enum import Enum

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other_text_node):
        #if all three properties between two nodes are equal
        return self.text == other_text_node.text and self.text_type == other_text_node.text_type and self.url == other_text_node.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    