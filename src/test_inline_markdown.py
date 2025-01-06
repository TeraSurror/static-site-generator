import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.IMAGE_TEXT, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode(
            "to youtube", TextType.IMAGE_TEXT, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        got = split_nodes_image([node])

        self.assertEqual(got, expected)

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINK_TEXT, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode(
            "to youtube", TextType.LINK_TEXT, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        got = split_nodes_link([node])

        self.assertEqual(got, expected)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("obi wan image", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]
        got = text_to_textnodes(text)

        self.assertEqual(got, expected)
            
            


