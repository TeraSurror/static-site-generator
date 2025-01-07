import unittest

from htmlnode import LeafNode, ParentNode
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_heading_block_to_html_node(self):
        text = "# This is a heading"
        text_html_node = LeafNode(
            tag=None,
            value="This is a heading",
            props=None
        )
        h1_node = ParentNode(
            tag="h1",
            children=[text_html_node],
            props=None,
        )
        parent_node = ParentNode(
            tag='div',
            children=[h1_node],
            props=None,
        )

        conv_html_node = markdown_to_html_node(text)

        self.assertEqual(conv_html_node.to_html(), parent_node.to_html())