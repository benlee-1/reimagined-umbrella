import unittest
from leafnode import *


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "this is a paragraph")
        node2 = LeafNode("p", "this is a paragraph")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("a","this is a text node - image type")
        node2 = LeafNode("p","this is a text node - code type")
        self.assertNotEqual(node, node2)
        
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')