import unittest
from src.utils.extract_title import extract_title

class test_extract_title(unittest.TestCase):
    def test_extract_title(self):
        val_extracted = extract_title("# Hello")
        self.assertEqual(val_extracted, "Hello")