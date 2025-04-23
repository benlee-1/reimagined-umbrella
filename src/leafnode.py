from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None): 
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        to_return = f"<{self.tag}>"
        prop_string = self.props_to_html()
        if prop_string:
            to_return = f"<{self.tag}" + prop_string +">"
        to_return = to_return + self.value + f"</{self.tag}>"

        return to_return
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.props == other.props
        

