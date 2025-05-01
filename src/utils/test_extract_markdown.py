import unittest
from .extract_markdown import *

class test_extract_markdown(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        produced_tuple_list= extract_markdown_images(text)
        test_tuple_list = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(produced_tuple_list, test_tuple_list)
    
    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        produced_tuple_list = extract_markdown_links(text)
        test_tuple_list = [("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(produced_tuple_list, test_tuple_list)
