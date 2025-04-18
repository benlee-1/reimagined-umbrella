class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other_node):
        if not isinstance(other_node, HTMLNode):
            return False
        return (self.tag == other_node.tag and self.value == other_node.value and self.children == other_node.children and self.props == other_node.props)

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""
        props_list = []
        for key, value in self.props.items():
            props_list.append(f'{key}="{value}"')
        return " " + " ".join(props_list)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"