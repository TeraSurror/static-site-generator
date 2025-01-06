import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode().to_html()

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        html_node = HTMLNode(tag="a", props=props)
        self.assertEquals(html_node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        html_node = HTMLNode("h1", "This is some text", None, None)
        self.assertEquals(str(html_node), "HTMLNode(h1, This is some text, None, None)")



if __name__ == "__main__":
    unittest.main()