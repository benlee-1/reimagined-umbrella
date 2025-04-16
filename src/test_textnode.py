import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("this is a text node - image type", TextType.IMAGE)
        node2 = TextNode("this is a text node - code type", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_none_working(self):
        node = TextNode("test", TextType.LINK)
        if node.url!= None :
            raise Exception("empty URLs need to be None")

if __name__ == "__main__":
    unittest.main()
