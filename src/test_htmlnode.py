import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode().to_html()

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_parent_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "a",
                    [LeafNode('b', "Bold text")],
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><a><b>Bold text</b></a><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_parent_nested_parents_exception(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    None,
                    [LeafNode('b', "Bold text")],
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_convert_text_to_html_text(self):
        text_node = TextNode(
            text="This is some text", 
            text_type=TextType.NORMAL_TEXT
        )
        result_html_node = LeafNode(
            tag=None,
            value=text_node.text
        )

        conv_html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(conv_html_node, HTMLNode)
        self.assertIsInstance(conv_html_node, LeafNode)
        self.assertEqual(result_html_node.value, conv_html_node.value)

    def test_convert_text_to_html_bold(self):
        text_node = TextNode(
            text="This is some text", 
            text_type=TextType.BOLD_TEXT
        )
        result_html_node = LeafNode(
            tag='b',
            value=text_node.text
        )

        conv_html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(conv_html_node, HTMLNode)
        self.assertIsInstance(conv_html_node, LeafNode)
        self.assertEqual(result_html_node.tag, conv_html_node.tag)
        self.assertEqual(result_html_node.value, conv_html_node.value)

    def test_convert_text_to_html_italic(self):
        text_node = TextNode(
            text="This is some text", 
            text_type=TextType.ITALIC_TEXT
        )
        result_html_node = LeafNode(
            tag='i',
            value=text_node.text
        )

        conv_html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(conv_html_node, HTMLNode)
        self.assertIsInstance(conv_html_node, LeafNode)
        self.assertEqual(result_html_node.tag, conv_html_node.tag)
        self.assertEqual(result_html_node.value, conv_html_node.value)

    def test_convert_text_to_html_code(self):
        text_node = TextNode(
            text="This is some text", 
            text_type=TextType.CODE_TEXT
        )
        result_html_node = LeafNode(
            tag='code',
            value=text_node.text
        )

        conv_html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(conv_html_node, HTMLNode)
        self.assertIsInstance(conv_html_node, LeafNode)
        self.assertEqual(result_html_node.tag, conv_html_node.tag)
        self.assertEqual(result_html_node.value, conv_html_node.value)

    def test_convert_text_to_html_link(self):
        text_node = TextNode(
            text="This is a link",
            url="http://localhost:8000", 
            text_type=TextType.LINK_TEXT
        )
        result_html_node = LeafNode(
            tag='a',
            value=text_node.text,
            props={'href': text_node.url}
        )

        conv_html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(conv_html_node, HTMLNode)
        self.assertIsInstance(conv_html_node, LeafNode)
        self.assertEqual(result_html_node.tag, conv_html_node.tag)
        self.assertEqual(result_html_node.props, conv_html_node.props)
        self.assertEqual(result_html_node.value, conv_html_node.value)

    def test_convert_text_to_html_image(self):
        text_node = TextNode(
            text="This is a image",
            url="http://localhost:8000", 
            text_type=TextType.IMAGE_TEXT
        )
        result_html_node = LeafNode(
            tag='img',
            value=None,
            props={'src': text_node.url, 'alt': text_node.text}
        )

        conv_html_node = text_node_to_html_node(text_node)

        self.assertIsInstance(conv_html_node, HTMLNode)
        self.assertIsInstance(conv_html_node, LeafNode)
        self.assertEqual(result_html_node.tag, conv_html_node.tag)
        self.assertEqual(result_html_node.props, conv_html_node.props)
        self.assertEqual(result_html_node.value, conv_html_node.value)
    

if __name__ == "__main__":
    unittest.main()