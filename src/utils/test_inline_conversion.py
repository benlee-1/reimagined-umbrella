from .inline_conversion import split_nodes_delimiter, TextType, TextNode
import unittest

class TestInlineConversion(unittest.TestCase):
    def test_bold(self):
        test_old_nodes = [TextNode("hello **beautiful** world", TextType.TEXT)]
        node_list =  split_nodes_delimiter(test_old_nodes, "**", TextType.BOLD)
        example_list = [
            TextNode("hello ", TextType.TEXT),
            TextNode("beautiful", TextType.BOLD),
            TextNode(" world", TextType.TEXT)
            ]                                    
        self.assertListEqual(node_list, example_list)

