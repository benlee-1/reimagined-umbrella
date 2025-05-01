from .split_nodes import *
import unittest

class test_split_nodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsjkBB.png)", TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "This is text with an ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://i.imgur.com/zjjcJKZ.png")
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "another")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[3].url, "https://i.imgur.com/dfsjkBB.png")

    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://boot.dev) and [another](https://blog.boot.dev)", TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://boot.dev")
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "another")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[3].url, "https://blog.boot.dev")

    def test_split_nodes_image_multiple(self):
        nodes = [
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            TextNode("And another ![image](https://i.imgur.com/dfsjkBB.png) here", TextType.TEXT)
        ]
        nodes = split_nodes_image(nodes)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is text with an ")
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[2].text, "And another ")
        self.assertEqual(nodes[3].text, "image")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[4].text, " here")

    def test_split_nodes_link_multiple(self):
        nodes = [
            TextNode("This is text with a [link](https://boot.dev)", TextType.TEXT),
            TextNode("And another [link](https://blog.boot.dev) here", TextType.TEXT)
        ]
        nodes = split_nodes_link(nodes)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[2].text, "And another ")
        self.assertEqual(nodes[3].text, "link")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[4].text, " here")
