import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "testval")
        node2 = HTMLNode("a", "testval")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("a", "testval")
        node2 = HTMLNode("img", "testimg")
        self.assertNotEqual(node, node2)

    def test_empty_node_set_none(self):
        node = HTMLNode()
        if not (node.tag == None and node.value == None and node.children == None and node.props == None):
            raise Exception("Empty none defaulting not working")
    
    def test_props_to_html(self):
        node = HTMLNode("a", "val", None, {
        "href": "https://www.google.com",
        "target": "_blank", }
        )
        if node.props_to_html() !=  ' href="https://www.google.com" target="_blank"':
            raise Exception("props_to_html not working")