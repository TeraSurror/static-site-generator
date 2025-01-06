import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a test", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test", TextType.BOLD_TEXT)
        self.assertEqual(node1, node2)
    
    def test_repr(self):
        node = TextNode("This is a test", TextType.BOLD_TEXT)
        self.assertEqual(str(node), "TextNode(This is a test, bold, None)")

    def test_empty_url(self):
        node = TextNode("This is a test", TextType.BOLD_TEXT)
        self.assertIsNone(node.url)
    
    def test_fields(self):
        node = TextNode("This is a test", TextType.BOLD_TEXT, "http://localhost:9090")
        self.assertEqual(node.text, "This is a test")
        self.assertEqual(node.text_type.value, "bold")
        self.assertEqual(node.url, "http://localhost:9090")

if __name__ == "__main__":
    unittest.main()