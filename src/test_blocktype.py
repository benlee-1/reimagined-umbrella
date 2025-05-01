from src.blocktype import BlockType, block_to_block_type
import unittest

class test_blocktype(unittest.TestCase):

    def test_block_to_block_type(self):
        # Test heading block
        heading_block = "# This is a heading"
        result = block_to_block_type(heading_block)
        self.assertEqual(result, BlockType.HEADING)
        
        # Test ordered list
        ordered_list = "1. First item\n2. Second item"
        result = block_to_block_type(ordered_list)
        self.assertEqual(result, BlockType.ORDERED_LIST)
        
        # Test quote block
        quote_block = "> This is a quote"
        result = block_to_block_type(quote_block)
        self.assertEqual(result, BlockType.QUOTE)
        
        # Test code block
        code_block = "```\nsome code\n```"
        result = block_to_block_type(code_block)
        self.assertEqual(result, BlockType.CODE)
        
        # Test unordered list
        unordered_list = "- First item\n- Second item"
        result = block_to_block_type(unordered_list)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
        
        # Test paragraph
        paragraph = "This is a regular paragraph"
        result = block_to_block_type(paragraph)
        self.assertEqual(result, BlockType.PARAGRAPH)
        

        
