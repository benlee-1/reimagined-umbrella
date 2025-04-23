from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires tag")
        if not self.children:
            raise ValueError("Children are required for ParentNode")
        
        to_return = f"<{self.tag}>"

        for child in self.children:
            to_return += child.to_html()
        
        return to_return + f"</{self.tag}>"