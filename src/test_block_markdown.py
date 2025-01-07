import unittest

from block_markdown import block_to_block_type, markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '''
* This is the first list item in a list block
* This is a list item
* This is another list item 
'''.strip()           
        ]

        got = markdown_to_blocks(markdown)

        self.assertEqual(expected, got)

    def test_block_to_block_type_heading(self):
        block1 = '# Heading 1'
        block2 = '## Heading 2'
        block3 = '### Heading 3'
        block4 = '#### Heading 4'
        block5 = '##### Heading 5'
        block6 = '###### Heading 6'

        block_type = "heading"

        self.assertEqual(block_to_block_type(block1), block_type)
        self.assertEqual(block_to_block_type(block2), block_type)
        self.assertEqual(block_to_block_type(block3), block_type)
        self.assertEqual(block_to_block_type(block4), block_type)
        self.assertEqual(block_to_block_type(block5), block_type)
        self.assertEqual(block_to_block_type(block6), block_type)

