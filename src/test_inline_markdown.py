import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_code(self):
        node1 = TextNode('This is a `code` block', TextType.NORMAL_TEXT)
        node2 = TextNode('This `is a code` block', TextType.NORMAL_TEXT)
        old_nodes = [node1, node2]

        got = split_nodes_delimiter(old_nodes, '`', TextType.CODE_TEXT)

        expected = [
            TextNode('This is a ', TextType.NORMAL_TEXT),
            TextNode('code', TextType.CODE_TEXT),
            TextNode(' block', TextType.NORMAL_TEXT),
            TextNode('This ', TextType.NORMAL_TEXT),
            TextNode('is a code', TextType.CODE_TEXT),
            TextNode(' block', TextType.NORMAL_TEXT),
        ]

        self.assertEqual(got, expected)

    def test_split_nodes_italics(self):
        node = TextNode('This *is* a *code* block', TextType.NORMAL_TEXT)
        old_nodes = [node]

        got = split_nodes_delimiter(old_nodes, '*', TextType.ITALIC_TEXT)

        expected = [
            TextNode('This ', TextType.NORMAL_TEXT),
            TextNode('is', TextType.ITALIC_TEXT),
            TextNode(' a ', TextType.NORMAL_TEXT),
            TextNode('code', TextType.ITALIC_TEXT),
            TextNode(' block', TextType.NORMAL_TEXT),
        ]

        self.assertEqual(got, expected)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        got = extract_markdown_images(text)

        self.assertEqual(got, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        got = extract_markdown_links(text)

        self.assertEqual(got, expected)
